#!/usr/bin/env python

def exception():
    try:
        raise Exception('whoops')
    except Exception as val:
        print val 
        print type(val)
        whoa = val.args
        print 'whoah =', whoa

def attribute():
    # call attribute that doesn't exist
    print "\n def attribute():" 
    print "   attribute.error() \n"
    attribute.error()


def eoferror():
    print "\nfile = input('glossary.md')\n"
    file = input('glossary.md')

def io_error():
    print "\nfp = open('glossary', 'r')\n"
    fp = open('glossary', 'r')

def index_error():
    # returning list item where none exists
    print "\nmyval = []"
    print "print myval = [1] \n"
    myval = []
    print myval[1]

def key_error():

    print """\n    mydict = {}
    mydict[\"whoops\"]\n"""

    mydict = {}
    print mydict["whoops"]

def name_error():
    # no value exists
    print "\nmyval=val\n"
    myval = val

def stop_iteration():
    print """
    myval = "dog"
    myiter = iter(myval)
    print next(myiter)
    print next(myiter)
    print next(myiter)
    print next(myiter)
    """
    myval = "dog"
    myiter = iter(myval)
    print next(myiter)
    print next(myiter)
    print next(myiter)
    print next(myiter)

def type_error():
    # combining int with string
    hello=1 + "derp"
    return hello

# bonus time
def recursion_error():
    return recursion_error()

print type_error()
