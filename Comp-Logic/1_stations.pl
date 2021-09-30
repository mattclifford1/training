% define the network of underground stations FACTS
% connected is where there are no stations inbetween
connected(bond_street,oxford_circus,central).
connected(oxford_circus,tottenham_court_road,central).
connected(bond_street,green_park,jubilee).
connected(green_park,charing_cross,jubilee).
connected(green_park,piccadilly_circus,piccadilly).
connected(piccadilly_circus,leicester_square,piccadilly).
connected(green_park,oxford_circus,victoria).
connected(oxford_circus,piccadilly_circus,bakerloo).
connected(piccadilly_circus,charing_cross,bakerloo).
connected(tottenham_court_road,leicester_square,northern).
connected(leicester_square,charing_cross,northern).

% nearby RULE
nearby(X,Y):-connected(X,Y,_L). % next to each other on the same line
nearby(X,Y):-connected(X,Z,L),connected(Z,Y,L). % one station away on the same line

% not too far RULE - "on the same or a different line, with at most one station in between"
not_too_far(X,Y):-nearby(X,Y).
not_too_far(X,Y):-connected(X,Z,_L1),connected(Z,Y,_L2).

% reachable recurrsive RULE
% reachable(X,Y):-connected(X,Y,_L).
% reachable(X,Y):-connected(X,Z,L),reachable(Z,Y).

% reachable via routes
% reachable(X,Y,noroute):-connected(X,Y,_L).
% reachable(X,Y,route(Z)):-connected(X,Z,_L1),connected(Z,Y,_L2).
% reachable(X,Y,route(Z1,Z2)):-connected(X,Z1,_L1),connected(Z1,Z2,_L2),connected(Z2,Y,_L3).

% routes re written
% reachable(X,Y,noroute):-connected(X,Y,_L).
% reachable(X,Y,route(Z,R)):-connected(X,Z,_L),connected(Z,Y,R).

% routes using lists to define num of stations as params
reachable(X,Y,[]):-connected(X,Y,_L).
reachable(X,Y,[Z|R]):-connected(X,Z,_L),reachable(Z,Y,R).
% query this using ?-reachable(X,charing_cross,[A,B,C,D])



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % print out some queries
% :- forall(not_too_far(bond_street, X), (writeln(X))).
