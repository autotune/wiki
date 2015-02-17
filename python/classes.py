#!/usr/bin/python2.6

class Taco(object):

    "This object is a taco"

    def __init__(self, type):
      self.type = type
      print self.type

Taco("cheese") 
