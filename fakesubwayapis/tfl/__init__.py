import fakesubwayapis

class tfl (fakesubwayapis.fakesubwayservice) :

    def __init__ (self) :

        fakesubwayapis.fakesubwayservice.__init__(self, 'tfl')

    def generate_station_url (self, code, **more) :
        
        if not more.has_key('line_code') :
            return fakesubwayapis.fakesubwayservice.generate_station_url(self, code)

        if not self.stations[code].has_key('line') :        
            return fakesubwayapis.fakesubwayservice.generate_station_url(self, code)

        if not more['line_code'] in self.lines :
            return fakesubwayapis.fakesubwayservice.generate_station_url(self, code)

        line_name = self.lines[ more['line_code'] ]

        return "http://www.tfl.gov.uk/tfl/livetravelnews/departureboards/tube/default.asp?LineCode=%s&StationCode=%s" % (line_name, code.upper())
                        
class docs (tfl, fakesubwayapis.fakesubwayapidocs) :

    def __init__ (self) :

        tfl.__init__(self)        
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        
    def get (self) :

        self.show_docs(generate_compound_ids=True)
        return
        
class station (tfl, fakesubwayapis.fakesubwaystation) :

    def __init__ (self) :

        tfl.__init__(self)
        fakesubwayapis.fakesubwaystation.__init__(self)

    def get (self, station_code, line_code) :

        if line_code :
            self.do_redirect(station_code, line_code=line_code)
            return

        self.show_station(station_code)
        return
    
class api (tfl, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        tfl.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)

class getinfo (api) :

    def get (self, station_code, line_code) :

        self.generate_info(station_code, line_code=line_code)
        return
