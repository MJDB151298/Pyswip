:-dynamic progenitor/2.
progenitor(juan, maria).

insertarProgenitor():- write('Inserta el nombre del padre '), read(Padre),nl,write('Inserte el nombre del hijo'),read(Hijo),nl,assert(progenitor(Padre, Hijo)),write(progenitor(Padre, Hijo)).

retractPadre():- write('Escribe el nombre del padre: '),read(Padre),retractall(progenitor(Padre,_)).

retractEspecifico(Padre,Hijo):- retract(progenitor(Padre,Hijo)).
