'''
Created on May 31, 2015

@author: Greg Silverman
'''

def comp(a,b):
    return a<b 

def nocomp(a,b):
    return False

def f(l,d,r,e,comp):
    d += 1
    if d<e:
        for i in xrange(len(l)):
            r[d] = l[i]
            if d>0:
                if comp(r[d],r[d-1]):
                    continue
            for perm in f(l[0:i]+l[i+1:],d,r,e,comp):
                yield perm
    else:
        if d!=e:
            r[d] = l[0]
        d -= 1
        yield r[0:d+1]

def myPermu(l,d,r,e):
    return f(l,d,r,e,lambda a,b:False)

def myCombo(l,d,r,e):
    return f(l,d,r,e,lambda a,b:a<b)

l = [i+1 for i in xrange(5)]
r = [None]*len(l)

d = -1
e = len(l)-1
h = myPermu(l, d, r, e)
for i,j in enumerate(h):
    pass 
    print i+1,j
