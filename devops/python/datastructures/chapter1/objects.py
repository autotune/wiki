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
internet = "network"
internet = connection + ' ' +  internet
print internet 

# create a music class that prints an artist
class Music(object):

    asiwyfa = "This musician is And So I Watch You From Afar"
    giao = "This musician is God Is An Astronaut"
    def __init__(self, artist):
      self.type = artist
    
    def _printall_(self, allartists):
      self.type = allartists
      print asiwyfa
      print giao

artist = Music("artist")
allartists = Music("allartists")

# instantiate an object
asiwyfa = artist.asiwyfa

print asiwyfa

# calling methods/member functions

print asiwyfa.upper()

mainstream = []
mainstream = ["Hello", False, True, 1, 1.50, int(1.50), ["World"],("foo", 1, "bar" ), "\"Hi there!\"", set('abcdefg'), {'whoop' :'whoop'}]

# print out class types
for i in mainstream:
   print str(i) + ' ' + str(type(i)) 
   

