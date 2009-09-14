import fakesubwayapis

class docs (fakesubwayapis.fakesubwayapidocs) :

    def get (self) :
        self.display("bart.html")
        return
    
class api (fakesubwayapis.fakesubwayapi) :

    def __init__ (self)  :

        fakesubwayapis.fakesubwayapi.__init__(self)
        
        self.stations = {
            
            "12th" : "12th St. Oakland City Center",
            "16th" : "16th St. Mission (SF)",
            "19th" : "19th St. Oakland",
            "24th" : "24th St. Mission (SF)",
            "ashb" : "Ashby (Berkeley)",
            "balb" : "Balboa Park (SF)",
            "bayf" : "Bay Fair (San Leandro)",
            "cast" : "Castro Valley",
            "civc" : "Civic Center (SF)",
            "cols" : "Coliseum/Oakland Airport",
            "colm" : "Colma",
            "conc" : "Concord",
            "daly" : "Daly City",
            "dbrk" : "Downtown Berkeley",
            "dubl" : "Dublin/Pleasanton",
            "deln" : "El Cerrito del Norte",
            "plza" : "El Cerrito Plaza",
            "embr" : "Embarcadero (SF)",
            "frmt" : "Fremont",
            "ftvl" : "Fruitvale (Oakland)",
            "glen" : "Glen Park (SF)",
            "hayw" : "Hayward",
            "lafy" : "Lafayette",
            "lake" : "Lake Merritt (Oakland)",
            "mcar" : "MacArthur (Oakland)",
            "mlbr" : "Millbrae",
            "mont" : "Montgomery St. (SF)",
            "nbrk" : "North Berkeley",
            "ncon" : "North Concord/Martinez",
            "orin" : "Orinda",
            "pitt" : "Pittsburg/Bay Point",
            "phil" : "Pleasant Hill",
            "powl" : "Powell St. (SF)",
            "rich" : "Richmond",
            "rock" : "Rockridge (Oakland)",
            "sbrn" : "San Bruno",
            "sfia" : "San Francisco Int'l Airport",
            "sanl" : "San Leandro",
            "shay" : "South Hayward",
            "ssan" : "South San Francisco",
            "ucty" : "Union City",
            "wcrk" : "Walnut Creek",
            "woak" : "West Oakland",
            }
    
class getinfo (api) :

    def get (self, code) :

        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')
            return

        out = {
            'code' : code,
            'service' : 'bart',
            'name' :  { '_content' : self.stations[code] },
            'url' : { '_content' : 'http://www.bart.gov/stations/%s/' % code },
            }
        
        self.api_ok({'station' : out})
        return
