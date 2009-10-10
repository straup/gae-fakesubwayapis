import fakesubwayapis

class bart :

    def __init__ (self) :

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
        
class docs (fakesubwayapis.fakesubwayapidocs, bart) :

    def __init__ (self)  :

        fakesubwayapis.fakesubwayapidocs.__init__(self)        
        bart.__init__(self)

    def get (self) :

        stations = self.prepare_stations()
        
        self.display("bart.html", {'title' : 'bart', 'stations' : stations})
        return
    
class api (fakesubwayapis.fakesubwayapi, bart) :

    def __init__ (self)  :

        fakesubwayapis.fakesubwayapi.__init__(self)        
        bart.__init__(self)
        
class getinfo (api) :

    def get (self, code) :

        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')
            return

        out = {
            'code' : code,
            'service' : 'bart',
            'name' :  { '_content' : self.stations[code]['name'] },
            'url' : { '_content' : 'http://www.bart.gov/stations/%s/' % code },
            }
        
        self.api_ok({'station' : out})
        return
