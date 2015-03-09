#!/usr/bin/python2.6
# dictionaries howto 

managed_sysops = 0
managed_infra = 0

# no need for ordered items here
# hourly server prices
flavors = {'general1-1' :0.037, 'general1-2' :0.074, 'general1-4' :.148, 'general1-8' :.296}
servers = ""
num_hours = 0
total_dollars = 0
done = False

# do not exit loop until done
while not done:
  flavname = raw_input("Flavor: ")
  if flavname == '':
    done = True 
  elif flavname == "exit":
    quit()
  elif flavname not in flavors:
    print("Unknown flavor '{0}' being ignored".format(flavname))
  else:
    print flavors[flavname]

print "Welcome to my cloud server cost calculator"
print "Please enter"


