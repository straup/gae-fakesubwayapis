import fakesubwayapis

class tfl :

    def __init__ (self) :

        # http://www.tfl.gov.uk/tfl/livetravelnews/departureboards/default.asp

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
            "ALD" : { "name" : "Aldgate", "line" : ("O", "H", "M") },            
            "ALE" : { "name" : "Aldgate East", "line" : ("D", "H") },

            "BAR" : { "name" : "Barbican", "line" : ("O", "H", "M") }, 
            "BAY" : { "name" : "Bayswater", "line" : ("O", "H") },
            "BBB" : { "name" : "Bromley-by-Bow", "line" : ("O", "D", "H") },
            "BCT" : { "name" : "Barons Court", "line" : ("D",) },
            "BDE" : { "name" : "Barkingside", "line" : ("C",) },
            "BDS" : { "name" : "Bond Street", "line" : ("C", "J") },
            "BEC" : { "name" : "Becontree", "line" : ("D",) },
            "BHL" : { "name" : "Buckhurst Hill", "line" : ("C",) },
            "BKG" : { "name" : "Barking", "line" : ("O", "D", "H") },
            "BLF" : { "name" : "Blackfriars", "line" : ("O", "D", "H") },
            "BNG" : { "name" : "Bethnal Green", "line" : ("C",) },
            "BNK" : { "name" : "Bank", "line" : ("C", "N", "W") },            
            "BST" : { "name" : "Baker Street", "line" : ("B", "O", "H", "J", "M") },            
            "BWR" : { "name" : "Bow Road", "line" : ("O", "D", "H") },

            "CHG" : { "name" : "Chigwell", "line" : ("C",) },
            "CHP" : { "name" : "Chiswick Park", "line" : ("D",) },            
            "CHX" : { "name" : "Charing Cross", "line" : ("B", "J", "N") },
            "CST" : { "name" : "Cannon Street", "line" : ("O", "D", "H") },
            "CYL" : { "name" : "Chancery Lane", "line" : ("C",) },

            "DEB" : { "name" : "Debden", "line" : ("C",) },
            "DGE" : { "name" : "Dagenham East", "line" : ("D",) },
            "DGH" : { "name" : "Dagenham Heathway", "line" : ("D",) },
            
            "EAC" : { "name" : "East Acton", "line" : ("C",) },            
            "EBY" : { "name" : "Ealing Broadway", "line" : ("C", "D") },
            "ECM" : { "name" : "Ealing Common", "line" : ("D", "P") },
            "ECT" : { "name" : "Earls Court", "line" : ("D",) },
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

            "GFD" : { "name" : "Greenford", "line" : ("C",) },
            "GHL" : { "name" : "Gants Hill", "line" : ("C",) },
            "GPK" : { "name" : "Green Park", "line" : ("J", "P", "V") },            
            "GPS" : { "name" : "Great Portland Street", "line" : ("O", "H", "M") },
            "GRD" : { "name" : "Gloucester Road", "line" : ("D", "H", "O", "P") },
            "GRH" : { "name" : "Grange Hill", "line" : ("C",) },
            "GUN" : { "name" : "Gunnersbury", "line" : ("D",) },
            
            "HAI" : { "name" : "Hainault", "line" : ("C",) },            
            "HAW" : { "name" : "Harrow & Wealdstone", "line" : ("B",) },
            "HCH" : { "name" : "Hornchurch", "line" : ("D",) },
            "HDN" : { "name" : "Hillingdon", "line" : ("M", "P") },
            "HLN" : { "name" : "Hanger Lane", "line" : ("C",) },
            "HMD" : { "name" : "Hammersmith (District and Picc)", "line" : ("D",) },
            "HMS" : { "name" : "Hammersmith (Circle and H&C)", "line" : ("O", "H") },
            "HOL" : { "name" : "Holborn", "line" : ("C", "P") },
            "HPK" : { "name" : "Holland Park", "line" : ("C",) },            
            "HSD" : { "name" : "Harlesden", "line" : ("B",) },
            "HST" : { "name" : "High Street Kensington", "line" : ("O", "D", "H") },            

            "ICK" : { "name" : "Ickenham", "line" : ("M", "P") },

            "KEW" : { "name" : "Kew Gardens", "line" : ("D",) },
            "KGN" : { "name" : "Kensal Green", "line" : ("B",) },
            "KNT" : { "name" : "Kenton", "line" : ("B",) },
            "KPK" : { "name" : "Kilburn Park", "line" : ("B",) },
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
            "MDV" : { "name" : "Maida Vale", "line" : ("B",) },
            "MGT" : { "name" : "Moorgate", "line" : ("O", "H", "M", "N") },
            "MLE" : { "name" : "Mile End", "line" : ("C", "D", "H", "O") },
            "MON" : { "name" : "Monument", "line" : ("O", "D", "H") },
            "MYB" : { "name" : "Marylebone", "line" : ("B",) },

            "NAC" : { "name" : "North Acton", "line" : ("C",) },
            "NEP" : { "name" : "Newbury Park", "line" : ("C",) },
            "NHG" : { "name" : "Notting Hill Gate", "line" : ("C", "O", "H") },
            "NHT" : { "name" : "Northolt", "line" : ("C",) },
            "NWM" : { "name" : "North Wembley", "line" : ("B",) },

            "OLY" : { "name" : "Olympia", "line" : ("D",) },
            "OXC" : { "name" : "Oxford Circus", "line" : ("B","C", "V") },

            "PAD" : { "name" : "Paddington", "line" : ("B", "C", "O") },
            # "PADc" : { "name" : "Paddington Circle", "line" : ("H",) },
            # "PADs" : { "name" : "Paddington H & C", "line" : ("H",) },
            "PER" : { "name" : "Perivale", "line" : ("C",) },
            "PGR" : { "name" : "Parsons Green", "line" : ("D",) },
            "PIC" : { "name" : "Piccadilly Circus", "line" : ("B",) },
            "PLW" : { "name" : "Plaistow", "line" : ("O", "D", "H") },
            "PUT" : { "name" : "Putney Bridge", "line" : ("D",) },
            
            "QPK" : { "name" : "Queen's Park", "line" : ("B",) },
            "QWY" : { "name" : "Queensway", "line" : ("C",) },

            "RCP" : { "name" : "Ravenscourt Park", "line" : ("D",) },
            "RED" : { "name" : "Redbridge", "line" : ("C",) },            
            "RLN" : { "name" : "Rayners Lane", "line" : ("M", "P") },
            "RMD" : { "name" : "Richmond", "line" : ("D",) },
            "ROA" : { "name" : "Royal Oak", "line" : ("O", "H") },
            "ROD" : { "name" : "Roding Valley", "line" : ("C",) },
            "RPK" : { "name" : "Regent's Park", "line" : ("B",) },
            "RUG" : { "name" : "Ruislip Gardens", "line" : ("C",) },
            "RUI" : { "name" : "Ruislip", "line" : ("M", "P") },
            "RUM" : { "name" : "Ruislip Manor", "line" : ("M", "P") },

            "SBC" : { "name" : "Shepherds Bush (Central Line)", "line" : ("C",) },
            "SFD" : { "name" : "Stratford", "line" : ("C", "J") },
            "SFS" : { "name" : "Southfields", "line" : ("D",) },
            "SJP" : { "name" : "St. James's Park", "line" : ("O", "D", "H") },                        
            "SKN" : { "name" : "South Kensington", "line" : ("O", "D", "H", "P") },
            "SKT" : { "name" : "South Kenton", "line" : ("B",) },
            "SNB" : { "name" : "Snaresbrook", "line" : ("C",) },
            "SPK" : { "name" : "Stonebridge Park", "line" : ("B",) },
            "SRP" : { "name" : "South Ruislip", "line" : ("C",) },
            "SSQ" : { "name" : "Sloane Square", "line" : ("O", "D", "H") },
            "STB" : { "name" : "Stamford Brook", "line" : ("D",) },
            "STG" : { "name" : "Stepney Green", "line" : ("O", "D", "H") },
            "STK" : { "name" : "Stockwell", "line" : ("N", "V") },
            "STP" : { "name" : "St. Paul's", "line" : ("C",) },
            "SWF" : { "name" : "South Woodford", "line" : ("C",) },

            "TCR" : { "name" : "Tottenham Court Road", "line" : ("C",) },            
            "TEM" : { "name" : "Temple", "line" : ("O", "D", "H") },
            "TGR" : { "name" : "Turnham Green", "line" : ("D",) },
            "THB" : { "name" : "Theydon Bois", "line" : ("C",) },
            "THL" : { "name" : "Tower Hill", "line" : ("O", "D", "H") },

            "UPB" : { "name" : "Upminster Bridge", "line" : ("D",) },
            "UPK" : { "name" : "Upton Park", "line" : ("O", "D", "H") },
            "UPM" : { "name" : "Upminster", "line" : ("D",) },
            "UPY" : { "name" : "Upney", "line" : ("D",) },
            "UXB" : { "name" : "Uxbridge", "line" : ("M", "P") },            

            "VIC" : { "name" : "Victoria", "line" : ("O", "D", "H", "V") },

            "WAC" : { "name" : "West Acton", "line" : ("C",) },
            "WAN" : { "name" : "Wanstead", "line" : ("C",) },            
            "WAR" : { "name" : "Warwick Avenue", "line" : ("B",) },
            "WBP" : { "name" : "Westbourne Park", "line" : ("O", "H") },
            "WBT" : { "name" : "West Brompton", "line" : ("D",) },
            "WCL" : { "name" : "Whitechapel", "line" : ("O", "D", "H", "M") },
            "WCT" : { "name" : "White City", "line" : ("C",) },
            "WDN" : { "name" : "Wimbledon", "line" : ("D",) },
            "WEM" : { "name" : "Wembley Central", "line" : ("B",) },
            "WFD" : { "name" : "Woodford", "line" : ("C",) },
            "WHM" : { "name" : "West Ham", "line" : ("O", "D", "H", "J") },
            "WJN" : { "name" : "Willesden Junction", "line" : ("B",) },
            "WKN" : { "name" : "West Kensington", "line" : ("D",) },
            "WLO" : { "name" : "Waterloo", "line" : ("B", "J", "N", "W") },
            "WMP" : { "name" : "Wimbledon Park", "line" : ("D",) },
            "WMS" : { "name" : "Westminster", "line" : ("O", "D", "H", "J") },            
            "WRP" : { "name" : "West Ruislip", "line" : ("C",) },
            
            # Circle
            # District
            # Hammersmith and City
            # Jubilee
            
            "BER" : { "name" : "Bermondsey", "line" : ("J",) },
            "CWR" : { "name" : "Canada Water", "line" : ("J",) },
            "CWF" : { "name" : "Canary Wharf", "line" : ("J",) },
            "CNT" : { "name" : "Canning Town", "line" : ("J",) },
            "CPK" : { "name" : "Canons Park", "line" : ("J",) },
            "DHL" : { "name" : "Dollis Hill", "line" : ("J",) },
            "FRD" : { "name" : "Finchley Road", "line" : ("J",) },
            "KIL" : { "name" : "Kilburn", "line" : ("J",) },
            "KBY" : { "name" : "Kingsbury", "line" : ("J",) },
            "NEA" : { "name" : "Neasden", "line" : ("J",) },
            "NGW" : { "name" : "North Greenwich", "line" : ("J",) },
            "QBY" : { "name" : "Queensbury", "line" : ("J",) },
            "SWK" : { "name" : "Southwark", "line" : ("J",) },
            "SJW" : { "name" : "St. John's Wood", "line" : ("J",) },
            "STA" : { "name" : "Stanmore", "line" : ("J",) },
            "SWC" : { "name" : "Swiss Cottage", "line" : ("J",) },
            "WPK" : { "name" : "Wembley Park", "line" : ("J",) },
            "WHD" : { "name" : "West Hampstead", "line" : ("J",) },
            "WLG" : { "name" : "Willesden Green", "line" : ("J",) },
            
            # Metropolitain
            
            "AME" : { "name" : "Amersham", "line" : ("M",) },
            "CLF" : { "name" : "Chalfont & Latimer", "line" : ("M",) },
            "CWD" : { "name" : "Chorleywood", "line" : ("M",) },
            "CRX" : { "name" : "Croxley", "line" : ("M",) },
            "FRD" : { "name" : "Finchley Road", "line" : ("M",) },
            "HOH" : { "name" : "Harrow on the Hill", "line" : ("M",) },
            "MPK" : { "name" : "Moor Park", "line" : ("M",) },
            "NHR" : { "name" : "North Harrow", "line" : ("M",) },
            "NWP" : { "name" : "Northwick Park", "line" : ("M",) },
            "NWD" : { "name" : "Northwood", "line" : ("M",) },
            "NWH" : { "name" : "Northwood Hills", "line" : ("M",) },
            "PIN" : { "name" : "Pinner", "line" : ("M",) },
            "RKY" : { "name" : "Rickmansworth", "line" : ("M",) },
            "WAT" : { "name" : "Watford", "line" : ("M",) },
            "WPK" : { "name" : "Wembley Park", "line" : ("M",) },
            "WHR" : { "name" : "West Harrow", "line" : ("M",) },
            "WSP" : { "name" : "Woodside Park", "line" : ("M",) },
            
            # Northern

            "ANG" : { "name" : "Angel", "line" : ("N",) },
            "ARC" : { "name" : "Archway", "line" : ("N",) },
            "BAL" : { "name" : "Balham", "line" : ("N",) },
            "BPK" : { "name" : "Belsize Park", "line" : ("N",) },
            "BOR" : { "name" : "Borough", "line" : ("N",) },
            "BTX" : { "name" : "Brent Cross", "line" : ("N",) },
            "BUR" : { "name" : "Burnt Oak", "line" : ("N",) },
            "CTN" : { "name" : "Camden Town", "line" : ("N",) },
            "CHF" : { "name" : "Chalk Farm", "line" : ("N",) },
            "CPC" : { "name" : "Clapham Common", "line" : ("N",) },
            "CPN" : { "name" : "Clapham North", "line" : ("N",) },
            "CPS" : { "name" : "Clapham South", "line" : ("N",) },
            "COL" : { "name" : "Colindale", "line" : ("N",) },
            "CLW" : { "name" : "Colliers Wood", "line" : ("N",) },
            "EFY" : { "name" : "East Finchley", "line" : ("N",) },
            "EDG" : { "name" : "Edgware", "line" : ("N",) },
            "FYC" : { "name" : "Finchley Central", "line" : ("N",) },
            "GGR" : { "name" : "Golders Green", "line" : ("N",) },
            "GST" : { "name" : "Goodge Street", "line" : ("N",) },
            "HMP" : { "name" : "Hampstead", "line" : ("N",) },
            "HND" : { "name" : "Hendon Central", "line" : ("N",) },
            "HBT" : { "name" : "High Barnet", "line" : ("N",) },
            "HIG" : { "name" : "Highgate", "line" : ("N",) },
            "KEN" : { "name" : "Kennington", "line" : ("N",) },
            "KTN" : { "name" : "Kentish Town", "line" : ("N",) },
            "MHE" : { "name" : "Mill Hill East", "line" : ("N",) },
            "MOR" : { "name" : "Morden", "line" : ("N",) },
            "MCR" : { "name" : "Mornington Crescent", "line" : ("N",) },
            "OLD" : { "name" : "Old Street", "line" : ("N",) },
            "OVL" : { "name" : "Oval", "line" : ("N",) },
            "SWM" : { "name" : "South Wimbledon", "line" : ("N",) },
            "TBE" : { "name" : "Tooting Bec", "line" : ("N",) },
            "TBY" : { "name" : "Tooting Broadway", "line" : ("N",) },
            "TCR" : { "name" : "Tottenham Court Road", "line" : ("N",) },
            "TOT" : { "name" : "Totteridge and Whetstone", "line" : ("N",) },
            "TPK" : { "name" : "Tufnell Park", "line" : ("N",) },
            "WST" : { "name" : "Warren Street", "line" : ("N",) },
            "WFY" : { "name" : "West Finchley", "line" : ("N",) },
            "WSP" : { "name" : "Woodside Park", "line" : ("N",) },                
            
            # Piccadilly
            
            "ALP" : { "name" : "Alperton", "line" : ("P",) },
            "AGR" : { "name" : "Arnos Grove", "line" : ("P",) },
            "ARL" : { "name" : "Arsenal", "line" : ("P",) },
            "BCT" : { "name" : "Barons Court", "line" : ("P",) },
            "BOS" : { "name" : "Boston Manor", "line" : ("P",) },
            "BGR" : { "name" : "Bounds Green", "line" : ("P",) },
            "CRD" : { "name" : "Caledonian Road", "line" : ("P",) },
            "CFS" : { "name" : "Cockfosters", "line" : ("P",) },
            "COV" : { "name" : "Covent Garden", "line" : ("P",) },
            "ECT" : { "name" : "Earls Court", "line" : ("P",) },
            "HMD" : { "name" : "Hammersmith (District and Picc)", "line" : ("P",) },
            "HTX" : { "name" : "Hatton Cross", "line" : ("P",) },
            "HRF" : { "name" : "Heathrow Terminal 4", "line" : ("P",) },
            "HRV" : { "name" : "Heathrow Terminal 5", "line" : ("P",) },
            "HRC" : { "name" : "Heathrow Terminals 123", "line" : ("P",) },
            "HRD" : { "name" : "Holloway Road", "line" : ("P",) },
            "HNC" : { "name" : "Hounslow Central", "line" : ("P",) },
            "HNE" : { "name" : "Hounslow East", "line" : ("P",) },
            "HNW" : { "name" : "Hounslow West", "line" : ("P",) },
            "HPC" : { "name" : "Hyde Park Corner", "line" : ("P",) },
            "KNB" : { "name" : "Knightsbridge", "line" : ("P",) },
            "MNR" : { "name" : "Manor House", "line" : ("P",) },
            "NEL" : { "name" : "North Ealing", "line" : ("P",) },
            "NFD" : { "name" : "Northfields", "line" : ("P",) },
            "OAK" : { "name" : "Oakwood", "line" : ("P",) },
            "OST" : { "name" : "Osterley", "line" : ("P",) },
            "PRY" : { "name" : "Park Royal", "line" : ("P",) },
            "PIC" : { "name" : "Piccadilly Circus", "line" : ("P",) },
            "RSQ" : { "name" : "Russell Square", "line" : ("P",) },
            "SEL" : { "name" : "South Ealing", "line" : ("P",) },
            "SHR" : { "name" : "South Harrow", "line" : ("P",) },
            "SGT" : { "name" : "Southgate", "line" : ("P",) },
            "SHL" : { "name" : "Sudbury Hill", "line" : ("P",) },
            "STN" : { "name" : "Sudbury Town", "line" : ("P",) },
            "TGR" : { "name" : "Turnham Green", "line" : ("P",) },
            "TPL" : { "name" : "Turnpike Lane", "line" : ("P",) },
            "WGN" : { "name" : "Wood Green", "line" : ("P",) },
            
            # Victoria
            
            "BHR" : { "name" : "Blackhorse Road", "line" : ("V",) },
            "BRX" : { "name" : "Brixton", "line" : ("V",) },
            "HBY" : { "name" : "Highbury & Islington", "line" : ("V",) },
            "PIM" : { "name" : "Pimlico", "line" : ("V",) },
            "SVS" : { "name" : "Seven Sisters", "line" : ("V",) },
            "TTH" : { "name" : "Tottenham Hale", "line" : ("V",) },
            "VUX" : { "name" : "Vauxhall", "line" : ("V",) },
            "WAL" : { "name" : "Walthamstow Central", "line" : ("V",) },
            "WST" : { "name" : "Warren Street", "line" : ("V",) },                
            
            # Waterloo and City
            
            # DLR
            
            # River Service
            
            }
        
class docs (fakesubwayapis.fakesubwayapidocs, tfl) :

    def __init__ (self) :
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        tfl.__init__(self)
        
    def get (self) :

        stations = self.prepare_stations()
        
        self.display("tfl.html", {'title' : 'tfl', 'stations' : stations})
        return

class api (fakesubwayapis.fakesubwayapi, tfl) :

    def __init__ (self) :

        fakesubwayapis.fakesubwayapi.__init__(self)
        tfl.__init__(self)
        
class getinfo (api) :

    def get (self, station_code, line_code) :

        code = station_code.upper()

        if line_code :
            code = "%s-%s" % (station_code.upper(), line_code.upper())
            
        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')
            return

        data = self.stations[code]

        name = data['name']
        url = None

        lines = data['line'].split(",")
        
        if len(lines) == 1 and lines[0] != '' :
            line_name = self.lines[lines[0]]
        
            url = "http://www.tfl.gov.uk/tfl/livetravelnews/departureboards/tube/default.asp?LineCode=%s&StationCode=%s" % (line_name, station_code.upper())
        
        out = {
            'code' : code,
            'service' : 'tfl',
            'name' :  { '_content' : name },
            'url' : { '_content' : url },
            }
        
        self.api_ok({'station' : out})
        return        
