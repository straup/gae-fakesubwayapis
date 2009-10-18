import fakesubwayapis

class ttc :

    def __init__ (self) :

        # http://www.ttc.ca/Subway/index.jsp
        
        self.service = {
            'id' : 'ttc',
            'name' : 'Toronto Transit Commission',
            'url' : 'http://www.ttc.ca/'
            }

        self.url_template = 'http://www.ttc.ca/Subway/Stations/%s/station.jsp'
        
        self.lines = {
            'Y' : 'Yonge - University - Spadina',
            'B' : 'Bloor -Danforth',
            }
        
	self.stations = {
            'Bloor-Yonge' : { 'name' : 'Bloor-Yonge', 'line' : ('Y',) },
            'College' : { 'name' : 'College', 'line' : ('Y',) },            
            'Davisville' : { 'name' : 'Davisville', 'line' : ('Y',) },
            'Downsview' : { 'name' : 'Downsview', 'line' : ('Y',) },
            'Dundas' : { 'name' : 'Dundas', 'line' : ('Y',) },
            'Dupont' : { 'name' : 'Dupont', 'line' : ('Y',) },
            'Eglinton' : { 'name' : 'Eglinton', 'line' : ('Y',) },
            'Eglington_West' : { 'name' : 'Eglington West', 'line' : ('Y',) },            
            'Finch' : { 'name' : 'Finch', 'line' : ('Y',) },
            'Glencairn' : { 'name' : 'Glencairn', 'line' : ('Y',) },            
            'King' : { 'name' : 'King', 'line' : ('Y',) },
            'Lawrence' : { 'name' : 'Lawrence', 'line' : ('Y',) },
            'Lawrence_West' : { 'name' : 'Lawrence West', 'line' : ('Y',) },
            'Museum' : { 'name' : 'Museum', 'line' : ('Y',) },
            'North_York_Center' : { 'name' : 'North York Center', 'line' : ('Y',) },
            'Osgoode' : { 'name' : 'Osgoode', 'line' : ('Y',) },
            'Queen' : { 'name' : 'Queen', 'line' : ('Y',) },
            'Queens_Park' : { 'name' : 'Queen\'s Park', 'line' : ('Y',) },            
            'Rosedale' : { 'name' : 'Rosedale', 'line' : ('Y',) },
            'Sheppard-Yonge' : { 'name' : 'Sheppard-Yonge', 'line' : ('Y',) },
            'St_Andrew' : { 'name' : 'St Andrew', 'line' : ('Y',) },
            'St_Clair' : { 'name' : 'St Clair', 'line' : ('Y',) },
            'St_Clair_West' : { 'name' : 'St Clair West', 'line' : ('Y',) },            
            'St_George' : { 'name' : 'St George', 'line' : ('Y',) },
            'St_Patrick' : { 'name' : 'St Patrick', 'line' : ('Y',) },
            'Summerhill' : { 'name' : 'Summerhill', 'line' : ('Y',) },
            'Union' : { 'name' : 'Union', 'line' : ('Y',) },
            'Wellesley' : { 'name' : 'Wellesley', 'line' : ('Y',) },
            'Wilson' : { 'name' : 'Wilson', 'line' : ('Y',) },
            'York_Mills' : { 'name' : 'York Mills', 'line' : ('Y',) },
            'Yorkdale' : { 'name' : 'Yorkdale', 'line' : ('Y',) },

            '' : { 'name' : '', 'line' : ('',) },
            '' : { 'name' : '', 'line' : ('',) },
            '' : { 'name' : '', 'line' : ('',) },
            '' : { 'name' : '', 'line' : ('',) },
            '' : { 'name' : '', 'line' : ('',) },
            
	}

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

        self.do_redirect(code)
        return
    
class api (ttc, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        ttc.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)

class getinfo (api) :

    def get (self, code) :

        code = int(code)

        self.generate_info(code)
        return
