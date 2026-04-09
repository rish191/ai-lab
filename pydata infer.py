from pyDatalog import pyDatalog

pyDatalog.create_terms('parent, ancestor, X, Y, Z')

+ parent('john','mary')
+ parent('mary','susan')

ancestor(X,Y) <= parent(X,Y)
ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)

print(ancestor('john', Y))