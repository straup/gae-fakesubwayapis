from APIApp import APIApp

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os.path

class fakesubwayapi (APIApp) :

    def __init__ (self) :
        APIApp.__init__(self, 'xml')

class fakesubwayapidocs (webapp.RequestHandler) :

    def get (self) :

        self.display("intro.html")
        return

    def display (self, template_name, template_values={}) :

        root = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(root, 'templates', template_name)
    
        self.response.out.write(template.render(path, template_values))
        
