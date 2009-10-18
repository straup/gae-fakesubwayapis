from APIApp import APIApp

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os.path
import types

# base request class

class fakesubwayrequest (webapp.RequestHandler) :

    def __init__ (self) :
        webapp.RequestHandler.__init__(self)        

    # Hey look! This might be subclassed in a service-specific package!
    
    def generate_url (self, code, **more) :

        try :
            return self.url_template % code
        except :
            return "http://%s/%s/station/%s" % (self.request.host, self.service['id'], code)

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

        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')            
            return None

        out = {
            'code' : code,
            'service' : self.service['id'],
            'name' :  { '_content' : self.stations[code]['name'] },
            'url' : { '_content' : self.generate_url(code, **more) },
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

    def show_docs (self, **args) :

        stations = self.prepare_stations(**args)

        title = "%s (%s)" % (self.service['id'].upper(), self.service['name'])
        
        template = "%s.html" % self.service['id']
        
        template_vars = {
            'service' : self.service,
            'stations' : stations,
            'title' : title
            }
        
        self.display(template, template_vars)
        return

# base station page clas

class fakesubwaystation (fakesubwayrequest) :

    def show_station (self, code) :
        
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
        url = self.generate_url(code, **more)
        self.redirect(url)
