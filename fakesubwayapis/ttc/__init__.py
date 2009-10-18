import fakesubwayapis

class ttc :

    def __init__ (self) :

        # http://www.ttc.ca/Subway/index.jsp
        
        self.service = {
            'id' : 'ttc',
            'name' : 'Toronto Transit Commission',
            'url' : 'http://www3.ttc.ca/'
            }

        self.url_template = 'http://www3.ttc.ca/Subway/Stations/%s/station.jsp'
        
        self.lines = {
            'Y' : 'Yonge - University - Spadina',
            'B' : 'Bloor - Danforth',
            'SC' : 'Scarborough RT',
            'SH' : 'Sheppard',
            }
        
	self.stations = {
            'Bathurst' : { 'name' : 'Bathurst', 'line' : ('B',) },
            'Bay' : { 'name' : 'Bay', 'line' : ('B',) },            
            'Bayview' : { 'name' : 'Bayview', 'line' : ('SH',) },
            'Bessarion' : { 'name' : 'Bessarion', 'line' : ('SH',) },
            'Bloor-Yonge' : { 'name' : 'Bloor-Yonge', 'line' : ('Y', 'B') },
            'Broadview' : { 'name' : 'Broadview', 'line' : ('B',) },            
            'Castle_Frank' : { 'name' : 'Castle Frank', 'line' : ('B',) },
            'Chester' : { 'name' : 'Chester', 'line' : ('B',) },            
            'Christie' : { 'name' : 'Christie', 'line' : ('B',) },
            'College' : { 'name' : 'College', 'line' : ('Y',) },
            'Coxwell' : { 'name' : 'Coxwell', 'line' : ('B',) },            
            'Davisville' : { 'name' : 'Davisville', 'line' : ('Y',) },
            'Don_Mills' : { 'name' : 'Don Mills', 'line' : ('SH',) },
            'Donlands' : { 'name' : 'Donlands', 'line' : ('B',) },
            'Downsview' : { 'name' : 'Downsview', 'line' : ('Y',) },
            'Dufferin' : { 'name' : 'Dufferin', 'line' : ('B',) },
            'Dundas' : { 'name' : 'Dundas', 'line' : ('Y',) },
            'Dundas_West' : { 'name' : 'Dundas West', 'line' : ('B',) },            
            'Dupont' : { 'name' : 'Dupont', 'line' : ('Y',) },
            'Eglinton' : { 'name' : 'Eglinton', 'line' : ('Y',) },
            'Eglinton_West' : { 'name' : 'Eglinton West', 'line' : ('Y',) },            
            'Ellesmere' : { 'name' : 'Ellesmere', 'line' : ('SC',) },
            'Finch' : { 'name' : 'Finch', 'line' : ('Y',) },
            'Glencairn' : { 'name' : 'Glencairn', 'line' : ('Y',) },
            'Greenwood' : { 'name' : 'Greenwood', 'line' : ('B',) },
            'High_Park' : { 'name' : 'High Park', 'line' : ('B',) },
            'Islington' : { 'name' : 'Islington', 'line' : ('B',) },            
            'Jane' : { 'name' : 'Jane', 'line' : ('B',) },
            'Keele' : { 'name' : 'Keele', 'line' : ('B',) },
            'Kennedy' : { 'name' : 'Kennedy', 'line' : ('B', 'SC') },
            'King' : { 'name' : 'King', 'line' : ('Y',) },
            'Kipling' : { 'name' : 'Kipling', 'line' : ('B',) },
            'Lansdowne' : { 'name' : 'Lansdowne', 'line' : ('B',) },
            'Lawrence' : { 'name' : 'Lawrence', 'line' : ('Y',) },
            'Lawrence_East' : { 'name' : 'Lawrence East', 'line' : ('SC',) },
            'Lawrence_West' : { 'name' : 'Lawrence West', 'line' : ('Y',) },
            'Leslie' : { 'name' : 'Leslie', 'line' : ('SH',) },
            'Main_Street' : { 'name' : 'Main Street', 'line' : ('B',) },
            'McCowan' : { 'name' : 'McCowan', 'line' : ('SC',) },
            'Midland' : { 'name' : 'Midland', 'line' : ('SC',) },
            'Museum' : { 'name' : 'Museum', 'line' : ('Y',) },
            'North_York_Centre' : { 'name' : 'North York Centre', 'line' : ('Y',) },
            'Old_Mill' : { 'name' : 'Old Mill', 'line' : ('B',) },
            'Osgoode' : { 'name' : 'Osgoode', 'line' : ('Y',) },
            'Ossington' : { 'name' : 'Ossington', 'line' : ('B',) },
            'Pape' : { 'name' : 'Pape', 'line' : ('B',) },            
            'Queen' : { 'name' : 'Queen', 'line' : ('Y',) },
            'Queens_Park' : { 'name' : 'Queen\'s Park', 'line' : ('Y',) },            
            'Rosedale' : { 'name' : 'Rosedale', 'line' : ('Y',) },
            'Royal_York' : { 'name' : 'Royal York', 'line' : ('B',) },
            'Runnymede' : { 'name' : 'Runnymede', 'line' : ('B',) },
            'Scarborough_Centre' : { 'name' : 'Scarborough Centre', 'line' : ('SC',) },
            'Sheppard-Yonge' : { 'name' : 'Sheppard-Yonge', 'line' : ('Y', 'SH') },
            'Sherbourne' : { 'name' : 'Sherbourne', 'line' : ('B',) },
            'Spadina' : { 'name' : 'Spadina', 'line' : ('B',) },            
            'St_Andrew' : { 'name' : 'St Andrew', 'line' : ('Y',) },
            'St_Clair' : { 'name' : 'St Clair', 'line' : ('Y',) },
            'St_Clair_West' : { 'name' : 'St Clair West', 'line' : ('Y',) },            
            'St_George' : { 'name' : 'St George', 'line' : ('Y', 'B') },
            'St_Patrick' : { 'name' : 'St Patrick', 'line' : ('Y',) },
            'Summerhill' : { 'name' : 'Summerhill', 'line' : ('Y',) },
            'Union' : { 'name' : 'Union', 'line' : ('Y',) },
            'Victoria_Park' : { 'name' : 'Victoria Park', 'line' : ('B',) },
            'Warden' : { 'name' : 'Warden', 'line' : ('B',) },
            'Wellesley' : { 'name' : 'Wellesley', 'line' : ('Y',) },
            'Wilson' : { 'name' : 'Wilson', 'line' : ('Y',) },
            'Woodbine' : { 'name' : 'Woodbine', 'line' : ('B',) },
            'York_Mills' : { 'name' : 'York Mills', 'line' : ('Y',) },
            'Yorkdale' : { 'name' : 'Yorkdale', 'line' : ('Y',) },


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

        code = code.title()
        
        self.do_redirect(code)
        return
    
class api (ttc, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        ttc.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)

class getinfo (api) :

    def get (self, code) :

        code = code.title()
        
        self.generate_info(code)
        return
