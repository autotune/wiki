#!/usr/bin/python2.6
# Expressions, Operators, and Procedence

indie_rock = {"radiohead" :"Radiohead", "pixies" :"Pixies", "interpol" :"Interpol", "m83": "M83"}  
rock = {"jimmy_eat_world" :"Jimmy Eat World", "say anything" :"Say Anything", "everclear" :"Everclear"} 

# logical operators 

# not
if "Say Anything" not in indie_rock:
    print "Say Anything not found in indie rock." 

# and is if both are true
if "radiohead" and "pixies" in indie_rock:
    # requires tuple to return strings 
    print "%s and %s have been found in indie rock!" % (indie_rock["radiohead"], indie_rock["pixies"]) 
# or is if either condition is true
# print all rock artists 
if "Radiohead" or "Jimmy Eat World" in rock:
  for artist in rock:
    print rock[artist] + " has been found in rock!"

# equality operators 

if indie_rock["pixies"] is "Pixies":
  print "Yup, that's Pixies" 

if rock["everclear"] is not "Say Anything":
  print "These are two different artists!" 
