'''
Created on Jul 12, 2015

@author: Jeffrey
'''
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x < b :
        return 0
    return myLog(x/b, b) + 1

def lessThan4(aList):
    res = []
    for x in aList :
        if len(x) < 4 :
            res += [x]
    return res

def sumDigits(N):
    if N == 0 :
        return 0
    return N%10 + sumDigits(N/10)

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    res = []
    for key in aDict.keys() :
        if aDict[key] == target :
            res += [key]
    return res
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    res = []
    for x in L :
        if f(x) :
            res += [x]
    L[:] = res
    return len(L)
    
def f(s):
    return 'a' in s
      
#L = ['a', 'b', 'a']
#print satisfiesF(L)
#print L

def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L
swapSort([1,10,2,9,3,7])

