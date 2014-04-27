% Monica Thornton
% CSCI 305 Lab 4
:- consult('royal.pl').

% Program to define a set of genealogical rules.
% In all of the rules, the order is as follows:
% first argument is the <relation> second argument,
% that is M is the mother of C, P is the son of C.

% Rule that defines a mother (M) as a female parent of a child (C).
mother(M,C):- parent(M,C), female(M).

% Rule that defines a father (F) as a male parent of a child (C).
% Rule is followed by a cut, because a child only has one father (in
% our definition of father).
father(F,C):- parent(F,C), male(F), !.

% Rule that defines a spouse as a married couple, contains an or (;) so
% that the order the spouse was given in does not matter.
spouse(H,W):- married(H,W); married(W,H).

% Rule that defines a child (C) by transposing the arguments given in
% the parent rule. Given a child (C), and a parent (P) if the child is
% provided in the argument, both parents will be returned. However, if a
% parent is provided in the argument, the child (or children) will be
% returned.
child(C,P):- parent(P,C).

% Rule that defines a son as a child (C) who is male. The same rules
% that govern arguments for child (above) apply with the son rule.
son(C,P):- child(C,P), male(C).

% Rule that defines a daughter as a child (C) who is female. Again, the
% same rules that govern arguments for child (above) apply with the
% daughter rule.
daughter(C,P):- child(C,P), female(C).

% Rule that defines a sibling of (X) as having the same parents. The
% rule also specifies that X and Y cannot be the same person otherwise
% we will have duplicate results.
sibling(X,Y):- mother(M,X), mother(M,Y), father(F,X), father(F,Y), \+ X == Y.

% Rule that defines a brother of (B) as one (or more) male sibling(s),
% Y. A name (or names) is returned if B has a brother. If the brother Y
% is provided as an argument, the sibling(s) B is returned.
brother(B,Y):- sibling(B,Y), male(B).

% Rule that defines a sister of (S) as one (or more) female sibling(s),
% Y. A name (or names) is returned if S has a sister. The same rules
% regarding arguments for brother (above) apply, but with the genders
% switched.
sister(S,Y):- sibling(S,Y), female(S).

% Set of rules to define a relationship between an uncle U, and
% their nieces/nephews (X or Y). The first rule defines an uncle by
% blood, that is, as the sibling of X's parent. The second rule defines
% an uncle by marriage, that is, when they are married to a sibling of
% Y's parent.
uncle(U,X):- sibling(U,P), parent(P,X), male(U).
uncle(U,Y):- spouse(U,A), sibling(A,P), parent(P,Y), male(U).

% Set of rules to define a relationship between an aunt A, and
% their nieces/nephews (X or Y). The first rule defines an aunt by
% blood, that is, as the sibling of X's parent. The second rule defines
% an aunt by marriage, that is, when they are married to a sibling of
% Y's parent.
aunt(A,X):- sibling(A,P), parent(P,X), female(A).
aunt(A,Y):- spouse(A,U), sibling(U,P), parent(P,Y), female(A).

% Rule that defines a grandparent (G) as the parent of X's parent. This
% rule would return both the grandmother and grandfather (and both sets,
% if the data allows for it).
grandparent(G,X):- parent(G,P), parent(P,X).

% Rule that defines a grandfather as a male grandparent. If the
% grandfather (G) is provided in the argument, their grandchild(ren) are
% returned. If the name of the grandchild (X) is provided instead, then
% the name of the grandfather is returned.
grandfather(G,X):- grandparent(G,X), male(G).

% Rule that defines a grandmother as a female grandparent. The same
% rules governing the arguments of grandfather (above) apply, but with
% the genders switched.
grandmother(G,X):- grandparent(G,X), female(G).

% Rule that defines a grandchild (C) by transposing the arguments given
% in the grandparent rule. Given a child (C), and a parent (G) if the
% grandchild is provided in the argument, both grandparents will be
% returned. However, if a grandparent is provided in the argument, the
% grandchild (or grandchildren) will be returned.
grandchild(C,G):- grandparent(G,C).

% Set of rules to define an ancestor of (D), given from most remote to
% most immediate. The first rule gets ancestors of D in generations
% preceding their parents by first looking at their parent's parents,
% and then the ancestors of those parents (through recursion). The second rule
% comes into play when there are no more ancestors, and it defines the
% ancestor (A) of (D) as an parent of D.

ancestor(A,D):- parent(A,X), ancestor(X,D).
ancestor(A,D):- parent(A,D).

% Rule that defines a descendant (D) in terms of D's ancestors.
descendant(D,A):- ancestor(A,D).

% Rule that compares the birth year for two people (O) and (Y). If the
% birth year (X) of the first person (O) happens before the birth year
% (Z) of the second person, their name (or true, if the name is
% provided) is returned to indicate that they are older. If the second
% person (Y) is older, than false is returned.
older(O,Y):- born(O,X), born(Y,Z),((X < Z) -> true ; false).

% Rule that compares the birth year for two people (O) and (Y). If the
% birth year (X) of the first person (O) happens before the birth year
% (Z) of the second person, false is returned to indicate that they are
% not younger. If the second person (Y) is younger, than true is
% returned.
younger(O,Y):- born(O,X), born(Y,Z), ((X < Z) -> false ; true).

% Rule to determine who the regent (R) was when person (B) was born.
% This is done by first getting the birth year of person (B), and then
% comparing it to the start (S) and end dates (E) of various regents. If
% they were born between the start and end date (inclusive) of the
% regent's reign, then that regent was reigning when they were born.
regentWhenBorn(R,B):- born(B,Y), reigned(R, S, E), S=<Y, Y=<E, !.















