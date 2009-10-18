import fakesubwayapis

class mbta :

    def __init__ (self) :

        self.lines = {
            'R' : 'RED',
            'O' : 'ORANGE',
            
            },
        
	self.stations = {

            # red line
            
            10029 : { 'name' : 'Alewife', 'lat' : 42.395261, 'lon' : -71.142449, 'line' : ('R',) },
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11404&lat=42.39662&lng=-71.122527 Davis
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13912&lat=42.388353&lng=-71.119159 Porter Square
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=12084&lat=42.373936&lng=-71.118917 Harvard Square
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10919&lat=42.365326&lng=-71.103474 Central Square
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=12412&lat=42.362427&lng=-71.086058 Kendall Station
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11048&lat=42.361279&lng=-71.070493 Charles/MGH
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13771&lat=42.356332&lng=-71.062202 Park Street
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11473&lat=42.355453&lng=-71.060465 Downtown Crossing
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14435&lat=42.352573&lng=-71.055428 South Station
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10641&lat=42.342793&lng=-71.057117 Broadway
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10062&lat=42.329752&lng=-71.056979 Andrew
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=12410&lat=42.321065&lng=-71.052545 JFK/UMass
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13524&lat=42.274957&lng=-71.029307 North Quincy
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15412&lat=42.265972&lng=-71.019721 Wollaston
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13981&lat=42.250879&lng=-71.004798 Quincy Street
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13946&lat=42.232848&lng=-71.007034 Quincy Adams
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10431&lat=42.20855&lng=-71.00085 Braintree
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14289&lat=42.311099&lng=-71.053175 Savin Hill
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11781&lat=42.299992&lng=-71.061516 Fields Corner
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14352&lat=42.293712&lng=-71.065912 Shawmut
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15481&lat=42.284219&lng=-71.063229 Ashmont
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15659&lat=42.279712&lng=-71.060327 Cedar Grove
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15660&lat=42.272253&lng=-71.062453 Butler
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15692&lat=42.270093&lng=-71.067612 Milton
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15664&lat=42.269965&lng=-71.073249 Central Avenue
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15665&lat=42.267772&lng=-71.083025 Valley ROad
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15667&lat=42.267622&lng=-71.087436 Capen Street
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15668&lat=42.267586&lng=-71.092021 Mattapan

            # orange line

            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13642&lat=42.436381&lng=-71.071007 Oak Grove
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=12975&lat=42.426678&lng=-71.074144 Malden Center
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15231&lat=42.405202&lng=-71.076969 Wellington
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14490&lat=42.383434&lng=-71.077056 Sullivan Square
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11258&lat=42.372593&lng=-71.07052 Community College
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13610&lat=42.365551&lng=-71.061251 North Station
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=12091&lat=42.363222&lng=-71.057922 Haymarket
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14471&lat=42.359065&lng=-71.057421 State
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11471&lat=42.355453&lng=-71.060465 Downtown Crossing
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11108&lat=42.352529&lng=-71.062759 Chinatown
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13443&lat=42.349504&lng=-71.063877 Tufts Medical Center
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10124&lat=42.347314&lng=-71.075724 Back Bay
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13073&lat=42.341762&lng=-71.083072 Massachusetts Avenue
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14166&lat=42.335742&lng=-71.090437 Ruggles
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14153&lat=42.331388&lng=-71.095555 Roxbury Crossing
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=12395&lat=42.322893&lng=-71.099787 Jackson Square
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14477&lat=42.317251&lng=-71.104021 Stony Brook
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11952&lat=42.310359&lng=-71.107125 Green Street
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11788&lat=42.300023&lng=-71.113377 Forest Hills

            # green line

            # blue line

            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15415&lat=42.413963&lng=-70.990986 Wonderland
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=11913&lat=42.408389&lng=-70.99256 Revere Beach
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14474&lat=42.39745&lng=-70.992363 Beachmont
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10077&lat=42.390232&lng=-70.997678 Suffolk Downs
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13119&lat=42.386769&lng=-71.004941 Orient Heights
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10018&lat=42.379759&lng=-71.022476 Wood Island
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=15417&lat=42.372714&lng=-71.03208 Airport
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=13699&lat=42.368343&lng=-71.038422 Maverick
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14486&lat=42.359634&lng=-71.051807 Aquarium
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10180&lat=42.359065&lng=-71.057421 State
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14037&lat=42.359322&lng=-71.059252 Government Center
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=10409&lat=42.361457&lng=-71.062129 Bowdoin

            # silver

            # sl1

            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=14435&lat=42.352573&lng=-71.055428 South Station
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=25133&lat=42.352724&lng=-71.047514 Courthouse
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=25092&lat=42.349098&lng=-71.04206 World Trade Center
            # http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=25100&lat=42.347928&lng=-71.039287 Silver Line Way
            
	}

class docs (fakesubwayapis.fakesubwayapidocs, mbta) :

    def __init__ (self) :
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        mbta.__init__(self)
        
    def get (self) :

        stations = self.prepare_stations()
        
        self.display("mbta.html", {'title' : 'mbta', 'stations' : stations})
        return

class api (fakesubwayapis.fakesubwayapi, mbta) :

    def __init__ (self) :

        fakesubwayapis.fakesubwayapi.__init__(self)
        mbta.__init__(self)

class getinfo (api) :

    def get (self, code) :

        code = int(code)
        
        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')
            return

        out = {
            'code' : code,
            'service' : 'mbta',
            'location' : { 'lat' : self.stations[code]['lat'], 'lon' : self.stations[code]['lon'] },            
            'name' :  { '_content' : self.stations[code]['name'] },
            'url' : { '_content' : 'http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=' % code },
            }
        
        self.api_ok({'station' : out})
        return
