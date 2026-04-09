from pyDatalog import pyDatalog

pyDatalog.create_terms('p, q, r')

+ p(True)
+ q(False)

r(X) <= p(X) & q(X)

print(r(X))