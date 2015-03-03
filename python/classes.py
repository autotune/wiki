#!/usr/bin/python2.6

class Taco(object):
    taco = "This object is a taco"
    def __init__(self, taco):
      self.type = taco
      print self.taco

Taco("cheese") 
