#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp

import fakesubwayapis

import fakesubwayapis.boilerplate
import fakesubwayapis.ttc
import fakesubwayapis.tfl

if __name__ == '__main__':

  handlers = [
    ('/', fakesubwayapis.fakesubwayapidocs),

    (r'/(bart)/getinfo/([a-z0-9]+)/?', fakesubwayapis.boilerplate.getinfo),
    (r'/(bart)/station/([a-z0-9]+)/?', fakesubwayapis.boilerplate.station),    
    (r'/(bart)/?', fakesubwayapis.boilerplate.docs),    

    (r'/(mbta)/getinfo/(\d+)/?', fakesubwayapis.boilerplate.getinfo),
    (r'/(mbta)/station/(\d+)/?', fakesubwayapis.boilerplate.station),    
    (r'/(mbta)/?', fakesubwayapis.boilerplate.docs),    

    (r'/(mta)/getinfo/([a-z0-9]+)/?', fakesubwayapis.boilerplate.getinfo),
    (r'/(mta)/station/([a-z0-9]+)/?', fakesubwayapis.boilerplate.station),
    (r'/(mta)/?', fakesubwayapis.boilerplate.docs),

    (r'/(stm)/getinfo/(m\d{2})/?', fakesubwayapis.boilerplate.getinfo),
    (r'/(stm)/station/(m\d{2})/?', fakesubwayapis.boilerplate.station),    
    (r'/(stm)/?', fakesubwayapis.boilerplate.docs),    

    (r'/tfl/dump/?', fakesubwayapis.tfl.dump),
    (r'/tfl/getinfo/(\w+)(?:-(\w))?/?', fakesubwayapis.tfl.getinfo),
    (r'/tfl/station/(\w+)(?:-(\w))?/?', fakesubwayapis.tfl.station),
    (r'/tfl/?', fakesubwayapis.tfl.docs), 

    (r'/ttc/getinfo/(\w+)/?', fakesubwayapis.ttc.getinfo),
    (r'/ttc/station/(\w+)/?', fakesubwayapis.ttc.station),
    (r'/ttc/?', fakesubwayapis.ttc.docs), 

    (r'/(ukrail)/getinfo/(\w{3})/?', fakesubwayapis.boilerplate.getinfo),
    (r'/(ukrail)/station/(\w{3})/?', fakesubwayapis.boilerplate.station),    
    (r'/(ukrail)/?', fakesubwayapis.boilerplate.docs), 

    (r'/(wmata)/getinfo/(\w+)/?', fakesubwayapis.boilerplate.getinfo),
    (r'/(wmata)/station/(\w+)/?', fakesubwayapis.boilerplate.station),
    (r'/(wmata)/?', fakesubwayapis.boilerplate.docs), 

    ]

  application = webapp.WSGIApplication(handlers, debug=False)
  wsgiref.handlers.CGIHandler().run(application)
