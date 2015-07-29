#!/usr/bin/env python
# illistrate a factorial example

def fib(n):
 # take two values and assign them "1"
 a,b = 1,1
 # take range of given number
 for num in range(n-1):
  # assign a,b value of b and a+b
  a,b = b,a+b
  print num 
 print a

print fib(5)
