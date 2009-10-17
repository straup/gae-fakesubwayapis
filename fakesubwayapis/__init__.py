from APIApp import APIApp

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os.path
import types

class fakesubwayapi (APIApp) :

    def __init__ (self) :
        APIApp.__init__(self, 'xml')

class fakesubwayapidocs (webapp.RequestHandler) :

    def get (self) :

        self.display("intro.html")
        return

    def prepare_stations (self, compound_ids_only=False) :

        prepared = []

        codes = self.stations.keys()
        codes.sort()

        for code in codes :

            if code == '' :
                continue

            name = self.stations[code]['name']
                
            if self.stations[code].has_key('line') :

                for ln in self.stations[code]['line'] :

                    line = self.lines[ln]
                    
                    code2 = "%s-%s" % (code, ln)                
                    name2 = "%s (%s line)" % (name, line.capitalize())

                    prepared.append((code2, name2))                    

                if compound_ids_only :
                    continue
                
            prepared.append((code, name))
                
        return prepared
    
    def display (self, template_name, template_values={}) :

        root = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(root, 'templates', template_name)
    
        self.response.out.write(template.render(path, template_values))
