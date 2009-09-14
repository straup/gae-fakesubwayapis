#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp

import fakesubwayapis.bart
import fakesubwayapis.stm
import fakesubwayapis.tfl
import fakesubwayapis.ukrail

if __name__ == '__main__':

  handlers = [
    (r'/bart/getinfo/([a-z0-9]+)', fakesubwayapis.bart.getinfo),
    (r'/stm/getinfo/(m\d{2})', fakesubwayapis.stm.getinfo),
    (r'/tfl/getinfo/(\w+)(?:-(\w))?', fakesubwayapis.tfl.getinfo),    
    (r'/ukrail/getinfo/(\w{3})', fakesubwayapis.ukrail.getinfo),
    ]

  application = webapp.WSGIApplication(handlers, debug=False)
  wsgiref.handlers.CGIHandler().run(application)
