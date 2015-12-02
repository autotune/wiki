#! /usr/bin/python
import sys

"""
tokenCalc() calculates the tokens requred for a class. This is calculated by 
taking the number of clusters and multiplying each node number by 2 to the 
power of 127 divided by the number of nodes in the cluster.
Original script per http://www.datastax.com/2012/01/how-to-set-up-and-monitor-a-multi-node-cassandra-cluster-on-linux
"""

class tokenCalc():
    def __init__(self):
        instatiate = []

    def tokenNums(self):
        if (len(sys.argv) > 1):
           num=int(sys.argv[1])
        else:
           num=int(raw_input("How many nodes are in your cluster? "))

        for i in range(0, num):
           print 'token %d: %d' % (i, (i*(2**127)/num))

def main():
    instantiate = tokenCalc()
    instantiate.tokenNums()

main()
