****an�lisis de cluster

*** al escoger el n�mero de clusters debemos ser cuidados, debido  a que no todos los elementos pueden  agruparse en categorias, pues habr�an muy disjuntas sin justificaci�n.
 use "C:\Users\TOSHIBA\Desktop\trabajo orjuela\trabajo empirico\base.dta", clear

*keep pib2000 pib2015 dpto
 
cluster kmeans pib2000 pib2015, k(6) name(categoria)

table categoria

list dpto if categoria==1 

list dpto if categoria==2

** agregar statistics....
tabstat pib2000-pib2015, by(categoria)

** averiguar cual es el factor de an�lisis. y ojo por que el viejo lo saca es las estadisticas mean y todo eso..




factor pib2000-pib2015

loadingplot


**** ANOVA analysis como es la vuelta?


