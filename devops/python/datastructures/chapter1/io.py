#!/usr/bin/env python
import fileinput

miles = 12.0
minutes = 150.0
# time in minutes
hour = 60
hours = 1
total = hour/minutes
text = [] 
process_text = False

print "Hi there!"
# not really practical but eh. 
# while int(input('The answer to life, the universe, and everything: ')) != 42:
#   print "Try again"
# miles = float(input('Miles ran: '))
# minutes = float(input('Total time ran: '))
# time = time * .10
# distance = rate/time

print "You ran %s miles" % miles
print "You ran %s miles in %s minutes " % (miles,minutes)

print "%s minutes per mile" % ((minutes)/(miles))

fp = open('glossary.md', 'r')

# print out open functions 
for i in dir(fp):
    print i

# 1 KB is one text character 
print fp.read(13)

for line in fp:
    if "1.1" in line:
        line = line.rstrip().replace('#### 1.5.1', '#### 1.5.1 Success')
        text.append(line)
fp.close()

# replace text
for line in fileinput.input('glossary.md', inplace=1):
    line = line.rstrip().replace('#### 1.5.1', '#### 1.5.1 Success')
    print line


for line in text:
    print line 
