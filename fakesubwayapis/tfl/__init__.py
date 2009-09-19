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

            # One day, TFL will have a web page per station...
            # Until then, here are all the connecting stations.
            
            "ACT" : { "name" : "Acton Town", "line" : "" },
            "ALD" : { "name" : "Aldgate", "line" : "" },
            "ALE" : { "name" : "Aldgate East", "line" : "" },            
            "BBB" : { "name" : "Bromley-by-Bow", "line" : "" },
            "BDS" : { "name" : "Bond Street", "line" : "" },
            "BST" : { "name" : "Baker Street", "line" : "" },
            "BNK" : { "name" : "Bank", "line" : "" },
            "BAR" : { "name" : "Barbican", "line" : "" },            
            "BAY" : { "name" : "Bayswater", "line" : "" },
            "BKG" : { "name" : "Barking", "line" : "" },
            "BLF" : { "name" : "Blackfriars", "line" : "" },
            "BWR" : { "name" : "Bow Road", "line" : "" },
            "CHX" : { "name" : "Charing Cross", "line" : "" },
            "CST" : { "name" : "Cannon Street", "line" : "" },            
            "EBY" : { "name" : "Ealing Broadway", "line" : "" },
            "ECM" : { "name" : "Ealing Common", "line" : "" },
            "EHM" : { "name" : "East Ham", "line" : "" },
            "ELE" : { "name" : "Elephant & Castle", "line" : "" },
            "EMB" : { "name" : "Embankment", "line" : "" },
            "ERB" : { "name" : "Edgware Road", "line" : "" },                        
            "ESQ" : { "name" : "Euston Square", "line" : "" },
            "ETE" : { "name" : "Eastcote", "line" : "" },
            "EUS" : { "name" : "Euston", "line" : "" },
            "FAR" : { "name" : "Farringdon", "line" : "" },            
            "FPK" : { "name" : "Finsbury Park", "line" : "" },
            "GRD" : { "name" : "Gloucester Road", "line" : "" },            
            "GPK" : { "name" : "Green Park", "line" : "" },
            "GPS" : { "name" : "Great Portland Street", "line" : "" },
            "HST" : { "name" : "High Street Kensington", "line" : "" },            
            "HDN" : { "name" : "Hillingdon", "line" : "" },
            "HOL" : { "name" : "Holborn", "line" : "" },
            "ICK" : { "name" : "Ickenham", "line" : "" },
            "KXX" : { "name" : "King's Cross St. Pancras", "line" : "" },
            "LON" : { "name" : "London Bridge", "line" : "" },
            "LSQ" : { "name" : "Leicester Square", "line" : "" },                        
            "LST" : { "name" : "Liverpool Street", "line" : "" },
            "MAN" : { "name" : "Mansion House", "line" : "" },
            "MLE" : { "name" : "Mile End", "line" : "" },
            "MON" : { "name" : "Monument", "line" : "" },
            "MGT" : { "name" : "Moorgate", "line" : "" },            
            "NHG" : { "name" : "Notting Hill Gate", "line" : "" },
            "OXC" : { "name" : "Oxford Circus", "line" : "" },            
            "RLN" : { "name" : "Rayners Lane", "line" : "P" },
            "RUI" : { "name" : "Ruislip", "line" : "" },
            "RUM" : { "name" : "Ruislip Manor", "line" : "" },
            "SFD" : { "name" : "Stratford", "line" : "" },
            "SSQ" : { "name" : "Sloane Square", "line" : "" },            
            "SKN" : { "name" : "South Kensington", "line" : "" },
            "SJP" : { "name" : "St. James's Park", "line" : "" },            
            "STG" : { "name" : "Stepney Green", "line" : "" },
            "STK" : { "name" : "Stockwell", "line" : "" },
            "VIC" : { "name" : "Victoria", "line" : "" },
            "TEM" : { "name" : "Temple", "line" : "" },
            "THL" : { "name" : "Tower Hill", "line" : "" },
            "UPK" : { "name" : "Upton Park", "line" : "" },            
            "UXB" : { "name" : "Uxbridge", "line" : "" },
            "WCL" : { "name" : "Whitechapel", "line" : "" },
            "WHM" : { "name" : "West Ham", "line" : "" },
            "WLO" : { "name" : "Waterloo", "line" : "" },
            "WMS" : { "name" : "Westminster", "line" : "" },            
            
            # Bakerloo
            
            "BST-B" : { "name" : "Baker Street", "line" : "B" },            
            "CHX-B" : { "name" : "Charing Cross", "line" : "B" },
            "ERB-B" : { "name" : "Edgware Road (Bakerloo)", "line" : "B" },
            "ELE-B" : { "name" : "Elephant & Castle", "line" : "B" },
            "EMB-B" : { "name" : "Embankment", "line" : "B" },            
            "HSD" : { "name" : "Harlesden", "line" : "B" },
            "HAW" : { "name" : "Harrow & Wealdstone", "line" : "B" },
            "KGN" : { "name" : "Kensal Green", "line" : "B" },
            "KNT" : { "name" : "Kenton", "line" : "B" },
            "KPK" : { "name" : "Kilburn Park", "line" : "B" },
            "LAM" : { "name" : "Lambeth North", "line" : "B" },
            "MDV" : { "name" : "Maida Vale", "line" : "B" },
            "MYB" : { "name" : "Marylebone", "line" : "B" },
            "NWM" : { "name" : "North Wembley", "line" : "B" },
            "OXC-B" : { "name" : "Oxford Circus", "line" : "B" },
            "PAD" : { "name" : "Paddington", "line" : "B" },
            "PIC" : { "name" : "Piccadilly Circus", "line" : "B" },
            "QPK" : { "name" : "Queen's Park", "line" : "B" },
            "RPK" : { "name" : "Regent's Park", "line" : "B" },
            "SKT" : { "name" : "South Kenton", "line" : "B" },
            "SPK" : { "name" : "Stonebridge Park", "line" : "B" },
            "WAR" : { "name" : "Warwick Avenue", "line" : "B" },
            "WLO-B" : { "name" : "Waterloo", "line" : "B" },
            "WEM" : { "name" : "Wembley Central", "line" : "B" },
            "WJN" : { "name" : "Willesden Junction", "line" : "B" },

            # Central
            
            "BNK-C" : { "name" : "Bank", "line" : "C" },
            "BDE" : { "name" : "Barkingside", "line" : "C" },
            "BNG" : { "name" : "Bethnal Green", "line" : "C" },
            "BDS-C" : { "name" : "Bond Street", "line" : "C" },
            "BHL" : { "name" : "Buckhurst Hill", "line" : "C" },
            "CYL" : { "name" : "Chancery Lane", "line" : "C" },
            "CHG" : { "name" : "Chigwell", "line" : "C" },
            "DEB" : { "name" : "Debden", "line" : "C" },
            "EBY-C" : { "name" : "Ealing Broadway", "line" : "C" },
            "EAC" : { "name" : "East Acton", "line" : "C" },
            "EPP" : { "name" : "Epping", "line" : "C" },
            "FLP" : { "name" : "Fairlop", "line" : "C" },
            "GHL" : { "name" : "Gants Hill", "line" : "C" },
            "GRH" : { "name" : "Grange Hill", "line" : "C" },
            "GFD" : { "name" : "Greenford", "line" : "C" },
            "HAI" : { "name" : "Hainault", "line" : "C" },
            "HLN" : { "name" : "Hanger Lane", "line" : "C" },
            "HOL-C" : { "name" : "Holborn", "line" : "C" },
            "HPK" : { "name" : "Holland Park", "line" : "C" },
            "LAN" : { "name" : "Lancaster Gate", "line" : "C" },
            "LEY" : { "name" : "Leyton", "line" : "C" },
            "LYS" : { "name" : "Leytonstone", "line" : "C" },
            "LST-C" : { "name" : "Liverpool Street", "line" : "C" },
            "LTN" : { "name" : "Loughton", "line" : "C" },
            "MAR" : { "name" : "Marble Arch", "line" : "C" },
            "CMLE" : { "name" : "Mile End", "line" : "C" },
            "NEP" : { "name" : "Newbury Park", "line" : "C" },
            "NAC" : { "name" : "North Acton", "line" : "C" },
            "NHT" : { "name" : "Northolt", "line" : "C" },
            "NHG-C" : { "name" : "Notting Hill Gate", "line" : "C" },
            "OXC-C" : { "name" : "Oxford Circus", "line" : "C" },
            "PER" : { "name" : "Perivale", "line" : "C" },
            "QWY" : { "name" : "Queensway", "line" : "C" },
            "RED" : { "name" : "Redbridge", "line" : "C" },
            "ROD" : { "name" : "Roding Valley", "line" : "C" },
            "RUG" : { "name" : "Ruislip Gardens", "line" : "C" },
            "SBC" : { "name" : "Shepherds Bush (Central Line)", "line" : "C" },
            "SNB" : { "name" : "Snaresbrook", "line" : "C" },
            "SRP" : { "name" : "South Ruislip", "line" : "C" },
            "SWF" : { "name" : "South Woodford", "line" : "C" },
            "STP" : { "name" : "St. Paul's", "line" : "C" },
            "SFD-C" : { "name" : "Stratford", "line" : "C" },
            "THB" : { "name" : "Theydon Bois", "line" : "C" },
            "TCR" : { "name" : "Tottenham Court Road", "line" : "C" },
            "WAN" : { "name" : "Wanstead", "line" : "C" },
            "WAC" : { "name" : "West Acton", "line" : "C" },
            "WRP" : { "name" : "West Ruislip", "line" : "C" },
            "WCT" : { "name" : "White City", "line" : "C" },
            "WFD" : { "name" : "Woodford", "line" : "C" },
            
            # Circle
                 
            "ALD-O" : { "name" : "Aldgate", "line" : "O" },
            "ALE-O" : { "name" : "Aldgate East", "line" : "O" },
            "BST-O" : { "name" : "Baker Street", "line" : "O" },            
            "BAR-O" : { "name" : "Barbican", "line" : "O" },
            "BKG-O" : { "name" : "Barking", "line" : "O" },
            "BAY-O" : { "name" : "Bayswater", "line" : "O" },
            "BLF-O" : { "name" : "Blackfriars", "line" : "O" },
            "BWR-O" : { "name" : "Bow Road", "line" : "O" },
            "BBB-O" : { "name" : "Bromley-by-Bow", "line" : "O" },
            "CST-O" : { "name" : "Cannon Street", "line" : "O" },
            "EHM-O" : { "name" : "East Ham", "line" : "O" },
            "ERD-O" : { "name" : "Edgware Road (H & C)", "line" : "O" },
            "EMB-O" : { "name" : "Embankment", "line" : "O" },            
            "ESQ-O" : { "name" : "Euston Square", "line" : "O" },
            "FAR-O" : { "name" : "Farringdon", "line" : "O" },
            "GRD-O" : { "name" : "Gloucester Road", "line" : "O" },
            "GPS-O" : { "name" : "Great Portland Street", "line" : "O" },
            "HMS" : { "name" : "Hammersmith (Circle and H&C)", "line" : "O" },
            "HST-O" : { "name" : "High Street Kensington", "line" : "O" },
            "KXX-O" : { "name" : "King's Cross St. Pancras", "line" : "O" },
            "LBG" : { "name" : "Ladbroke Grove", "line" : "O" },
            "LST-O" : { "name" : "Liverpool Street", "line" : "O" },
            "MAN-O" : { "name" : "Mansion House", "line" : "O" },
            "MLE-O" : { "name" : "Mile End", "line" : "O" },
            "MON-O" : { "name" : "Monument", "line" : "O" },
            "MGT-O" : { "name" : "Moorgate", "line" : "O" },
            "NHG-O" : { "name" : "Notting Hill Gate", "line" : "O" },
            "PADc" : { "name" : "Paddington Circle", "line" : "O" },
            "PADs" : { "name" : "Paddington H & C", "line" : "O" },
            "PLW" : { "name" : "Plaistow", "line" : "O" },
            "ROA" : { "name" : "Royal Oak", "line" : "O" },
            "SSQ-O" : { "name" : "Sloane Square", "line" : "O" },
            "SKN-O" : { "name" : "South Kensington", "line" : "O" },
            "SJP-O" : { "name" : "St. James's Park", "line" : "O" },
            "STG-O" : { "name" : "Stepney Green", "line" : "O" },
            "TEM-O" : { "name" : "Temple", "line" : "O" },
            "THL-O" : { "name" : "Tower Hill", "line" : "O" },
            "UPK-O" : { "name" : "Upton Park", "line" : "O" },
            "VIC-O" : { "name" : "Victoria", "line" : "O" },
            "WHM-O" : { "name" : "West Ham", "line" : "O" },
            "WBP" : { "name" : "Westbourne Park", "line" : "O" },
            "WMS-O" : { "name" : "Westminster", "line" : "O" },
            "WCL-O" : { "name" : "Whitechapel", "line" : "O" },

            # District

            "ACT-D" : { "name" : "Acton Town", "line" : "D" },            
            "ALE-D" : { "name" : "Aldgate East", "line" : "D" },
            "BKG-D" : { "name" : "Barking", "line" : "D" },
            "BCT" : { "name" : "Barons Court", "line" : "D" },
            "BEC" : { "name" : "Becontree", "line" : "D" },
            "BLF-D" : { "name" : "Blackfriars", "line" : "D" },
            "BWR-D" : { "name" : "Bow Road", "line" : "D" },
            "BBB-D" : { "name" : "Bromley-by-Bow", "line" : "D" },
            "DCST" : { "name" : "Cannon Street", "line" : "D" },
            "CHP" : { "name" : "Chiswick Park", "line" : "D" },
            "DGE" : { "name" : "Dagenham East", "line" : "D" },
            "DGH" : { "name" : "Dagenham Heathway", "line" : "D" },
            "EBY-D" : { "name" : "Ealing Broadway", "line" : "D" },
            "ECM-D" : { "name" : "Ealing Common", "line" : "D" },            
            "ECT" : { "name" : "Earls Court", "line" : "D" },
            "EHM-D" : { "name" : "East Ham", "line" : "D" },
            "EPY" : { "name" : "East Putney", "line" : "D" },
            "ERD-D" : { "name" : "Edgware Road (H & C)", "line" : "D" },
            "EPK" : { "name" : "Elm Park", "line" : "D" },
            "EMB-D" : { "name" : "Embankment", "line" : "D" },            
            "FBY" : { "name" : "Fulham Broadway", "line" : "D" },
            "GRD-D" : { "name" : "Gloucester Road", "line" : "D" },
            "GUN" : { "name" : "Gunnersbury", "line" : "D" },
            "HMD" : { "name" : "Hammersmith (District and Picc)", "line" : "D" },
            "HST-D" : { "name" : "High Street Kensington", "line" : "D" },
            "HCH" : { "name" : "Hornchurch", "line" : "D" },
            "KEW" : { "name" : "Kew Gardens", "line" : "D" },
            "MAN-D" : { "name" : "Mansion House", "line" : "D" },
            "MLE-D" : { "name" : "Mile End", "line" : "D" },
            "MON-D" : { "name" : "Monument", "line" : "D" },
            "OLY" : { "name" : "Olympia", "line" : "D" },
            "PGR" : { "name" : "Parsons Green", "line" : "D" },
            "PLW" : { "name" : "Plaistow", "line" : "D" },
            "PUT" : { "name" : "Putney Bridge", "line" : "D" },
            "RCP" : { "name" : "Ravenscourt Park", "line" : "D" },
            "RMD" : { "name" : "Richmond", "line" : "D" },
            "SSQ-D" : { "name" : "Sloane Square", "line" : "D" },
            "SFS" : { "name" : "Southfields", "line" : "D" },
            "SKN-D" : { "name" : "South Kensington", "line" : "D" },
            "SJP-D" : { "name" : "St. James's Park", "line" : "D" },
            "STB" : { "name" : "Stamford Brook", "line" : "D" },
            "STG-D" : { "name" : "Stepney Green", "line" : "D" },
            "TEM-D" : { "name" : "Temple", "line" : "D" },
            "THL-D" : { "name" : "Tower Hill", "line" : "D" },
            "TGR" : { "name" : "Turnham Green", "line" : "D" },
            "UPM" : { "name" : "Upminster", "line" : "D" },
            "UPB" : { "name" : "Upminster Bridge", "line" : "D" },
            "UPY" : { "name" : "Upney", "line" : "D" },
            "UPK-D" : { "name" : "Upton Park", "line" : "D" },
            "VIC-D" : { "name" : "Victoria", "line" : "D" },
            "WBT" : { "name" : "West Brompton", "line" : "D" },
            "WHM-D" : { "name" : "West Ham", "line" : "D" },
            "WKN" : { "name" : "West Kensington", "line" : "D" },
            "WMS-D" : { "name" : "Westminster", "line" : "D" },
            "WCL-D" : { "name" : "Whitechapel", "line" : "D" },
            "WDN" : { "name" : "Wimbledon", "line" : "D" },
            "WMP" : { "name" : "Wimbledon Park", "line" : "D" },
            
            # Hammersmith and City

            "ALD-H" : { "name" : "Aldgate", "line" : "H" },
            "ALE-H" : { "name" : "Aldgate East", "line" : "H" },
            "BST-H" : { "name" : "Baker Street", "line" : "H" },            
            "BAR-H" : { "name" : "Barbican", "line" : "H" },
            "BKG-H" : { "name" : "Barking", "line" : "H" },
            "BAY-H" : { "name" : "Bayswater", "line" : "H" },
            "BLF-H" : { "name" : "Blackfriars", "line" : "H" },
            "BWR-H" : { "name" : "Bow Road", "line" : "H" },
            "BBB-H" : { "name" : "Bromley-by-Bow", "line" : "H" },
            "CST-H" : { "name" : "Cannon Street", "line" : "H" },
            "EHM-H" : { "name" : "East Ham", "line" : "H" },
            "ERD" : { "name" : "Edgware Road (H & C)", "line" : "H" },
            "EMB-H" : { "name" : "Embankment", "line" : "H" },            
            "ESQ-H" : { "name" : "Euston Square", "line" : "H" },
            "FAR-H" : { "name" : "Farringdon", "line" : "H" },
            "GRD-H" : { "name" : "Gloucester Road", "line" : "H" },
            "GPS-H" : { "name" : "Great Portland Street", "line" : "H" },
            "HMS" : { "name" : "Hammersmith (Circle and H&C)", "line" : "H" },
            "HST-H" : { "name" : "High Street Kensington", "line" : "H" },
            "KXX-H" : { "name" : "King's Cross St. Pancras", "line" : "H" },
            "LBG" : { "name" : "Ladbroke Grove", "line" : "H" },
            "LST-H" : { "name" : "Liverpool Street", "line" : "H" },
            "MAN-H" : { "name" : "Mansion House", "line" : "H" },
            "MLE-H" : { "name" : "Mile End", "line" : "H" },
            "MON-H" : { "name" : "Monument", "line" : "H" },
            "MGT-H" : { "name" : "Moorgate", "line" : "H" },
            "NHG-H" : { "name" : "Notting Hill Gate", "line" : "H" },
            "PADc" : { "name" : "Paddington Circle", "line" : "H" },
            "PADs" : { "name" : "Paddington H & C", "line" : "H" },
            "PLW" : { "name" : "Plaistow", "line" : "H" },
            "ROA" : { "name" : "Royal Oak", "line" : "H" },
            "SSQ-H" : { "name" : "Sloane Square", "line" : "H" },
            "SKN-H" : { "name" : "South Kensington", "line" : "H" },
            "SJP-H" : { "name" : "St. James's Park", "line" : "H" },
            "STG-H" : { "name" : "Stepney Green", "line" : "H" },
            "TEM-H" : { "name" : "Temple", "line" : "H" },
            "THL-H" : { "name" : "Tower Hill", "line" : "H" },
            "UPK-H" : { "name" : "Upton Park", "line" : "H" },
            "VIC-H" : { "name" : "Victoria", "line" : "H" },
            "WHM-H" : { "name" : "West Ham", "line" : "H" },
            "WBP" : { "name" : "Westbourne Park", "line" : "H" },
            "WMS-H" : { "name" : "Westminster", "line" : "H" },
            "WCL-H" : { "name" : "Whitechapel", "line" : "H" },
            
            # Jubilee
            
            "BST-J" : { "name" : "Baker Street", "line" : "J" },            
            "BER" : { "name" : "Bermondsey", "line" : "J" },
            "BDS-J" : { "name" : "Bond Street", "line" : "J" },
            "CWR" : { "name" : "Canada Water", "line" : "J" },
            "CWF" : { "name" : "Canary Wharf", "line" : "J" },
            "CNT" : { "name" : "Canning Town", "line" : "J" },
            "CPK" : { "name" : "Canons Park", "line" : "J" },
            "CHX-J" : { "name" : "Charing Cross", "line" : "J" },
            "DHL" : { "name" : "Dollis Hill", "line" : "J" },
            "FRD" : { "name" : "Finchley Road", "line" : "J" },
            "GPK-J" : { "name" : "Green Park", "line" : "J" },
            "KIL" : { "name" : "Kilburn", "line" : "J" },
            "KBY" : { "name" : "Kingsbury", "line" : "J" },
            "LON-J" : { "name" : "London Bridge", "line" : "J" },
            "NEA" : { "name" : "Neasden", "line" : "J" },
            "NGW" : { "name" : "North Greenwich", "line" : "J" },
            "QBY" : { "name" : "Queensbury", "line" : "J" },
            "SWK" : { "name" : "Southwark", "line" : "J" },
            "SJW" : { "name" : "St. John's Wood", "line" : "J" },
            "STA" : { "name" : "Stanmore", "line" : "J" },
            "SFD-J" : { "name" : "Stratford", "line" : "J" },
            "SWC" : { "name" : "Swiss Cottage", "line" : "J" },
            "WLO-J" : { "name" : "Waterloo", "line" : "J" },
            "WPK" : { "name" : "Wembley Park", "line" : "J" },
            "WHM-J" : { "name" : "West Ham", "line" : "J" },
            "WHD" : { "name" : "West Hampstead", "line" : "J" },
            "WMS-J" : { "name" : "Westminster", "line" : "J" },
            "WLG" : { "name" : "Willesden Green", "line" : "J" },
            
            # Metropolitain
            
            "ALD-M" : { "name" : "Aldgate", "line" : "M" },
            "AME" : { "name" : "Amersham", "line" : "M" },
            "BST-M" : { "name" : "Baker Street", "line" : "M" },            
            "BAR-M" : { "name" : "Barbican", "line" : "M" },
            "CLF" : { "name" : "Chalfont & Latimer", "line" : "M" },
            "CWD" : { "name" : "Chorleywood", "line" : "M" },
            "CRX" : { "name" : "Croxley", "line" : "M" },
            "ETE-M" : { "name" : "Eastcote", "line" : "M" },
            "ESQ-M" : { "name" : "Euston Square", "line" : "M" },
            "FAR-M" : { "name" : "Farringdon", "line" : "M" },
            "FRD" : { "name" : "Finchley Road", "line" : "M" },
            "GPS-M" : { "name" : "Great Portland Street", "line" : "M" },
            "HOH" : { "name" : "Harrow on the Hill", "line" : "M" },
            "HDN-M" : { "name" : "Hillingdon", "line" : "M" },
            "ICK-M" : { "name" : "Ickenham", "line" : "M" },
            "KXX-M" : { "name" : "King's Cross St. Pancras", "line" : "M" },
            "LST-M" : { "name" : "Liverpool Street", "line" : "M" },
            "MPK" : { "name" : "Moor Park", "line" : "M" },
            "MGT-M" : { "name" : "Moorgate", "line" : "M" },
            "NHR" : { "name" : "North Harrow", "line" : "M" },
            "NWP" : { "name" : "Northwick Park", "line" : "M" },
            "NWD" : { "name" : "Northwood", "line" : "M" },
            "NWH" : { "name" : "Northwood Hills", "line" : "M" },
            "PIN" : { "name" : "Pinner", "line" : "M" },
            "RLN" : { "name" : "Rayners Lane", "line" : "M" },
            "RLN-M" : { "name" : "Rayners Lane", "line" : "M" },            
            "RKY" : { "name" : "Rickmansworth", "line" : "M" },
            "RUI-M" : { "name" : "Ruislip", "line" : "M" },
            "RUM-M" : { "name" : "Ruislip Manor", "line" : "M" },
            "UXB-M" : { "name" : "Uxbridge", "line" : "M" },
            "WAT" : { "name" : "Watford", "line" : "M" },
            "WPK" : { "name" : "Wembley Park", "line" : "M" },
            "WHR" : { "name" : "West Harrow", "line" : "M" },
            "WCL-M" : { "name" : "Whitechapel", "line" : "M" },
            "WSP" : { "name" : "Woodside Park", "line" : "M" },
            
            # Northern

            "ANG" : { "name" : "Angel", "line" : "N" },
            "ARC" : { "name" : "Archway", "line" : "N" },
            "BAL" : { "name" : "Balham", "line" : "N" },
            "BNK-N" : { "name" : "Bank", "line" : "N" },
            "BPK" : { "name" : "Belsize Park", "line" : "N" },
            "BOR" : { "name" : "Borough", "line" : "N" },
            "BTX" : { "name" : "Brent Cross", "line" : "N" },
            "BUR" : { "name" : "Burnt Oak", "line" : "N" },
            "CTN" : { "name" : "Camden Town", "line" : "N" },
            "CHF" : { "name" : "Chalk Farm", "line" : "N" },
            "CHX-N" : { "name" : "Charing Cross", "line" : "N" },
            "CPC" : { "name" : "Clapham Common", "line" : "N" },
            "CPN" : { "name" : "Clapham North", "line" : "N" },
            "CPS" : { "name" : "Clapham South", "line" : "N" },
            "COL" : { "name" : "Colindale", "line" : "N" },
            "CLW" : { "name" : "Colliers Wood", "line" : "N" },
            "EFY" : { "name" : "East Finchley", "line" : "N" },
            "EDG" : { "name" : "Edgware", "line" : "N" },
            "ELE-N" : { "name" : "Elephant & Castle", "line" : "N" },
            "EMB-N" : { "name" : "Embankment", "line" : "N" },            
            "EUS-N" : { "name" : "Euston", "line" : "N" },
            "FYC" : { "name" : "Finchley Central", "line" : "N" },
            "GGR" : { "name" : "Golders Green", "line" : "N" },
            "GST" : { "name" : "Goodge Street", "line" : "N" },
            "HMP" : { "name" : "Hampstead", "line" : "N" },
            "HND" : { "name" : "Hendon Central", "line" : "N" },
            "HBT" : { "name" : "High Barnet", "line" : "N" },
            "HIG" : { "name" : "Highgate", "line" : "N" },
            "KEN" : { "name" : "Kennington", "line" : "N" },
            "KTN" : { "name" : "Kentish Town", "line" : "N" },
            "KXX-N" : { "name" : "King's Cross St. Pancras", "line" : "N" },
            "LSQ-N" : { "name" : "Leicester Square", "line" : "N" },
            "LON-N" : { "name" : "London Bridge", "line" : "N" },
            "MHE" : { "name" : "Mill Hill East", "line" : "N" },
            "MGT-N" : { "name" : "Moorgate", "line" : "N" },
            "MOR" : { "name" : "Morden", "line" : "N" },
            "MCR" : { "name" : "Mornington Crescent", "line" : "N" },
            "OLD" : { "name" : "Old Street", "line" : "N" },
            "OVL" : { "name" : "Oval", "line" : "N" },
            "SWM" : { "name" : "South Wimbledon", "line" : "N" },
            "STK-N" : { "name" : "Stockwell", "line" : "N" },
            "TBE" : { "name" : "Tooting Bec", "line" : "N" },
            "TBY" : { "name" : "Tooting Broadway", "line" : "N" },
            "TCR" : { "name" : "Tottenham Court Road", "line" : "N" },
            "TOT" : { "name" : "Totteridge and Whetstone", "line" : "N" },
            "TPK" : { "name" : "Tufnell Park", "line" : "N" },
            "WST" : { "name" : "Warren Street", "line" : "N" },
            "WLO-N" : { "name" : "Waterloo", "line" : "N" },
            "WFY" : { "name" : "West Finchley", "line" : "N" },
            "WSP" : { "name" : "Woodside Park", "line" : "N" },                
            
            # Piccadilly
            
            "ACT-P" : { "name" : "Acton Town", "line" : "P" },            
            "ALP" : { "name" : "Alperton", "line" : "P" },
            "AGR" : { "name" : "Arnos Grove", "line" : "P" },
            "ARL" : { "name" : "Arsenal", "line" : "P" },
            "BCT" : { "name" : "Barons Court", "line" : "P" },
            "BOS" : { "name" : "Boston Manor", "line" : "P" },
            "BGR" : { "name" : "Bounds Green", "line" : "P" },
            "CRD" : { "name" : "Caledonian Road", "line" : "P" },
            "CFS" : { "name" : "Cockfosters", "line" : "P" },
            "COV" : { "name" : "Covent Garden", "line" : "P" },
            "ECM-P" : { "name" : "Ealing Common", "line" : "P" },            
            "ECT" : { "name" : "Earls Court", "line" : "P" },
            "ETE-P" : { "name" : "Eastcote", "line" : "P" },
            "FPK-P" : { "name" : "Finsbury Park", "line" : "P" },
            "GRD-P" : { "name" : "Gloucester Road", "line" : "P" },
            "GPK-P" : { "name" : "Green Park", "line" : "P" },
            "HMD" : { "name" : "Hammersmith (District and Picc)", "line" : "P" },
            "HTX" : { "name" : "Hatton Cross", "line" : "P" },
            "HRF" : { "name" : "Heathrow Terminal 4", "line" : "P" },
            "HRV" : { "name" : "Heathrow Terminal 5", "line" : "P" },
            "HRC" : { "name" : "Heathrow Terminals 123", "line" : "P" },
            "HDN-P" : { "name" : "Hillingdon", "line" : "P" },
            "HOL-P" : { "name" : "Holborn", "line" : "P" },
            "HRD" : { "name" : "Holloway Road", "line" : "P" },
            "HNC" : { "name" : "Hounslow Central", "line" : "P" },
            "HNE" : { "name" : "Hounslow East", "line" : "P" },
            "HNW" : { "name" : "Hounslow West", "line" : "P" },
            "HPC" : { "name" : "Hyde Park Corner", "line" : "P" },
            "ICK-P" : { "name" : "Ickenham", "line" : "P" },
            "KXX-P" : { "name" : "King's Cross St. Pancras", "line" : "P" },
            "KNB" : { "name" : "Knightsbridge", "line" : "P" },
            "LSQ-P" : { "name" : "Leicester Square", "line" : "P" },
            "MNR" : { "name" : "Manor House", "line" : "P" },
            "NEL" : { "name" : "North Ealing", "line" : "P" },
            "NFD" : { "name" : "Northfields", "line" : "P" },
            "OAK" : { "name" : "Oakwood", "line" : "P" },
            "OST" : { "name" : "Osterley", "line" : "P" },
            "PRY" : { "name" : "Park Royal", "line" : "P" },
            "PIC" : { "name" : "Piccadilly Circus", "line" : "P" },
            "RLN-P" : { "name" : "Rayners Lane", "line" : "P" },            
            "RUI-P" : { "name" : "Ruislip", "line" : "P" },
            "RUM-P" : { "name" : "Ruislip Manor", "line" : "P" },
            "RSQ" : { "name" : "Russell Square", "line" : "P" },
            "SEL" : { "name" : "South Ealing", "line" : "P" },
            "SHR" : { "name" : "South Harrow", "line" : "P" },
            "SKN-P" : { "name" : "South Kensington", "line" : "P" },
            "SGT" : { "name" : "Southgate", "line" : "P" },
            "SHL" : { "name" : "Sudbury Hill", "line" : "P" },
            "STN" : { "name" : "Sudbury Town", "line" : "P" },
            "TGR" : { "name" : "Turnham Green", "line" : "P" },
            "TPL" : { "name" : "Turnpike Lane", "line" : "P" },
            "UXB-P" : { "name" : "Uxbridge", "line" : "P" },
            "WGN" : { "name" : "Wood Green", "line" : "P" },
            
            # Victoria
            
            "BHR" : { "name" : "Blackhorse Road", "line" : "V" },
            "BRX" : { "name" : "Brixton", "line" : "V" },
            "EUS-V" : { "name" : "Euston", "line" : "V" },
            "FPK-V" : { "name" : "Finsbury Park", "line" : "V" },
            "GPK-V" : { "name" : "Green Park", "line" : "V" },
            "HBY" : { "name" : "Highbury & Islington", "line" : "V" },
            "KXX-V" : { "name" : "King's Cross St. Pancras", "line" : "V" },
            "OXC-V" : { "name" : "Oxford Circus", "line" : "V" },
            "PIM" : { "name" : "Pimlico", "line" : "V" },
            "SVS" : { "name" : "Seven Sisters", "line" : "V" },
            "STK-V" : { "name" : "Stockwell", "line" : "V" },
            "TTH" : { "name" : "Tottenham Hale", "line" : "V" },
            "VUX" : { "name" : "Vauxhall", "line" : "V" },
            "VIC-V" : { "name" : "Victoria", "line" : "V" },
            "WAL" : { "name" : "Walthamstow Central", "line" : "V" },
            "WST" : { "name" : "Warren Street", "line" : "V" },                
            
            # Waterloo and City
            
            "BNK-W" : { "name" : "Bank", "line" : "W" },
            "WLO-W" : { "name" : "Waterloo", "line" : "W" },

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
