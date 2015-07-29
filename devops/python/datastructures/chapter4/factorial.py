#!/usr/bin/env python
# illistrate a factorial example

def factorial(n):
    print "Factorial has been called with n = " + str(n)
    if n == 1:
        return 1
    else:
        result = n * factorial(n-1)
        print str(n) + ':' + str(result)
        return result	
   
print(factorial(5))
