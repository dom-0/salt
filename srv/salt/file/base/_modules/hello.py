#!/usr/bin/env python

import logging
logger = logging.getLogger(__name__)

def world():
  return("Hello World")

def fqdn():
  testvar = __name__
  name = __grains__['id']
  logger.debug('Found grain id {}'.format(name))
  return "Hello {} {}".format(testvar, name)

def hi():
  return("Hello")
