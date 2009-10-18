import fakesubwayapis

class bart :

    def __init__ (self) :

        self.service = {
            'id' : 'bart',
            'name' : 'Bay Area Rapid Transit',
            'url' : 'http://www.bart.gov/'
            }
        
        self.url_template = 'http://www.bart.gov/stations/%s/'
        
        self.stations = {
            
            "12th" : { "name" : "12th St. Oakland City Center" },
            "16th" : { "name" : "16th St. Mission (SF)" },
            "19th" : { "name" : "19th St. Oakland" },
            "24th" : { "name" : "24th St. Mission (SF)" },
            "ashb" : { "name" : "Ashby (Berkeley)" },
            "balb" : { "name" : "Balboa Park (SF)" },
            "bayf" : { "name" : "Bay Fair (San Leandro)" },
            "cast" : { "name" : "Castro Valley" },
            "civc" : { "name" : "Civic Center (SF)" },
            "cols" : { "name" : "Coliseum/Oakland Airport" },
            "colm" : { "name" : "Colma" },
            "conc" : { "name" : "Concord" },
            "daly" : { "name" : "Daly City" },
            "dbrk" : { "name" : "Downtown Berkeley" },
            "dubl" : { "name" : "Dublin/Pleasanton" },
            "deln" : { "name" : "El Cerrito del Norte" },
            "plza" : { "name" : "El Cerrito Plaza" },
            "embr" : { "name" : "Embarcadero (SF)" },
            "frmt" : { "name" : "Fremont" },
            "ftvl" : { "name" : "Fruitvale (Oakland)" },
            "glen" : { "name" : "Glen Park (SF)" },
            "hayw" : { "name" : "Hayward" },
            "lafy" : { "name" : "Lafayette" },
            "lake" : { "name" : "Lake Merritt (Oakland)" },
            "mcar" : { "name" : "MacArthur (Oakland)" },
            "mlbr" : { "name" : "Millbrae" },
            "mont" : { "name" : "Montgomery St. (SF)" },
            "nbrk" : { "name" : "North Berkeley" },
            "ncon" : { "name" : "North Concord/Martinez" },
            "orin" : { "name" : "Orinda" },
            "pitt" : { "name" : "Pittsburg/Bay Point" },
            "phil" : { "name" : "Pleasant Hill" },
            "powl" : { "name" : "Powell St. (SF)" },
            "rich" : { "name" : "Richmond" },
            "rock" : { "name" : "Rockridge (Oakland)" },
            "sbrn" : { "name" : "San Bruno" },
            "sfia" : { "name" : "San Francisco Int'l Airport" },
            "sanl" : { "name" : "San Leandro" },
            "shay" : { "name" : "South Hayward" },
            "ssan" : { "name" : "South San Francisco" },
            "ucty" : { "name" : "Union City" },
            "wcrk" : { "name" : "Walnut Creek" },
            "woak" : { "name" : "West Oakland" },
            }
        
class docs (bart, fakesubwayapis.fakesubwayapidocs) :

    def __init__ (self)  :

        bart.__init__(self)
        fakesubwayapis.fakesubwayapidocs.__init__(self)        

    def get (self) :

        self.show_docs()
        return

class station (bart, fakesubwayapis.fakesubwaystation) :

    def __init__ (self) :

        bart.__init__(self)
        fakesubwayapis.fakesubwaystation.__init__(self)

    def get (self, code) :

        self.do_redirect(code)
        return
    
class api (bart, fakesubwayapis.fakesubwayapi) :

    def __init__ (self)  :

        bart.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)        
        
class getinfo (api) :

    def get (self, code) :

        self.generate_info(code)
        return
