from APIApp import APIApp

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import memcache

import csv
import logging
import os
import os.path
import random
import re
import types

# base memcache class

class fakesubwaycache :

    def __init__ (self) :

        self.prefix = 'fakesubwayapis2009102'

    def prepare_key (self, key) :
        return "%s_%s" % (self.prefix, key)

    def get_cache (self, key) :

        cache_key = self.prepare_key(key)

        try :
            cache = memcache.get(cache_key)
        except Exception, e :
            logging.warning("failed to get cache key '%s': %s" % (cache_key, e))            
            return None
    
        if cache :
            return cache
        
        return None

    def set_cache (self, key, data) :

        cache_key = self.prepare_key(key)

        try :
            memcache.set(cache_key, data)
        except Exception, e :
            logging.warning("failed to set cache key '%s': %s" % (cache_key, e))            
            return False

        return True
        
    def unset_cache (self, key) :

        cache_key = self.prepare_key(key)

        try :
            memcache.delete(cache_key)            
        except Exception, e :
            logging.warning("failed to unset cache key '%s': %s" % (cache_key, e))            
            return False
        
        return True
    
# base service/agency data class

class fakesubwaydata (fakesubwaycache) :

    def __init__ (self) :

        fakesubwaycache.__init__(self)

    def load_data (self, source, force=True) :

        cache_key = "%s_%s" % (self.id, source)
        data = None
        
        if not force :
            data = self.get_cache(cache_key)
        
        if not data :
            data = self.read_data(source)

        if not data :
            logging.error("failed to load any '%s' data for '%s'" % (source, self.id))
            return None
        
        self.set_cache(cache_key, data)
        return data

    def read_data (self, source) :

        path = self.generate_data_path(source)

        try :
            reader = csv.DictReader(open(path))
        except Exception, e :
            logging.error("failed to open '%s' for reading: %s" % (path, e))
            return None

        if source == 'stops' :
            return self.read_stops_data(reader)

        if source == 'agency' :
            return self.read_agency_data(reader)

        if source == 'routes' :
            return self.read_routes_data(reader)

        logging.error("unknown source: '%s'" % source)
        return None
    
    def read_stops_data (self, reader) :

        stations = {}

        for row in reader :
            code, data = self.format_station(row)
            code = self.prepare_station_code(code)
            stations[ code ] = data
        
        return stations
    
    def read_agency_data (self, reader) :

        data = reader.next()

        return {
            'id' : self.id,
            'name' : data['agency_name'],
            'url' : data['agency_url'],
            'url_template' : data['fsa_url_template'],
            }

    def read_routes_data (self, reader) :

        routes = {}
        
        for row in reader :
            routes[ row['route_id' ] ] = row['route_long_name']

        return routes
    
    def format_station (self, row) :

        uid = row['fsa_stop_id']
        name = row['stop_name']
        
        data = { 'name' : name }

        if row['stop_lat'] != '' :
            data['lat'] = float(row['stop_lat'])

        if row['stop_lon'] != '' :
            data['lon'] = float(row['stop_lon'])

        if row.has_key('fsa_stop_routes') and row['fsa_stop_routes'] :
            routes = row['fsa_stop_routes'].split(";")
            data['line'] = routes
            
        return (uid, data)

    def generate_data_path (self, file) :
        app_root = os.path.dirname(os.path.dirname(__file__))
        data_root = os.path.join(app_root, 'data', self.id)

        file = "%s.txt" % file
        
        path = os.path.join(data_root, file)
        return path

# base service/agency class

