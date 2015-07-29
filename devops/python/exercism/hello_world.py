#
# Skeleton file for the Python "Hello World" exercise.
#
import argparse
import sys

parser = argparse.ArgumentParser(description='Accept name.')
# nargs otherwise annoying message about too few arguments. 
parser.add_argument('myname', nargs='?')


def hello(name=parser.parse_args()):
    try:
        if len(name.myname) > 0:
            print "Hello, {0}".format(name.myname)
    except:
        print "Hello, World"
    sys.exit(1)
    finally:
        sys.exit
    return

def main():
    hello() 

# determines that code is being ran directly rather than via module.
if __name__ == "__main__":
   main()
