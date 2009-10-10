#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp

import fakesubwayapis
import fakesubwayapis.bart
import fakesubwayapis.mta
import fakesubwayapis.stm
import fakesubwayapis.tfl
import fakesubwayapis.ukrail

if __name__ == '__main__':

  handlers = [
    ('/', fakesubwayapis.fakesubwayapidocs),

    (r'/bart/getinfo/([a-z0-9]+)/?', fakesubwayapis.bart.getinfo),
    (r'/bart/?', fakesubwayapis.bart.docs),    

    (r'/mta/getinfo/([a-z0-9]+)/?', fakesubwayapis.mta.getinfo),
    (r'/mta/?', fakesubwayapis.mta.docs),    

    (r'/stm/getinfo/(m\d{2})/?', fakesubwayapis.stm.getinfo),
    (r'/stm/?', fakesubwayapis.stm.docs),    

    (r'/tfl/getinfo/(\w+)(?:-(\w))?/?', fakesubwayapis.tfl.getinfo),    
    (r'/tfl/?', fakesubwayapis.tfl.docs), 

    (r'/ukrail/getinfo/(\w{3})/?', fakesubwayapis.ukrail.getinfo),
    (r'/ukrail/?', fakesubwayapis.ukrail.docs), 
    ]

  application = webapp.WSGIApplication(handlers, debug=False)
  wsgiref.handlers.CGIHandler().run(application)
