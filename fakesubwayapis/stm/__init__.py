# http://www.python.org/dev/peps/pep-0263/
# -*- coding: utf8 -*-

import fakesubwayapis

class api (fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        fakesubwayapis.fakesubwayapi.__init__(self)
        
        self.stations = {
            "m01" : "Henri-Bourassa",
            "m02" : "Sauvé",
            "m03" : "Crémazie",
            "m04" : "Jarry",
            "m05" : "Jean-Talon",
            "m06" : "Beaubien",
            "m07" : "Rosemont",
            "m08" : "Laurier",
            "m09" : "Mont-Royal",
            "m10" : "Sherbrooke",
            "m11" : "Berri-UQAM",
            "m12" : "Champ-de-Mars",
            "m13" : "Place-d'Armes",
            "m14" : "Square-Victoria",
            "m15" : "Bonaventure",
            "m16" : "Lucien-L'Allier",
            "m17" : "Georges-Vanier",
            "m18" : "Honoré-Beaugrand",
            "m19" : "Radisson",
            "m20" : "Langelier",
            "m21" : "Cadillac",
            "m22" : "Assomption",
            "m23" : "Viau",
            "m24" : "Pie-IX",
            "m25" : "Joliette",
            "m26" : "Préfontaine",
            "m27" : "Frontenac",
            "m28" : "Papineau",
            "m29" : "Beaudry",
            "m30" : "Saint-Laurent",
            "m31" : "Place-des-Arts",
            "m32" : "McGill",
            "m33" : "Peel",
            "m34" : "Guy-Concordia",
            "m35" : "Atwater",
            "m36" : "Lionel-Groulx",
            "m37" : "Charlevoix",
            "m38" : "LaSalle",
            "m39" : "De l'Église",
            "m40" : "Verdun",
            "m41" : "Jolicoeur",
            "m42" : "Monk",
            "m43" : "Angrignon",
            "m44" : "Longueuil",
            "m45" : "Jean-Drapeau",
            "m46" : "Place-Saint-Henri",
            "m47" : "Vendôme",
            "m48" : "Villa-Maria",
            "m49" : "Snowdon",
            "m50" : "Côte-Sainte-Catherine",
            "m51" : "Plamondon",
            "m52" : "Namur",
            "m53" : "De La Savane",
            "m54" : "Du Collège",
            "m55" : "Côte-des-Neiges",
            "m56" : "Université-de-Montréal",
            "m57" : "Édouard-Montpetit",
            "m58" : "Outremont",
            "m59" : "Acadie",
            "m60" : "Parc",
            "m61" : "De Castelnau",
            "m62" : "Fabre",
            "m63" : "D'Iberville",
            "m64" : "Saint-Michel",
            "m65" : "Côte-Vertu",
            "m66" : "Cartier",
            "m67" : "de la Concorde",
            "m68" : "Montmorency",
            }
        
class getinfo (api) :

    def get (self, code) :

        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')
            return

        out = {
            'code' : code,
            'service' : 'stm',
            'name' :  { '_content' : self.stations[code] },
            'url' : { '_content' : 'http://www.stm.info/metro/%s.htm' % code },
            }
        
        self.api_ok({'station' : out})
        return
