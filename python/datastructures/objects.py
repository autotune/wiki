#!/usr/bin/python2.6

# assignment statement
internet = "" 
internet = "network"
home = ""
home = internet 
print home

# no reserved words from control structure or error handeling
# alias object reads right to left. New floating point value
# gets created first 
connection = ""
connection = "fiber"
internet = "home network"
internet = connection + ' ' +  internet
print internet 

class Taco(object):
    taco = "This object is a taco"
    def __init__(self, taco):
      self.type = taco
      print self.taco

Taco("cheese")
