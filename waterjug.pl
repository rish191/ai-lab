move((X,Y),(4,Y)).
move((X,Y),(X,3)).
move((X,Y),(0,Y)).
move((X,Y),(X,0)).
move((X,Y),(X1,Y1)) :- T is min(X, 3-Y), X1 is X-T, Y1 is Y+T.
move((X,Y),(X1,Y1)) :- T is min(Y, 4-X), X1 is X+T, Y1 is Y-T.

path(State, Goal, Visited) :-
    State = Goal,
    write(State), nl.

path(State, Goal, Visited) :-
    move(State, Next),
    \+ member(Next, Visited),
    write(State), nl,
    path(Next, Goal, [Next|Visited]).

solve :-
    path((0,0),(2,_),[(0,0)]).