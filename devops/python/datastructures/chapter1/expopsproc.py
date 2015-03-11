#!/usr/bin/python2.6
# Expressions, Operators, and Procedence

indie_rock = {"radiohead" :"Radiohead", "pixies" :"Pixies", "interpol" :"Interpol", "m83": "M83"}  
indie_rock_list = ["Radiohead", "Pixies", "Interpol", "M83"]  
rock = {"the_steve_miller_band" :"The Steve Miller Band", "jimmy_eat_world" :"Jimmy Eat World", "say anything" :"Say Anything", "everclear" :"Everclear"} 
rock_list = ["The Steve Miller Band", "Jimmy Eat World"]
ska = {"mighty_mighty_bosstones" :"Mighty Mighty Bosstones", "gold_finger" :"Gold Finger", "reel big fish" :"Reel Big Fish"}

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
# substitute with != and == for is not and is

if indie_rock["pixies"] is "Pixies":
  print "Yup, that's Pixies" 

if rock["everclear"] is not "Say Anything":
  print "These are two different artists!" 

print "There are %s bands in indie rock" % len(indie_rock) 
print "There are %s bands in rock" % len(rock) 
print "There are %s bands in ska" % len(ska)

# comparison operators 
if len(indie_rock) < len(rock):
  print "There are less bands in indie rock than rock"
elif len(indie_rock) < len(ska):
  print "There are less bands in indie rock than ska"
elif len(indie_rock) <= len(rock):
  print "There are as many indie rock bands as there are rock"

if len(indie_rock) > len(ska):
  print "There are more bands in indie rock than ska"

# arithmatic operators
total_rock = len(rock) + len(indie_rock)
total_artists = total_rock + len(ska)
more_rock = total_rock - len(ska) 
equipment_costs = 10000
total_costs = equipment_costs * total_artists
total_income = 1000000
artist_income = total_income/total_artists
fish_income = artist_income
fish_guitar = ~1300

print "There are %s rock and indie rock bands" % total_rock 
print "There are %s more total rock and indie rock artists than ska" % more_rock
print "It will cost %s per band to buy equipment and %s for %s bands" % (equipment_costs, total_costs, total_artists)
print "We will have to divide %s income among %s bands for a total of %s per band" % (total_income, total_artists, artist_income)
  
# bitwise operators
# skipping over section until actually needed

# sequence operators 
print indie_rock_list[0]
print indie_rock_list[0:3]
# slice indices until stop x at step y
print indie_rock_list[0:4:2]
# zero index indicing is awesome 
print indie_rock_list[0] + ' ' + indie_rock_list[1]

# value check 
if "Radiohead" in indie_rock_list:
    print "Found Radiohead"

if "radiohead" not in indie_rock_list:
    print "Proper grammar required"

# operators for sets and dictionaries

# comparison operators
print "NO len()" 
if indie_rock <= rock:
  print "There are as many or less indie rock bands as there are rock"
elif indie_rock >= rock:
  print "There are as many or more indie rock bands as there are rock"

if indie_rock < ska:
  print "There are less bands in indie rock than ska"

if indie_rock > ska:
  print "There are more bands in indie rock than ska"

print indie_rock_list[0]
del indie_rock_list[0]
print indie_rock_list[0]
print len(indie_rock_list)

new_band = ["As Tall As Lions"]
band = new_band
indie_rock_list += band
print indie_rock_list[3]
indie_rock_list = indie_rock_list + rock_list 
print indie_rock_list

precedense = indie_rock_list[1] + ' ' + (indie_rock_list[0] + ' ' +  indie_rock_list[3])
print precedense
