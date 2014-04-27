% Monica Thornton
% CSCI 305 Lab 4
:- consult('royal.pl').

%Program to define a set of genealogical rules.
%In all of the rules, the order is as follows:
%first argument is the <relation> second argument,
%that is M is the mother of C, P is the son of C.

%rule that defines a mother (M) as a female parent of a child (C)
mother(M,C):- parent(M,C), female(M).

%rule that defines a father (F) as a male parent of a child (C)
father(F,C):- parent(F,C), male(F).

% rule that defines a spouse as a married couple, contains an or (;) so
% that the order the spouse was given in does not matter.
spouse(H,W):- married(H,W); married(W,H).

%rule that relates a parent (P) to their child (C)
child(P,C):- parent(C,P).

%rule that defines a son as a child (C) who is male
son(P,C):- child(P,C), male(C).

%rule that defines a daughter as a child (C) who is female
daughter(P,C):- child(P,C), female(C).

%rule that defines a sibling of (X) as a child of the same parent
sibling(X,Y):- father(F,X), father(F,Y), mother(M,X), mother(M,Y), not(same(X,Y)).

%rule used to determine if two arguments are the same
same(X,X).


brother(B,Y):- sibling(B,Y), male(B).
sister(S,Y):- sibling(S,Y), female(S).

uncle(U,X):- sibling(U,P), parent(P,X), male(U).
uncle(U,Y):- spouse(U,A), sibling(A,P), parent(P,Y), male(U).

aunt(A,X):- sibling(A,P), parent(P,X), female(A).
aunt(A,Y):- spouse(A,U), sibling(U,P), parent(P,Y), female(A).

cousin(C,X):- parent(A,C), parent(B,X), sibling(A,B).

grandparent(G,X):- parent(G,P), parent(P,X).

grandfather(G,X):- grandparent(G,X), male(G).
grandmother(G,X):- grandparent(G,X), female(G).

grandchild(C,G):- grandparent(C,G).

ancestor(A,D):- parent(A,D).
ancestor(A,D):- parent(A,X), ancestor(X,D).

descendant(D,A):- ancestor(A,D).

older(O,Y):- born(O,X), born(Y,Z), (( X < Z) -> true ; false).

younger(O,Y):- born(O,X), born(Y,Z), (( X < Z) -> false ; true).

regentWhenBorn(R,B):- born(B,Y), reigned(R, S, E), S=<Y, Y=<E.







