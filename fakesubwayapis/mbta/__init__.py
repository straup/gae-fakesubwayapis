import fakesubwayapis

class mbta :

    def __init__ (self) :

        self.lines = {
            'R' : 'RED',
            'O' : 'ORANGE',
            'G' : 'GREEN',
            'B' : 'BLUE',
            'S' : 'SILVER',
            },
        
	self.stations = {

            613 : { 'name' : 'East Berkeley Street', 'lat' : 42.343845, 'lon' : -71.066041, 'line' : ('S',) },

            4057 : { 'name' : 'Massachusetts Avenue', 'lat' : 42.336378, 'lon' : -71.077232, 'line' : ('S',) },
            
            6537 : { 'name' : 'Chinatown', 'lat' : 42.352529, 'lon' : -71.062759, 'line' : ('S4',) },
            6565 : { 'name' : 'Tufts Medical Center', 'lat' : 42.350019, 'lon' : -71.06357, 'line' : ('S',) },            
            6962 : { 'name' : 'Northern Avenue & Harbor Street', 'lat' : 42.346621, 'lon' : -71.035215, 'line' : ('S',) },

            8190 : { 'name' : '25 Dry Dock Avenue', 'lat' : 42.344681, 'lon' : -71.028456, 'line' : ('S',) },

            9108 : { 'name' : 'Worcester Street', 'lat' : 42.337386, 'lon' : -71.075846, 'line' : ('S',) },
            9154 : { 'name' : 'Lenox Street', 'lat' : 42.334958, 'lon' : -71.078958, 'line' : ('S',) },
            
            10018 : { 'name' : 'Wood Island', 'lat' : 42.379759, 'lon' : -71.022476, 'line' : ('B',) },            
            10029 : { 'name' : 'Alewife', 'lat' : 42.395261, 'lon' : -71.142449, 'line' : ('R',) },
            10062 : { 'name' : 'Andrew', 'lat' : 42.329752, 'lon' : -71.056979, 'line' : ('R',) },
            10077 : { 'name' : 'Suffolk Downs', 'lat' : 42.390232, 'lon' : -70.997678, 'line' : ('B',) },
            10124 : { 'name' : 'Back Bay', 'lat' : 42.347314, 'lon' : -71.075724, 'line' : ('O',) },
            10180 : { 'name' : 'State', 'lat' : 42.359065, 'lon' : -71.057421, 'line' : ('B',) },
            10369 : { 'name' : 'Boston College', 'lat' : 42.339902, 'lon' : -71.166124, 'line' : ('G',) },
            10409 : { 'name' : 'Bowdoin', 'lat' : 42.361457, 'lon' : -71.062129, 'line' : ('B',) },
            10431 : { 'name' : 'Braintree', 'lat' : 42.20855, 'lon' : -71.00085, 'line' : ('R',) },
            10641 : { 'name' : 'Broadway', 'lat' : 42.342793, 'lon' : -71.057117, 'line' : ('R',) },
            10690 : { 'name' : 'Boston University Central Station', 'lat' : 42.34989, 'lon' : -71.106804, 'line' : ('G',) },            
            10693 : { 'name' : 'Boston University East Station', 'lat' : 42.349569, 'lon' : -71.103866, 'line' : ('G',) },
            10694 : { 'name' : 'Boston University West Station', 'lat' : 42.350759, 'lon' : -71.113833, 'line' : ('G',) },            
            10919 : { 'name' : 'Central Square', 'lat' : 42.365326, 'lon' : -71.103474, 'line' : ('R',) },

            11048 : { 'name' : 'Charles/MGH', 'lat' : 42.361279, 'lon' : -71.070493, 'line' : ('R',) },            
            11108 : { 'name' : 'Chinatown', 'lat' : 42.352529, 'lon' : -71.062759, 'line' : ('O',) },
            11178 : { 'name' : 'Allston Street', 'lat' : 42.348468, 'lon' : -71.137888, 'line' : ('G',) },
            11180 : { 'name' : 'Babcock Street', 'lat' : 42.35169, 'lon' : -71.121547, 'line' : ('G',) },
            11182 : { 'name' : 'Blandford Street', 'lat' : 42.349126, 'lon' : -71.100235, 'line' : ('G',) },            
            11185 : { 'name' : 'Packards Corner', 'lat' : 42.351833, 'lon' : -71.124702, 'line' : ('G',) },
            11187 : { 'name' : 'Chestnut Hill Avenue', 'lat' : 42.338145, 'lon' : -71.152961, 'line' : ('G',) },            
            11189 : { 'name' : 'Sutherland Street', 'lat' : 42.341483, 'lon' : -71.146162, 'line' : ('G',) },            
            11194 : { 'name' : 'Harvard Avenue', 'lat' : 42.350118, 'lon' : -71.131197, 'line' : ('G',) },
            11197 : { 'name' : 'Griggs Street/Long Avenue', 'lat' : 42.348542, 'lon' : -71.134551, 'line' : ('G',) },
            11201 : { 'name' : 'Pleasant Street', 'lat' : 42.351345, 'lon' : -71.118783, 'line' : ('G',) },
            11202 : { 'name' : 'South Street', 'lat' : 42.339455, 'lon' : -71.157622, 'line' : ('G',) },
            11203 : { 'name' : 'St. Paul Street', 'lat' : 42.350997, 'lon' : -71.115997, 'line' : ('G',) },
            11207 : { 'name' : 'Chiswick Road', 'lat' : 42.340839, 'lon' : -71.150459, 'line' : ('G',) },
            11210 : { 'name' : 'Warren Street', 'lat' : 42.348366, 'lon' : -71.140224, 'line' : ('G',) },
            11212 : { 'name' : 'Washington Street', 'lat' : 42.343886, 'lon' : -71.142593, 'line' : ('G',) },
            11258 : { 'name' : 'Community College', 'lat' : 42.372593, 'lon' : -71.07052, 'line' : ('O',) },
            11404 : { 'name' : 'Davis', 'lat' : 42.39662, 'lon' : -71.122527, 'line' : ('R',) },
            11471 : { 'name' : 'Downtown Crossing', 'lat' : 42.355453, 'lon' : -71.060465, 'line' : ('O',) },
            11473 : { 'name' : 'Downtown Crossing', 'lat' : 42.355453, 'lon' : -71.060465, 'line' : ('R',) },
            11475 : { 'name' : '21 Dry Dock Avenue', 'lat' : 42.344626, 'lon' : -71.031036, 'line' : ('S',) },            
            11496 : { 'name' : 'Dudley Square', 'lat' : 42.329379, 'lon' : -71.084266, 'line' : ('S',) },
            11781 : { 'name' : 'Fields Corner', 'lat' : 42.299992, 'lon' : -71.061516, 'line' : ('R',) },
            11788 : { 'name' : 'Forest Hills', 'lat' : 42.300023, 'lon' : -71.113377, 'line' : ('O',) },
            11913 : { 'name' : 'Revere Beach', 'lat' : 42.408389, 'lon' : -70.99256, 'line' : ('B',) },
            11952 : { 'name' : 'Green Street', 'lat' : 42.310359, 'lon' : -71.107125, 'line' : ('O',) },
            
            12084 : { 'name' : 'Harvard Square', 'lat' : 42.373936, 'lon' : -71.118917, 'line' : ('R',) },
            12091 : { 'name' : 'Haymarket', 'lat' : 42.363222, 'lon' : -71.057922, 'line' : ('O',) },
            12395 : { 'name' : 'Jackson Square', 'lat' : 42.322893, 'lon' : -71.099787, 'line' : ('O',) },
            12410 : { 'name' : 'JFK/UMass', 'lat' : 42.321065, 'lon' : -71.052545, 'line' : ('R',) },
            12412 : { 'name' : 'Kendall', 'lat' : 42.362427, 'lon' : -71.086058, 'line' : ('R',) },            
            12975 : { 'name' : 'Malden Center', 'lat' : 42.426678, 'lon' : -71.074144, 'line' : ('O',) },

            13073 : { 'name' : 'Massachusetts Avenue', 'lat' : 42.341762, 'lon' : -71.083072, 'line' : ('O',) },
            13119 : { 'name' : 'Orient Heights', 'lat' : 42.386769, 'lon' : -71.004941, 'line' : ('B',) },
            13443 : { 'name' : 'Tufts Medical Center', 'lat' : 42.349504, 'lon' : -71.063877, 'line' : ('O',) },            
            13524 : { 'name' : 'North Quincy', 'lat' : 42.274957, 'lon' : -71.029307, 'line' : ('R',) },
            13610 : { 'name' : 'North Station', 'lat' : 42.365551, 'lon' : -71.061251, 'line' : ('O',) },            
            13614 : { 'name' : 'Northern Avenue & Tide Street', 'lat' : 42.345051, 'lon' : -71.031956, 'line' : ('S',) },
            13642 : { 'name' : 'Oak Grove', 'lat' : 42.436381, 'lon' : -71.071007, 'line' : ('O',) },
            13699 : { 'name' : 'Maverick', 'lat' : 42.368343, 'lon' : -71.038422, 'line' : ('B',) },
            13771 : { 'name' : 'Park', 'lat' : 42.356332, 'lon' : -71.062202, 'line' : ('R',) },            
            13912 : { 'name' : 'Porter Square', 'lat' : 42.388353, 'lon' : -71.119159, 'line' : ('R',) },
            13946 : { 'name' : 'Quincy Adams', 'lat' : 42.232848, 'lon' : -71.007034, 'line' : ('R',) },
            13981 : { 'name' : 'Quincy Street', 'lat' : 42.250879, 'lon' : -71.004798, 'line' : ('R',) },

            14037 : { 'name' : 'Government Center', 'lat' : 42.359322, 'lon' : -71.059252, 'line' : ('B',) },
            14153 : { 'name' : 'Roxbury Crossing', 'lat' : 42.331388, 'lon' : -71.095555, 'line' : ('O',) },
            14166 : { 'name' : 'Ruggles', 'lat' : 42.335742, 'lon' : -71.090437, 'line' : ('O',) },
            14289 : { 'name' : 'Savin Hill', 'lat' : 42.311099, 'lon' : -71.053175, 'line' : ('R',) },
            14352 : { 'name' : 'Shawmut', 'lat' : 42.293712, 'lon' : -71.065912, 'line' : ('R',) },
            14435 : { 'name' : 'South', 'lat' : 42.352573, 'lon' : -71.055428, 'line' : ('R',) },
            # 14435 : { 'name' : 'South Station', 'lat' : 42.352573, 'lon' : -71.055428, 'line' : ('S',) }, ***
            # 14435 : { 'name' : 'South Station', 'lat' : 42.352573, 'lon' : -71.055428, 'line' : ('S',) }, ***
            14436 : { 'name' : 'South Station', 'lat' : 42.352573, 'lon' : -71.055428, 'line' : ('S4',) },
            14471 : { 'name' : 'State', 'lat' : 42.359065, 'lon' : -71.057421, 'line' : ('O',) },
            14474 : { 'name' : 'Beachmont', 'lat' : 42.39745, 'lon' : -70.992363, 'line' : ('B',) },
            14477 : { 'name' : 'Stony Brook', 'lat' : 42.317251, 'lon' : -71.104021, 'line' : ('O',) },
            14486 : { 'name' : 'Aquarium', 'lat' : 42.359634, 'lon' : -71.051807, 'line' : ('B',) },            
            14490 : { 'name' : 'Sullivan Square', 'lat' : 42.383434, 'lon' : -71.077056, 'line' : ('O',) },
            14942 : { 'name' : 'Herald Street', 'lat' : 42.346443, 'lon' : -71.064651, 'line' : ('S',) },

            15009 : { 'name' : 'Union Park Street', 'lat' : 42.34136, 'lon' : -71.06955, 'line' : ('S',) },
            15011 : { 'name' : 'Newton Street', 'lat' : 42.338754, 'lon' : -71.073783, 'line' : ('S',) },            
            15231 : { 'name' : 'Wellington', 'lat' : 42.405202, 'lon' : -71.076969, 'line' : ('O',) },
            15412 : { 'name' : 'Wollaston', 'lat' : 42.265972, 'lon' : -71.019721, 'line' : ('R',) },
            15415 : { 'name' : 'Wonderland', 'lat' : 42.413963, 'lon' : -70.990986, 'line' : ('B',) },
            15417 : { 'name' : 'Airport', 'lat' : 42.372714, 'lon' : -71.03208, 'line' : ('B',) },            
            15481 : { 'name' : 'Ashmont', 'lat' : 42.284219, 'lon' : -71.063229, 'line' : ('R',) },
            15580 : { 'name' : 'Government ', 'lat' : 42.359322, 'lon' : -71.059252, 'line' : ('G',) },
            # 15580 : { 'name' : 'Government Center', 'lat' : 42.359322, 'lon' : -71.059252, 'line' : ('G',) },  ***
            # 15580 : { 'name' : 'Government Center', 'lat' : 42.359322, 'lon' : -71.059252, 'line' : ('G',) },  ***
            15582 : { 'name' : 'Haymarket', 'lat' : 42.363222, 'lon' : -71.057922, 'line' : ('G',) },
            15583 : { 'name' : 'North', 'lat' : 42.365551, 'lon' : -71.061251, 'line' : ('G',) },
            # 15583 : { 'name' : 'North', 'lat' : 42.365551, 'lon' : -71.061251, 'line' : ('G',) }, ***
            15585 : { 'name' : 'Science Park', 'lat' : 42.368009, 'lon' : -71.070673, 'line' : ('G',) },
            15591 : { 'name' : 'Kenmore', 'lat' : 42.348783, 'lon' : -71.095128, 'line' : ('G',) },
            # 15591 : { 'name' : 'Kenmore', 'lat' : 42.348783, 'lon' : -71.095128, 'line' : ('G',) }, ***
            # 15591 : { 'name' : 'Kenmore', 'lat' : 42.348783, 'lon' : -71.095128, 'line' : ('G',) }, ***
            # 15591 : { 'name' : 'Kenmore Station', 'lat' : 42.348783, 'lon' : -71.095128, 'line' : ('G',) }, ***
            15593 : { 'name' : 'Copley', 'lat' : 42.349991, 'lon' : -71.077463, 'line' : ('G',) },
            # 15593 : { 'name' : 'Copley', 'lat' : 42.349991, 'lon' : -71.077463, 'line' : ('G',) }, ***
            # 15593 : { 'name' : 'Copley', 'lat' : 42.349991, 'lon' : -71.077463, 'line' : ('G',) }, ***
            # 15593 : { 'name' : 'Copley Station', 'lat' : 42.349991, 'lon' : -71.077463, 'line' : ('G',) }, ***
            # 15593 : { 'name' : 'Copley', 'lat' : 42.349991, 'lon' : -71.077463, 'line' : ('G',) }, ***
            15595 : { 'name' : 'Arlington', 'lat' : 42.351847, 'lon' : -71.070817, 'line' : ('G',) },            
            15596 : { 'name' : 'Boylston Street', 'lat' : 42.352337, 'lon' : -71.06461, 'line' : ('G',) },
            15598 : { 'name' : 'Riverside', 'lat' : 42.337394, 'lon' : -71.252327, 'line' : ('G',) },
            15601 : { 'name' : 'Waban', 'lat' : 42.325981, 'lon' : -71.230712, 'line' : ('G',) },
            15602 : { 'name' : 'Eliot', 'lat' : 42.318744, 'lon' : -71.217023, 'line' : ('G',) },
            15604 : { 'name' : 'Newton Highlands', 'lat' : 42.321539, 'lon' : -71.205966, 'line' : ('G',) },
            15605 : { 'name' : 'Newton Center', 'lat' : 42.328354, 'lon' : -71.194444, 'line' : ('G',) },
            15607 : { 'name' : 'Chestnut Hill', 'lat' : 42.326601, 'lon' : -71.16529, 'line' : ('G',) },
            15609 : { 'name' : 'Reservoir', 'lat' : 42.334912, 'lon' : -71.149072, 'line' : ('G',) },
            15611 : { 'name' : 'Beaconsfield', 'lat' : 42.335805, 'lon' : -71.140849, 'line' : ('G',) },
            15614 : { 'name' : 'Brookline Village', 'lat' : 42.332002, 'lon' : -71.118129, 'line' : ('G',) },
            15617 : { 'name' : 'Fenway Station', 'lat' : 42.345347, 'lon' : -71.104156, 'line' : ('G',) },            
            15621 : { 'name' : 'Hawes Street', 'lat' : 42.34487, 'lon' : -71.111129, 'line' : ('G',) },
            15623 : { 'name' : 'Kent Street', 'lat' : 42.344125, 'lon' : -71.113885, 'line' : ('G',) },
            15624 : { 'name' : 'St. Paul Street', 'lat' : 42.343366, 'lon' : -71.116759, 'line' : ('G',) },
            15625 : { 'name' : 'Coolidge Corner', 'lat' : 42.342226, 'lon' : -71.120888, 'line' : ('G',) },
            15627 : { 'name' : 'Summit Avenue', 'lat' : 42.340946, 'lon' : -71.125182, 'line' : ('G',) },
            15629 : { 'name' : 'Brandon Hall', 'lat' : 42.339683, 'lon' : -71.129327, 'line' : ('G',) },            
            15633 : { 'name' : 'Tappan Street', 'lat' : 42.338469, 'lon' : -71.138705, 'line' : ('G',) },
            15634 : { 'name' : 'Dean Road', 'lat' : 42.337847, 'lon' : -71.141549, 'line' : ('G',) },
            15636 : { 'name' : 'Englewood Avenue', 'lat' : 42.337049, 'lon' : -71.145357, 'line' : ('G',) },            
            15639 : { 'name' : 'Prudential', 'lat' : 42.345503, 'lon' : -71.081401, 'line' : ('G',) },
            15640 : { 'name' : 'Symphony', 'lat' : 42.342919, 'lon' : -71.084529, 'line' : ('G',) },
            15642 : { 'name' : 'Northeastern University', 'lat' : 42.340307, 'lon' : -71.088717, 'line' : ('G',) },
            15643 : { 'name' : 'Museum of Fine Arts', 'lat' : 42.337732, 'lon' : -71.095125, 'line' : ('G',) },
            15645 : { 'name' : 'Longwood Medical Area', 'lat' : 42.335898, 'lon' : -71.100052, 'line' : ('G',) },
            15646 : { 'name' : 'Brigham Circle', 'lat' : 42.334268, 'lon' : -71.10437, 'line' : ('G',) },
            15648 : { 'name' : 'Fenwood Street', 'lat' : 42.333722, 'lon' : -71.105682, 'line' : ('G',) },            
            15652 : { 'name' : 'Back of the Hill', 'lat' : 42.32996, 'lon' : -71.111406, 'line' : ('G',) },
            15653 : { 'name' : 'Heath Street', 'lat' : 42.32868, 'lon' : -71.11068, 'line' : ('G',) },            
            15655 : { 'name' : 'Washington Square', 'lat' : 42.339258, 'lon' : -71.135387, 'line' : ('G',) },
            15659 : { 'name' : 'Cedar Grove', 'lat' : 42.279712, 'lon' : -71.060327, 'line' : ('R',) },
            15660 : { 'name' : 'Butler', 'lat' : 42.272253, 'lon' : -71.062453, 'line' : ('R',) },
            15664 : { 'name' : 'Central Avenue', 'lat' : 42.269965, 'lon' : -71.073249, 'line' : ('R',) },
            15665 : { 'name' : 'Valley ROad', 'lat' : 42.267772, 'lon' : -71.083025, 'line' : ('R',) },
            15667 : { 'name' : 'Capen Street', 'lat' : 42.267622, 'lon' : -71.087436, 'line' : ('R',) },
            15668 : { 'name' : 'Mattapan', 'lat' : 42.267586, 'lon' : -71.092021, 'line' : ('R',) },
            15670 : { 'name' : 'Hynes Convention Center', 'lat' : 42.347953, 'lon' : -71.088148, 'line' : ('G',) },            
            15672 : { 'name' : 'Park Street', 'lat' : 42.356332, 'lon' : -71.062202, 'line' : ('G',) },            
            15675 : { 'name' : 'Lechmere', 'lat' : 42.370774, 'lon' : -71.076593, 'line' : ('G',) },
            # 15675 : { 'name' : 'Lechmere', 'lat' : 42.370774, 'lon' : -71.076593, 'line' : ('G',) }, ***
            15676 : { 'name' : 'Woodland', 'lat' : 42.333336, 'lon' : -71.24434, 'line' : ('G',) },
            15679 : { 'name' : 'Brookline Hills', 'lat' : 42.331133, 'lon' : -71.127031, 'line' : ('G',) },
            15680 : { 'name' : 'Longwood', 'lat' : 42.341042, 'lon' : -71.110215, 'line' : ('G',) },            
            15681 : { 'name' : 'St. Marys Street', 'lat' : 42.345947, 'lon' : -71.107385, 'line' : ('G',) },
            15683 : { 'name' : 'Fairbanks', 'lat' : 42.339474, 'lon' : -71.131304, 'line' : ('G',) },
            15685 : { 'name' : 'Cleveland Circle', 'lat' : 42.336197, 'lon' : -71.149406, 'line' : ('G',) },            
            15689 : { 'name' : 'Mission Park', 'lat' : 42.333106, 'lon' : -71.109678, 'line' : ('G',) },
            15690 : { 'name' : 'Riverway', 'lat' : 42.331686, 'lon' : -71.112004, 'line' : ('G',) },
            15692 : { 'name' : 'Milton', 'lat' : 42.270093, 'lon' : -71.067612, 'line' : ('R',) },

            24419 : { 'name' : 'Chinatown', 'lat' : 42.352529, 'lon' : -71.062759, 'line' : ('S',) },
            24642 : { 'name' : 'Melnea Cass Blvd', 'lat' : 42.332709, 'lon' : -71.081205, 'line' : ('S',) },
            
            25092 : { 'name' : 'World Trade Center', 'lat' : 42.349098, 'lon' : -71.04206, 'line' : ('S',) },
            # 25092 : { 'name' : 'World Trade Center', 'lat' : 42.349098, 'lon' : -71.04206, 'line' : ('S',) }, ***
            25093 : { 'name' : 'Design Center', 'lat' : 42.344579, 'lon' : -71.034448, 'line' : ('S',) },            
            25100 : { 'name' : 'Silver Line Way', 'lat' : 42.347928, 'lon' : -71.039287, 'line' : ('S',) },            
            # 25100 : { 'name' : 'Siver Line Way', 'lat' : 42.347928, 'lon' : -71.039287, 'line' : ('S',) }, ***
            25117 : { 'name' : '306 Northern Way', 'lat' : 42.34769, 'lon' : -71.035882, 'line' : ('S',) },
            25133 : { 'name' : 'Courthouse', 'lat' : 42.352724, 'lon' : -71.047514, 'line' : ('S',) },
            # 25133 : { 'name' : 'Courthouse Station', 'lat' : 42.352724, 'lon' : -71.047514, 'line' : ('S',) }, ***
            25134 : { 'name' : '88 Black Falcon Avenue', 'lat' : 42.344105, 'lon' : -71.02724, 'line' : ('S',) },
            25168 : { 'name' : 'Terminal B Stop 1', 'lat' : 42.363726, 'lon' : -71.019404, 'line' : ('S',) },
            25329 : { 'name' : 'Terminal A', 'lat' : 42.364386, 'lon' : -71.021487, 'line' : ('S',) },
            25331 : { 'name' : 'Terminal B Stop 2', 'lat' : 42.364441, 'lon' : -71.01882, 'line' : ('S',) },
            25332 : { 'name' : 'Terminal C', 'lat' : 42.367461, 'lon' : -71.018148, 'line' : ('S',) },
            25333 : { 'name' : 'Terminal E', 'lat' : 42.370242, 'lon' : -71.020467, 'line' : ('S',) },

            90010 : { 'name' : 'Downtown Crossing', 'lat' : 42.355453, 'lon' : -71.060465, 'line' : ('S',) },            
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
            'url' : { '_content' : 'http://www.mbta.com/schedules_and_maps/subway/lines/stations/?stopId=%s' % code },
            }
        
        self.api_ok({'station' : out})
        return
