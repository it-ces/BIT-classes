**Análisis cluster...**

use "C:\Users\TOSHIBA\Desktop\trabajo orjuela\trabajo empirico\base.dta", clear

*** Para mirar en la hipótesis de solow si las economías con mayor PIb iniical tuvieron tasas de crecimiento menor

cluster completelinkage  pib2000 pib2008, name(col)
cluster dendrogram
cluster averagelinkage  pib2000 pib2008, name(al)
cluster dendrogram



** Tratando de encontrar el óptimo..

cluster stop al, rule(duda) groups(1/5)  

* para mirar clasificación

cluster gen g5cl=groups(5), name(al)
sort g5cl 
forvalues i=1/5{
displa	 " "
display "cluster `i'"
list dpto if g5cl==`i', noobs noheader separator(0)
}

table g5cl, contents(mean pib2000  mean pib2015)
