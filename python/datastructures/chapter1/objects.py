#!/usr/bin/python2.6

# import module example
import httplib
browse = httplib.HTTPConnection("www.google.com") 
browse.request("GET", "/index.html")
result = browse.getresponse()
print result.status

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

# update the core application only
# class update(software):
#     print "Software update function"
    # instantiate object
    # check existing packages
    # list required packages
    # update if desired
    # download from main site
    # replace specified application core
    # leave anything like themes, modules, 
    # custom code, etc. alone.


