#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp

import fakesubwayapis
import fakesubwayapis.bart
import fakesubwayapis.mbta
import fakesubwayapis.mta
import fakesubwayapis.stm
import fakesubwayapis.tfl
import fakesubwayapis.ukrail

if __name__ == '__main__':

  handlers = [
    ('/', fakesubwayapis.fakesubwayapidocs),

    (r'/bart/getinfo/([a-z0-9]+)/?', fakesubwayapis.bart.getinfo),
    (r'/bart/station/([a-z0-9]+)/?', fakesubwayapis.bart.station),    
    (r'/bart/?', fakesubwayapis.bart.docs),    

    (r'/mbta/getinfo/([a-z0-9]+)/?', fakesubwayapis.mbta.getinfo),
    (r'/mbta/station/([a-z0-9]+)/?', fakesubwayapis.mbta.station),    
    (r'/mbta/?', fakesubwayapis.mbta.docs),    

    (r'/mta/getinfo/([a-z0-9]+)/?', fakesubwayapis.mta.getinfo),
    (r'/mta/station/([a-z0-9]+)/?', fakesubwayapis.mta.station),
    (r'/mta/?', fakesubwayapis.mta.docs),    

    (r'/stm/getinfo/(m\d{2})/?', fakesubwayapis.stm.getinfo),
    (r'/stm/station/(m\d{2})/?', fakesubwayapis.stm.station),    
    (r'/stm/?', fakesubwayapis.stm.docs),    

    (r'/tfl/getinfo/(\w+)(?:-(\w))?/?', fakesubwayapis.tfl.getinfo),
    (r'/tfl/station/(\w+)(?:-(\w))?/?', fakesubwayapis.tfl.station),
    (r'/tfl/?', fakesubwayapis.tfl.docs), 

    (r'/ukrail/getinfo/(\w{3})/?', fakesubwayapis.ukrail.getinfo),
    (r'/ukrail/station/(\w{3})/?', fakesubwayapis.ukrail.station),    
    (r'/ukrail/?', fakesubwayapis.ukrail.docs), 
    ]

  application = webapp.WSGIApplication(handlers, debug=False)
  wsgiref.handlers.CGIHandler().run(application)
