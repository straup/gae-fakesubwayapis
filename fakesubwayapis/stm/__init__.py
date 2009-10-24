# http://www.python.org/dev/peps/pep-0263/
# -*- coding: utf8 -*-

import fakesubwayapis
import unicodedata

class stm :

    def __init__ (self) :

        self.service = {
            'id' : 'stm',
            'name' : 'Société de transport de Montréal',
            'url' : 'http://stm.info/'
            }

        self.url_template = 'http://www.stm.info/metro/%s.htm'
        
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

class dump(stm, fakesubwayapis.fakesubwaystation) :

    def get (self) :

        self.response.out.write("stop_id,stop_name,stop_desc,stop_lat,stop_lon,zone_id,fsa_stop_id,fsa_stop_routes<br />")

        for id, data in self.stations.items() :
            self.response.out.write("%s,\"%s\",,,,,%s<br />" % (id, data['name'], id))
        
class docs (stm, fakesubwayapis.fakesubwayapidocs) :

    def __init__ (self) :

        stm.__init__(self)        
        fakesubwayapis.fakesubwayapidocs.__init__(self)
        
    def get (self) :

        self.show_docs()
        return

class station (stm, fakesubwayapis.fakesubwaystation) :

    def __init__ (self) :

        stm.__init__(self)
        fakesubwayapis.fakesubwaystation.__init__(self)

    def get (self, code) :

        self.do_redirect(code)
        return

class api (stm, fakesubwayapis.fakesubwayapi) :

    def __init__ (self) :

        stm.__init__(self)        
        fakesubwayapis.fakesubwayapi.__init__(self)
        
class getinfo (api) :

    def get (self, code) :

        self.generate_info(code)
        return
