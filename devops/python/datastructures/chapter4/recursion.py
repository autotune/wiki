#!/usr/bin/env python

# print the previous value plus 
# previous value before it
def recursion(mylist=range(1, 5)):
  recursion = 1 
  for i in mylist:
      recursion = recursion + i   
      print str(i) + ':' + str(recursion) 
  return recursion 

print recursion()
