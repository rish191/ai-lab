:- use_module(library(pce)).
:- dynamic monkey_pos/1, box_pos/1, on_box/1.
:- dynamic monkey_obj/1, box_obj/1.

% Initial state
monkey_pos(door).
box_pos(window).
on_box(no).

% Screen positions
pos(door,   50).
pos(window, 200).
pos(middle, 350).

start :-
    new(W, picture('Monkey Banana Animation')),
    send(W, size, size(500,300)),

    % Banana
    send(W, display, new(Banana, ellipse(30,30)), point(360,30)),
    send(Banana, fill_pattern, colour(yellow)),

    % Box
    send(W, display, new(Box, box(50,50)), point(200,200)),
    send(Box, fill_pattern, colour(brown)),
    assert(box_obj(Box)),

    % Monkey
    send(W, display, new(M, circle(40)), point(50,220)),
    send(M, fill_pattern, colour(grey)),
    assert(monkey_obj(M)),

    % Run button
    send(W, display,
         button(run, message(@prolog, solve_animate)),
         point(200,260)),

    send(W, open).

solve_animate :-
    move_monkey(window),
    move_box(middle),
    climb_box,
    grab_banana.

move_monkey(To) :-
    monkey_obj(M),
    pos(To, X),
    send(M, move, point(X,220)),
    retract(monkey_pos(_)),
    assert(monkey_pos(To)),
    sleep(1).

move_box(To) :-
    box_obj(B),
    pos(To, X),
    send(B, move, point(X,200)),
    monkey_obj(M),
    send(M, move, point(X,220)),
    retract(box_pos(_)),
    assert(box_pos(To)),
    sleep(1).

climb_box :-
    monkey_obj(M),
    box_pos(P),
    pos(P, X),
    send(M, move, point(X,160)),
    retract(on_box(_)),
    assert(on_box(yes)),
    sleep(1).

grab_banana :-
    on_box(yes),
    send(@display, inform, 'Monkey grabbed the banana!').

:- initialization(start).
