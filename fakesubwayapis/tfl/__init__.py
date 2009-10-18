import fakesubwayapis

class tfl :

    def __init__ (self) :

        # http://www.tfl.gov.uk/tfl/livetravelnews/departureboards/default.asp

        self.service = {
            'id' : 'tfl',
            'name' : 'Transport For London',
            'url' : 'http://tfl.gov.uk'
            }

        self.lines = {
            'B' : 'bakerloo',
            'C' : 'central',
            'D' : 'district',
            'H' : 'hammersmith',
            'J' : 'jubilee',
            'M' : 'metropolitain',
            'N' : 'northern',
            'O' : 'circle',
            'P' : 'piccadilly',
            'V' : 'victoria',
            'W' : 'waterloo',
            }
        
        self.stations = {

            #

            "ACT" : { "name" : "Acton Town", "line" : ("D", "P") },
            "AGR" : { "name" : "Arnos Grove", "line" : ("P",) },
            "ALD" : { "name" : "Aldgate", "line" : ("O", "H", "M") },            
            "ALE" : { "name" : "Aldgate East", "line" : ("D", "H") },
            "ALP" : { "name" : "Alperton", "line" : ("P",) },
            "AME" : { "name" : "Amersham", "line" : ("M",) },
            "ANG" : { "name" : "Angel", "line" : ("N",) },
            "ARC" : { "name" : "Archway", "line" : ("N",) },
            "ARL" : { "name" : "Arsenal", "line" : ("P",) },
            
            "BAL" : { "name" : "Balham", "line" : ("N",) },            
            "BAR" : { "name" : "Barbican", "line" : ("O", "H", "M") }, 
            "BAY" : { "name" : "Bayswater", "line" : ("O", "H") },
            "BBB" : { "name" : "Bromley-by-Bow", "line" : ("O", "D", "H") },
            "BCT" : { "name" : "Barons Court", "line" : ("D", "P") },
            "BDE" : { "name" : "Barkingside", "line" : ("C",) },
            "BDS" : { "name" : "Bond Street", "line" : ("C", "J") },
            "BEC" : { "name" : "Becontree", "line" : ("D",) },
            "BER" : { "name" : "Bermondsey", "line" : ("J",) },
            "BGR" : { "name" : "Bounds Green", "line" : ("P",) },
            "BHL" : { "name" : "Buckhurst Hill", "line" : ("C",) },
            "BHR" : { "name" : "Blackhorse Road", "line" : ("V",) },
            "BKG" : { "name" : "Barking", "line" : ("O", "D", "H") },
            "BLF" : { "name" : "Blackfriars", "line" : ("O", "D", "H") },
            "BNG" : { "name" : "Bethnal Green", "line" : ("C",) },
            "BNK" : { "name" : "Bank", "line" : ("C", "N", "W") },
            "BOR" : { "name" : "Borough", "line" : ("N",) },            
            "BOS" : { "name" : "Boston Manor", "line" : ("P",) },
            "BPK" : { "name" : "Belsize Park", "line" : ("N",) },
            "BRX" : { "name" : "Brixton", "line" : ("V",) },
            "BST" : { "name" : "Baker Street", "line" : ("B", "O", "H", "J", "M") },            
            "BTX" : { "name" : "Brent Cross", "line" : ("N",) },
            "BUR" : { "name" : "Burnt Oak", "line" : ("N",) },
            "BWR" : { "name" : "Bow Road", "line" : ("O", "D", "H") },

            "CFS" : { "name" : "Cockfosters", "line" : ("P",) },
            "CHF" : { "name" : "Chalk Farm", "line" : ("N",) },
            "CHG" : { "name" : "Chigwell", "line" : ("C",) },           
            "CHP" : { "name" : "Chiswick Park", "line" : ("D",) },            
            "CHX" : { "name" : "Charing Cross", "line" : ("B", "J", "N") },
            "CLF" : { "name" : "Chalfont & Latimer", "line" : ("M",) },
            "CLW" : { "name" : "Colliers Wood", "line" : ("N",) },
            "CNT" : { "name" : "Canning Town", "line" : ("J",) },
            "COL" : { "name" : "Colindale", "line" : ("N",) },
            "COV" : { "name" : "Covent Garden", "line" : ("P",) },            
            "CPC" : { "name" : "Clapham Common", "line" : ("N",) },
            "CPK" : { "name" : "Canons Park", "line" : ("J",) },
            "CPN" : { "name" : "Clapham North", "line" : ("N",) },
            "CPS" : { "name" : "Clapham South", "line" : ("N",) },
            "CRD" : { "name" : "Caledonian Road", "line" : ("P",) },            
            "CRX" : { "name" : "Croxley", "line" : ("M",) },
            "CST" : { "name" : "Cannon Street", "line" : ("O", "D", "H") },
            "CTN" : { "name" : "Camden Town", "line" : ("N",) },
            "CWD" : { "name" : "Chorleywood", "line" : ("M",) },
            "CWF" : { "name" : "Canary Wharf", "line" : ("J",) },
            "CWR" : { "name" : "Canada Water", "line" : ("J",) },
            "CYL" : { "name" : "Chancery Lane", "line" : ("C",) },

            "DEB" : { "name" : "Debden", "line" : ("C",) },
            "DGE" : { "name" : "Dagenham East", "line" : ("D",) },
            "DGH" : { "name" : "Dagenham Heathway", "line" : ("D",) },
            "DHL" : { "name" : "Dollis Hill", "line" : ("J",) },
            
            "EAC" : { "name" : "East Acton", "line" : ("C",) },            
            "EBY" : { "name" : "Ealing Broadway", "line" : ("C", "D") },
            "ECM" : { "name" : "Ealing Common", "line" : ("D", "P") },
            "ECT" : { "name" : "Earls Court", "line" : ("D", "P") },
            "EDG" : { "name" : "Edgware", "line" : ("N",) },
            "EFY" : { "name" : "East Finchley", "line" : ("N",) },
            "EHM" : { "name" : "East Ham", "line" : ("O", "D", "H") },
            "ELE" : { "name" : "Elephant & Castle", "line" : ("B", "N") },
            "EMB" : { "name" : "Embankment", "line" : ("B", "O", "D", "H", "N") },            
            "EPK" : { "name" : "Elm Park", "line" : ("D",) },
            "EPP" : { "name" : "Epping", "line" : ("C",) },
            "EPY" : { "name" : "East Putney", "line" : ("D",) },
            "ERB" : { "name" : "Edgware Road", "line" : ("B",) },
            "ERD" : { "name" : "Edgware Road (H & C)", "line" : ("O", "D", "H") },
            "ESQ" : { "name" : "Euston Square", "line" : ("O", "H", "M") },
            "ETE" : { "name" : "Eastcote", "line" : ("M", "P") },
            "EUS" : { "name" : "Euston", "line" : ("N", "V") },

            "FAR" : { "name" : "Farringdon", "line" : ("O", "H", "M") },            
            "FBY" : { "name" : "Fulham Broadway", "line" : ("D",) },
            "FLP" : { "name" : "Fairlop", "line" : ("C",) },
            "FPK" : { "name" : "Finsbury Park", "line" : ("P", "V") },
            "FRD" : { "name" : "Finchley Road", "line" : ("J", "M") },
            "FYC" : { "name" : "Finchley Central", "line" : ("N",) },
            
            "GFD" : { "name" : "Greenford", "line" : ("C",) },
            "GGR" : { "name" : "Golders Green", "line" : ("N",) },
            "GHL" : { "name" : "Gants Hill", "line" : ("C",) },
            "GPK" : { "name" : "Green Park", "line" : ("J", "P", "V") },            
            "GPS" : { "name" : "Great Portland Street", "line" : ("O", "H", "M") },
            "GRD" : { "name" : "Gloucester Road", "line" : ("D", "H", "O", "P") },
            "GRH" : { "name" : "Grange Hill", "line" : ("C",) },
            "GST" : { "name" : "Goodge Street", "line" : ("N",) },
            "GUN" : { "name" : "Gunnersbury", "line" : ("D",) },
            
            "HAI" : { "name" : "Hainault", "line" : ("C",) },            
            "HAW" : { "name" : "Harrow & Wealdstone", "line" : ("B",) },
            "HBT" : { "name" : "High Barnet", "line" : ("N",) },
            "HBY" : { "name" : "Highbury & Islington", "line" : ("V",) },
            "HCH" : { "name" : "Hornchurch", "line" : ("D",) },
            "HDN" : { "name" : "Hillingdon", "line" : ("M", "P") },
            "HIG" : { "name" : "Highgate", "line" : ("N",) },
            "HLN" : { "name" : "Hanger Lane", "line" : ("C",) },
            "HMD" : { "name" : "Hammersmith (District and Picc)", "line" : ("D", "P") },
            "HMP" : { "name" : "Hampstead", "line" : ("N",) },
            "HMS" : { "name" : "Hammersmith (Circle and H&C)", "line" : ("O", "H") },
            "HNC" : { "name" : "Hounslow Central", "line" : ("P",) },
            "HND" : { "name" : "Hendon Central", "line" : ("N",) },
            "HNE" : { "name" : "Hounslow East", "line" : ("P",) },
            "HNW" : { "name" : "Hounslow West", "line" : ("P",) },
            "HOH" : { "name" : "Harrow on the Hill", "line" : ("M",) },
            "HOL" : { "name" : "Holborn", "line" : ("C", "P") },
            "HPC" : { "name" : "Hyde Park Corner", "line" : ("P",) },
            "HPK" : { "name" : "Holland Park", "line" : ("C",) },           
            "HRC" : { "name" : "Heathrow Terminals 123", "line" : ("P",) },            
            "HRD" : { "name" : "Holloway Road", "line" : ("P",) },
            "HRF" : { "name" : "Heathrow Terminal 4", "line" : ("P",) },
            "HRV" : { "name" : "Heathrow Terminal 5", "line" : ("P",) },            
            "HSD" : { "name" : "Harlesden", "line" : ("B",) },
            "HST" : { "name" : "High Street Kensington", "line" : ("O", "D", "H") },            
            "HTX" : { "name" : "Hatton Cross", "line" : ("P",) },
            
            "ICK" : { "name" : "Ickenham", "line" : ("M", "P") },

            "KBY" : { "name" : "Kingsbury", "line" : ("J",) },
            "KEN" : { "name" : "Kennington", "line" : ("N",) },            
            "KEW" : { "name" : "Kew Gardens", "line" : ("D",) },
            "KGN" : { "name" : "Kensal Green", "line" : ("B",) },
            "KIL" : { "name" : "Kilburn", "line" : ("J",) },
            "KNB" : { "name" : "Knightsbridge", "line" : ("P",) },            
            "KNT" : { "name" : "Kenton", "line" : ("B",) },
            "KPK" : { "name" : "Kilburn Park", "line" : ("B",) },
            "KTN" : { "name" : "Kentish Town", "line" : ("N",) },
            "KXX" : { "name" : "King's Cross St. Pancras", "line" : ("O", "H", "M", "N", "P", "V") },

            "LAM" : { "name" : "Lambeth North", "line" : ("B",) },
            "LAN" : { "name" : "Lancaster Gate", "line" : ("C",) },
            "LBG" : { "name" : "Ladbroke Grove", "line" : ("O", "H") },
            "LEY" : { "name" : "Leyton", "line" : ("C",) },
            "LON" : { "name" : "London Bridge", "line" : ("J", "N") },
            "LSQ" : { "name" : "Leicester Square", "line" : ("N", "P") },
            "LST" : { "name" : "Liverpool Street", "line" : ("C", "O", "H", "M") },
            "LTN" : { "name" : "Loughton", "line" : ("C",) },
            "LYS" : { "name" : "Leytonstone", "line" : ("C",) },
            
            "MAN" : { "name" : "Mansion House", "line" : ("O", "D", "H") },            
            "MAR" : { "name" : "Marble Arch", "line" : ("C",) },
            "MCR" : { "name" : "Mornington Crescent", "line" : ("N",) },
            "MDV" : { "name" : "Maida Vale", "line" : ("B",) },
            "MGT" : { "name" : "Moorgate", "line" : ("O", "H", "M", "N") },
            "MHE" : { "name" : "Mill Hill East", "line" : ("N",) },
            "MLE" : { "name" : "Mile End", "line" : ("C", "D", "H", "O") },
            "MNR" : { "name" : "Manor House", "line" : ("P",) },
            "MON" : { "name" : "Monument", "line" : ("O", "D", "H") },
            "MOR" : { "name" : "Morden", "line" : ("N",) },
            "MPK" : { "name" : "Moor Park", "line" : ("M",) },
            "MYB" : { "name" : "Marylebone", "line" : ("B",) },

            "NAC" : { "name" : "North Acton", "line" : ("C",) },
            "NEA" : { "name" : "Neasden", "line" : ("J",) },
            "NEL" : { "name" : "North Ealing", "line" : ("P",) },
            "NEP" : { "name" : "Newbury Park", "line" : ("C",) },
            "NFD" : { "name" : "Northfields", "line" : ("P",) },
            "NGW" : { "name" : "North Greenwich", "line" : ("J",) },
            "NHG" : { "name" : "Notting Hill Gate", "line" : ("C", "O", "H") },
            "NHR" : { "name" : "North Harrow", "line" : ("M",) },
            "NHT" : { "name" : "Northolt", "line" : ("C",) },
            "NWD" : { "name" : "Northwood", "line" : ("M",) },
            "NWH" : { "name" : "Northwood Hills", "line" : ("M",) },
            "NWM" : { "name" : "North Wembley", "line" : ("B",) },
            "NWP" : { "name" : "Northwick Park", "line" : ("M",) },

            "OAK" : { "name" : "Oakwood", "line" : ("P",) },
            "OLD" : { "name" : "Old Street", "line" : ("N",) },
            "OST" : { "name" : "Osterley", "line" : ("P",) },
            "OVL" : { "name" : "Oval", "line" : ("N",) },
            
            "QBY" : { "name" : "Queensbury", "line" : ("J",) },
            "OLY" : { "name" : "Olympia", "line" : ("D",) },
            "OXC" : { "name" : "Oxford Circus", "line" : ("B","C", "V") },

            "PAD" : { "name" : "Paddington", "line" : ("B", "C", "O") },
            # "PADc" : { "name" : "Paddington Circle", "line" : ("H",) },
            # "PADs" : { "name" : "Paddington H & C", "line" : ("H",) },
            "PER" : { "name" : "Perivale", "line" : ("C",) },
            "PGR" : { "name" : "Parsons Green", "line" : ("D",) },
            "PIC" : { "name" : "Piccadilly Circus", "line" : ("B", "P") },
            "PIM" : { "name" : "Pimlico", "line" : ("V",) },
            "PIN" : { "name" : "Pinner", "line" : ("M",) },            
            "PLW" : { "name" : "Plaistow", "line" : ("O", "D", "H") },
            "PRY" : { "name" : "Park Royal", "line" : ("P",) },
            "PUT" : { "name" : "Putney Bridge", "line" : ("D",) },
            
            "QPK" : { "name" : "Queen's Park", "line" : ("B",) },
            "QWY" : { "name" : "Queensway", "line" : ("C",) },

            "RCP" : { "name" : "Ravenscourt Park", "line" : ("D",) },
            "RED" : { "name" : "Redbridge", "line" : ("C",) },            
            "RKY" : { "name" : "Rickmansworth", "line" : ("M",) },
            "RLN" : { "name" : "Rayners Lane", "line" : ("M", "P") },
            "RMD" : { "name" : "Richmond", "line" : ("D",) },
            "ROA" : { "name" : "Royal Oak", "line" : ("O", "H") },
            "ROD" : { "name" : "Roding Valley", "line" : ("C",) },
            "RPK" : { "name" : "Regent's Park", "line" : ("B",) },
            "RSQ" : { "name" : "Russell Square", "line" : ("P",) },
            "RUG" : { "name" : "Ruislip Gardens", "line" : ("C",) },
            "RUI" : { "name" : "Ruislip", "line" : ("M", "P") },
            "RUM" : { "name" : "Ruislip Manor", "line" : ("M", "P") },

            "SBC" : { "name" : "Shepherds Bush (Central Line)", "line" : ("C",) },
            "SEL" : { "name" : "South Ealing", "line" : ("P",) },
            "SFD" : { "name" : "Stratford", "line" : ("C", "J") },
            "SGT" : { "name" : "Southgate", "line" : ("P",) },            
            "SFS" : { "name" : "Southfields", "line" : ("D",) },
            "SHL" : { "name" : "Sudbury Hill", "line" : ("P",) },
            "SHR" : { "name" : "South Harrow", "line" : ("P",) },
            "SJP" : { "name" : "St. James's Park", "line" : ("O", "D", "H") },                        
            "SJW" : { "name" : "St. John's Wood", "line" : ("J",) },
            "SKN" : { "name" : "South Kensington", "line" : ("O", "D", "H", "P") },
            "SKT" : { "name" : "South Kenton", "line" : ("B",) },
            "SNB" : { "name" : "Snaresbrook", "line" : ("C",) },
            "SPK" : { "name" : "Stonebridge Park", "line" : ("B",) },
            "SRP" : { "name" : "South Ruislip", "line" : ("C",) },
            "SSQ" : { "name" : "Sloane Square", "line" : ("O", "D", "H") },
            "STA" : { "name" : "Stanmore", "line" : ("J",) },
            "STB" : { "name" : "Stamford Brook", "line" : ("D",) },
            "STG" : { "name" : "Stepney Green", "line" : ("O", "D", "H") },
            "STK" : { "name" : "Stockwell", "line" : ("N", "V") },
            "STN" : { "name" : "Sudbury Town", "line" : ("P",) },
            "STP" : { "name" : "St. Paul's", "line" : ("C",) },
            "SVS" : { "name" : "Seven Sisters", "line" : ("V",) },
            "SWC" : { "name" : "Swiss Cottage", "line" : ("J",) },
            "SWF" : { "name" : "South Woodford", "line" : ("C",) },
            "SWK" : { "name" : "Southwark", "line" : ("J",) },
            "SWM" : { "name" : "South Wimbledon", "line" : ("N",) },

            "TBE" : { "name" : "Tooting Bec", "line" : ("N",) },
            "TBY" : { "name" : "Tooting Broadway", "line" : ("N",) },            
            "TCR" : { "name" : "Tottenham Court Road", "line" : ("C", "N") },            
            "TEM" : { "name" : "Temple", "line" : ("O", "D", "H") },
            "TGR" : { "name" : "Turnham Green", "line" : ("D", "P") },
            "THB" : { "name" : "Theydon Bois", "line" : ("C",) },
            "THL" : { "name" : "Tower Hill", "line" : ("O", "D", "H") },
            "TOT" : { "name" : "Totteridge and Whetstone", "line" : ("N",) },
            "TPK" : { "name" : "Tufnell Park", "line" : ("N",) },
            "TPL" : { "name" : "Turnpike Lane", "line" : ("P",) },
            "TTH" : { "name" : "Tottenham Hale", "line" : ("V",) },
            
            "UPB" : { "name" : "Upminster Bridge", "line" : ("D",) },
            "UPK" : { "name" : "Upton Park", "line" : ("O", "D", "H") },
            "UPM" : { "name" : "Upminster", "line" : ("D",) },
            "UPY" : { "name" : "Upney", "line" : ("D",) },
            "UXB" : { "name" : "Uxbridge", "line" : ("M", "P") },            

            "VIC" : { "name" : "Victoria", "line" : ("O", "D", "H", "V") },
            "VUX" : { "name" : "Vauxhall", "line" : ("V",) },
            
            "WAC" : { "name" : "West Acton", "line" : ("C",) },
            "WAL" : { "name" : "Walthamstow Central", "line" : ("V",) },
            "WAN" : { "name" : "Wanstead", "line" : ("C",) },            
            "WAR" : { "name" : "Warwick Avenue", "line" : ("B",) },
            "WAT" : { "name" : "Watford", "line" : ("M",) },            
            "WBP" : { "name" : "Westbourne Park", "line" : ("O", "H") },
            "WBT" : { "name" : "West Brompton", "line" : ("D",) },
            "WCL" : { "name" : "Whitechapel", "line" : ("O", "D", "H", "M") },
            "WCT" : { "name" : "White City", "line" : ("C",) },
            "WDN" : { "name" : "Wimbledon", "line" : ("D",) },
            "WEM" : { "name" : "Wembley Central", "line" : ("B",) },
            "WFD" : { "name" : "Woodford", "line" : ("C",) },
            "WFY" : { "name" : "West Finchley", "line" : ("N",) },
            "WGN" : { "name" : "Wood Green", "line" : ("P",) },
            "WHD" : { "name" : "West Hampstead", "line" : ("J",) },
            "WHM" : { "name" : "West Ham", "line" : ("O", "D", "H", "J") },
            "WHR" : { "name" : "West Harrow", "line" : ("M",) },
            "WJN" : { "name" : "Willesden Junction", "line" : ("B",) },
            "WKN" : { "name" : "West Kensington", "line" : ("D",) },
            "WLG" : { "name" : "Willesden Green", "line" : ("J",) },            
            "WLO" : { "name" : "Waterloo", "line" : ("B", "J", "N", "W") },
            "WMP" : { "name" : "Wimbledon Park", "line" : ("D",) },
            "WMS" : { "name" : "Westminster", "line" : ("O", "D", "H", "J") },            
            "WPK" : { "name" : "Wembley Park", "line" : ("J", "M") },
            "WRP" : { "name" : "West Ruislip", "line" : ("C",) },
            "WSP" : { "name" : "Woodside Park", "line" : ("M", "N") },
            "WST" : { "name" : "Warren Street", "line" : ("N", "V") },
                        
            }

    def generate_url (self, code, **more) :
        
        if not more.has_key('line_code') :
            return fakesubwayapis.fakesubwayapi.generate_url(self, code)

        if not self.stations[code].has_key('line') :        
            return fakesubwayapis.fakesubwayapi.generate_url(self, code)

        if not more['line_code'] in self.lines :
            return fakesubwayapis.fakesubwayapi.generate_url(self, code)

        line_name = self.lines[ more['line_code'] ]

        return "http://www.tfl.gov.uk/tfl/livetravelnews/departureboards/tube/default.asp?LineCode=%s&StationCode=%s" % (line_name, code.upper())
        
class docs (tfl, fakesubwayapis.fakesubwayapidocs) :

    def __init__ (self) :

        tfl.__init__(self)
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        
    def get (self) :

        self.show_docs(generate_compound_ids=True)
        return

class station (tfl, fakesubwayapis.fakesubwaystation) :

    def __init__ (self) :

        tfl.__init__(self)
        fakesubwayapis.fakesubwaystation.__init__(self)

    def get (self, station_code, line_code) :

        if line_code :
            self.do_redirect(station_code, line_code=line_code)
            return

        self.show_station(station_code)
        return
    
class api (tfl, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        tfl.__init__(self)
        fakesubwayapis.fakesubwayapi.__init__(self)
        
class getinfo (api) :
    
    def get (self, station_code, line_code) :

        code = station_code.upper()

        self.generate_info(code, line_code=line_code)
        return
