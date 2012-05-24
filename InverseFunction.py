# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        return binary_search(f, y, 0, 2, delta)
    return f_1

def binary_search(f, y, nMin, nMax, delta):
    x0 = f(nMin*delta)
    x1 = f(nMax*delta)
    if (nMin == (nMax-1)): #the root
        #print str(x0) + ', ' + str(y) + ', ' + str(nMin*delta) + ', ' + str(nMax*delta)
        #print x1
        return nMin*delta if (y-x0 < x1-y) else nMax*delta
    elif x1<y: # expand the bounds
        #print 'expand: '+str(nMax)+', '+str(nMax*2)
        return binary_search(f, y, nMax, nMax*2, delta)
    else: #within bounds so close in
        mid = nMin + (nMax-nMin)/2
        #print 'contract '+str(f(mid*delta))
        if f(mid*delta) > y:
            #print str(nMin) + ', '+str(mid)
            return binary_search(f, y, nMin, mid, delta)
        else:
            #print str(mid) + ', '+str(nMax)
            return binary_search(f, y, mid, nMax, delta)
    
def square(x): return x*x
sqrt = slow_inverse(square)
sqrt2 = inverse(square)
print 'start old'
print sqrt(1000000000)
print 'start new'
print sqrt2(1000000000)

