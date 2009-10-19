import fakesubwayapis

class wmata :

    def __init__ (self) :
        
        self.service = {
            'id' : 'wmata',
            'name' : 'Washington Metropolitain Area Transit Authority',
            'url' : 'http://www.wmata.com/'
            }

        self.url_template = 'http://www.wmata.com/rail/station_detail.cfm?station_id=%s'
        
        self.lines = {
            'R' : 'red',
            'O' : 'orange',
            'G' : 'green',
            'B' : 'blue',
            'Y' : 'yellow',
            }

	# http://www.wmata.com/rail/stations.cfm
        
	self.stations = {
            92 : { 'name' : 'Addison Road-Seat Pleasant', 'line' : ('B',) },
	}

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

        code = int(code)
        
        self.do_redirect(code)
        return
    
class api (wmata, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        wmata.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)

class getinfo (api) :

    def get (self, code) :

        code = int(code)
        
        self.generate_info(code)
        return
