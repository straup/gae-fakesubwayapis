import fakesubwayapis

class wmata (fakesubwayapis.fakesubwayservice) :

    def __init__ (self) :

        fakesubwayapis.fakesubwayservice.__init__(self, 'wmata')
        
    def prepare_station_code (self, code) :

        return int(code)
                        
class docs (wmata, fakesubwayapis.fakesubwayapidocs) :

    def __init__ (self) :

        wmata.__init__(self)        
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        
    def get (self) :

        self.show_docs()
        return
        
class station (wmata, fakesubwayapis.fakesubwaystation) :

    def __init__ (self) :

        wmata.__init__(self)
        fakesubwayapis.fakesubwaystation.__init__(self)

    def get (self, code) :

        self.show_station(code)
        return
    
class api (wmata, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        wmata.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)

class getinfo (api) :

    def get (self, code) :

        self.generate_info(code)
        return
