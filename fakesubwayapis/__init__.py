from APIApp import APIApp

class fakesubwayapi (APIApp) :

    def __init__ (self) :
        APIApp.__init__(self, 'xml')
