parent(john, mary).
parent(mary, sam).
parent(john, david).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).