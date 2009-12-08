import fakesubwayapis

class boilerplate (fakesubwayapis.fakesubwayservice) :

    def __init__ (self) :
        pass
    
    def initialize_service_id (self, service_id) :

        fakesubwayapis.fakesubwayservice.__init__(self, service_id)        
    
class docs (boilerplate, fakesubwayapis.fakesubwayapidocs) :

    def initialize_service_id (self, service_id) :
        boilerplate.initialize_service_id(self, service_id)        
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        
    def get (self, service_id) :

        self.initialize_service_id(service_id)
        self.show_docs()
        return
        
class station (boilerplate, fakesubwayapis.fakesubwaystation) :

    def initialize_service_id (self, service_id) :
        boilerplate.initialize_service_id(self, service_id)
        fakesubwayapis.fakesubwaystation.__init__(self)

    def get (self, service_id, code) :

        self.initialize_service_id(service_id)

        if self.service['url_template'] != '' :
            self.do_redirect(code)
            return
        
        self.show_station(code)
        return
    
class api (boilerplate, fakesubwayapis.fakesubwayapi) :

    def initialize_service_id (self, service_id) :
        boilerplate.initialize_service_id(self, service_id)
        fakesubwayapis.fakesubwayapi.__init__(self)

class getinfo (api) :

    def get (self, service_id, code) :

        self.initialize_service_id(service_id)
        self.generate_info(code)
        return
