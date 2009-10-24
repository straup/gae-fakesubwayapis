import fakesubwayapis

class ttc (fakesubwayapis.fakesubwayservice) :

    def __init__ (self) :

        fakesubwayapis.fakesubwayservice.__init__(self, 'ttc')

    # It's kind of insane that we need all this boiler
    # plate for the following method but, today anyway,
    # that's what's necessary...
    
    def generate_station_url (self, code) :

        code = code.title()
        
        try :
            return self.service['url_template'] % code
        except :
            return "http://%s/%s/station/%s" % (self.request.host, self.service['id'], code)
                        
class docs (ttc, fakesubwayapis.fakesubwayapidocs) :

    def __init__ (self) :

        ttc.__init__(self)        
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        
    def get (self) :

        self.show_docs()
        return
        
class station (ttc, fakesubwayapis.fakesubwaystation) :

    def __init__ (self) :

        ttc.__init__(self)
        fakesubwayapis.fakesubwaystation.__init__(self)

    def get (self, code) :

        self.show_station(code)
        return
    
class api (ttc, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        ttc.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)

class getinfo (api) :

    def get (self, code) :

        self.generate_info(code)
        return
