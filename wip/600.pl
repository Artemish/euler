?- use_module(library(clpfd)).

valid_hex(Vs, Top) :-
    Vs = [A,B,C,D],
    A #> 0, B #> 0, C #> 0, D #> 0, 
    B #=< C,
    A #< (C + D),
    D #< (B + A),
    (A + (2*C) + (2*B) + D) #=< Top,
    labeling([], Vs).
