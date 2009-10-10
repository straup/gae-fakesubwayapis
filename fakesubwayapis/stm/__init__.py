# http://www.python.org/dev/peps/pep-0263/
# -*- coding: utf8 -*-

import fakesubwayapis

class stm :

    def __init__ (self) :

        self.stations = {
            "m01" : { "name" : "Henri-Bourassa" },
            "m02" : { "name" : "Sauvé" },
            "m03" : { "name" : "Crémazie" },
            "m04" : { "name" : "Jarry" },
            "m05" : { "name" : "Jean-Talon" },
            "m06" : { "name" : "Beaubien" },
            "m07" : { "name" : "Rosemont" },
            "m08" : { "name" : "Laurier" },
            "m09" : { "name" : "Mont-Royal" },
            "m10" : { "name" : "Sherbrooke" },
            "m11" : { "name" : "Berri-UQAM" },
            "m12" : { "name" : "Champ-de-Mars" },
            "m13" : { "name" : "Place-d'Armes" },
            "m14" : { "name" : "Square-Victoria" },
            "m15" : { "name" : "Bonaventure" },
            "m16" : { "name" : "Lucien-L'Allier" },
            "m17" : { "name" : "Georges-Vanier" },
            "m18" : { "name" : "Honoré-Beaugrand" },
            "m19" : { "name" : "Radisson" },
            "m20" : { "name" : "Langelier" },
            "m21" : { "name" : "Cadillac" },
            "m22" : { "name" : "Assomption" },
            "m23" : { "name" : "Viau" },
            "m24" : { "name" : "Pie-IX" },
            "m25" : { "name" : "Joliette" },
            "m26" : { "name" : "Préfontaine" },
            "m27" : { "name" : "Frontenac" },
            "m28" : { "name" : "Papineau" },
            "m29" : { "name" : "Beaudry" },
            "m30" : { "name" : "Saint-Laurent" },
            "m31" : { "name" : "Place-des-Arts" },
            "m32" : { "name" : "McGill" },
            "m33" : { "name" : "Peel" },
            "m34" : { "name" : "Guy-Concordia" },
            "m35" : { "name" : "Atwater" },
            "m36" : { "name" : "Lionel-Groulx" },
            "m37" : { "name" : "Charlevoix" },
            "m38" : { "name" : "LaSalle" },
            "m39" : { "name" : "De l'Église" },
            "m40" : { "name" : "Verdun" },
            "m41" : { "name" : "Jolicoeur" },
            "m42" : { "name" : "Monk" },
            "m43" : { "name" : "Angrignon" },
            "m44" : { "name" : "Longueuil" },
            "m45" : { "name" : "Jean-Drapeau" },
            "m46" : { "name" : "Place-Saint-Henri" },
            "m47" : { "name" : "Vendôme" },
            "m48" : { "name" : "Villa-Maria" },
            "m49" : { "name" : "Snowdon" },
            "m50" : { "name" : "Côte-Sainte-Catherine" },
            "m51" : { "name" : "Plamondon" },
            "m52" : { "name" : "Namur" },
            "m53" : { "name" : "De La Savane" },
            "m54" : { "name" : "Du Collège" },
            "m55" : { "name" : "Côte-des-Neiges" },
            "m56" : { "name" : "Université-de-Montréal" },
            "m57" : { "name" : "Édouard-Montpetit" },
            "m58" : { "name" : "Outremont" },
            "m59" : { "name" : "Acadie" },
            "m60" : { "name" : "Parc" },
            "m61" : { "name" : "De Castelnau" },
            "m62" : { "name" : "Fabre" },
            "m63" : { "name" : "D'Iberville" },
            "m64" : { "name" : "Saint-Michel" },
            "m65" : { "name" : "Côte-Vertu" },
            "m66" : { "name" : "Cartier" },
            "m67" : { "name" : "de la Concorde" },
            "m68" : { "name" : "Montmorency" },
            }
        
class docs (fakesubwayapis.fakesubwayapidocs, stm) :

    def __init__ (self) :
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        stm.__init__(self)
        
    def get (self) :

        stations = self.prepare_stations()
        
        self.display("stm.html", {'title' : 'stm', 'stations' : stations})
        return

class api (fakesubwayapis.fakesubwayapi, stm) :

    def __init__ (self) :
        fakesubwayapis.fakesubwayapi.__init__(self)
        stm.__init__(self)
        
class getinfo (api) :

    def get (self, code) :

        if not self.stations.has_key(code) :
            self.api_error(404, 'Station not found')
            return

        out = {
            'code' : code,
            'service' : 'stm',
            'name' :  { '_content' : self.stations[code]['name'] },
            'url' : { '_content' : 'http://www.stm.info/metro/%s.htm' % code },
            }
        
        self.api_ok({'station' : out})
        return