class fakesubwayservice (fakesubwaydata) :

    def __init__ (self, id) :

        fakesubwaydata.__init__(self)
        
        self.id = id
        
        self.stations = self.load_data('stops')
        self.service = self.load_data('agency')
        self.lines = self.load_data('routes')

    def prepare_station_code (self, code) :

        if not code:
            logging.error("invalid station code!")
            return ''
        
        if type(code) == types.IntType :
            return code
        
        if re.match('^\d+$', code) :
            return int(code)

        return code

    def generate_station_url (self, code, **more) :

        code = self.prepare_station_code(code)
        
        try :
            return self.service['url_template'] % code
        except :
            return "http://%s/%s/station/%s" % (self.request.host, self.service['id'], code)
    
    def prepare_api_output (self, code, **more) :

        code = self.prepare_station_code(code)

        out = {
            'code' : code,
            'service' : self.service['id'],
            'name' :  { '_content' : self.stations[code]['name'] },
            'url' : { '_content' : self.generate_station_url(code, **more) },
            }

        if self.stations[code].has_key('lat') and self.stations[code].has_key('lon'):

            out['location'] = {
                'lat' : self.stations[code]['lat'],
                'lon' : self.stations[code]['lon']
                }
            
        if self.stations[code].has_key('line') :
            out['lines'] = {}
            out['lines']['line'] = []

            for line_code in self.stations[code]['line'] :

                out['lines']['line'].append({
                    'code' : line_code,
                    '_content' : self.lines[line_code]
                    })

        return out

# base www request class

class fakesubwayrequest (webapp.RequestHandler) :

    def __init__ (self) :
        webapp.RequestHandler.__init__(self)        

    def display (self, template_name, template_values={}) :

        template_values['host'] = "http://%s" % self.request.host
        
        root = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(root, 'templates', template_name)
    
        self.response.out.write(template.render(path, template_values))
        
    
# base api (method) class

class fakesubwayapi (fakesubwayrequest, APIApp) :

    def __init__ (self) :
        fakesubwayrequest.__init__(self)        
        APIApp.__init__(self, 'xml')
        
    def generate_info (self, code, **more) :

        code = self.prepare_station_code(code)
        
        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')            
            return None

        out = self.prepare_api_output(code, **more)
        
        self.api_ok({'station' : out})
        return

# base api docs class

class fakesubwayapidocs (fakesubwayrequest) :

    def get (self) :
        self.display("intro.html")
        return

    def prepare_stations (self, **args) :

        prepared = []

        codes = self.stations.keys()
        codes.sort()

        for code in codes :

            if code == '' :
                continue

            name = self.stations[code]['name']

            # For example, TFL

            if args.has_key('generate_compound_ids') and args['generate_compound_ids'] == True :
                if self.stations[code].has_key('line') :

                    for ln in self.stations[code]['line'] :

                        line = self.lines[ln]
                        
                        code2 = "%s-%s" % (code, ln)                
                        name2 = "%s (%s line)" % (name, line.capitalize())

                        prepared.append((code2, name2))                    

                    continue
                
            #

            if self.stations[code].has_key('line') :

                station_lines = []
                
                for ln in self.stations[code]['line'] :
                    
                    line = self.lines[ln]
                    station_lines.append(line.title())

                count = len(station_lines)
                
                if count == 0 :
                    pass
                elif count == 1 :
                    name = "%s (%s line)" % (name, station_lines[0])
                else :
                    name = "%s (%s lines)" % (name, ", ".join(station_lines))

            #
            
            prepared.append((code, name))
                    
        return prepared

    def show_docs (self) :

        stations = self.prepare_stations()
        offset = random.randrange(0, len(stations))

        api = APIApp()
        
        example_code = stations[offset][0]
        example_rsp = self.prepare_api_output(example_code)
        example_xml = api.serialize_xml('rsp', example_rsp)
        
        title = "%s (%s)" % (self.service['id'].upper(), self.service['name'])        
        template = "%s.html" % self.service['id']
        
        template_vars = {
            'service' : self.service,
            'stations' : stations,
            'title' : title,
            'example_code' : example_code,
            'example_xml' : example_xml,
            }
        
        self.display('service.html', template_vars)

# base station page clas

class fakesubwaystation (fakesubwayrequest) :

    def show_station (self, code) :

        code = self.prepare_station_code(code)
        
        if not self.stations.has_key(code) :
            self.error(404)
            return

        title = "%s (%s)" % (self.stations[code]['name'], self.service['name'])
        
        template_values = {
            'code' : code,
            'service' : self.service,
            'station' : self.stations[code],
            'title' : title
        }
        
        self.display('station.html', template_values)
        return

    def do_redirect (self, code, **more) :
        url = self.generate_station_url(code, **more)
        self.redirect(url)
