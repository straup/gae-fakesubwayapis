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

    def prepare_stations (self) :

        prepared = []

        codes = self.stations.keys()
        codes.sort()

        for code in codes :

            if code == '' :
                continue

            name = self.stations[code]
            
            # This is a series of badly named kludges but
            # I'm too tired to sort it out right now. At
            # the moment is a special case for TFL but eventually
            # all the other providers will use dicts too.
            
            if type(name) == types.DictType :

                line = None
                
                if name.has_key('line') and name['line'] != '' :
                    line = self.lines[name['line']]

                name = name['name']

                if line: 
                    name = "%s (%s line)" % (name, line.capitalize())
                    
            prepared.append((code, name))

        return prepared
    
    def display (self, template_name, template_values={}) :

        root = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(root, 'templates', template_name)
    
        self.response.out.write(template.render(path, template_values))
