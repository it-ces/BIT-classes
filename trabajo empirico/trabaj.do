** probar la hipotesis de que las economías más ricas crecen menos**

 use "C:\Users\TOSHIBA\Desktop\trabajo orjuela\trabajo empirico\base.dta", clear
 
drop year 	
 
 reshape long pib, i(dpto) j(year)
 
 bysort dpto (year): gen tasa= (pib-pib[_n-1])/pib[_n-1]
 
 bysort dpto: egen avaragetasa=mean(tasa) if inrange(year,2001,2016)
 
 keep pib avaragetasa dpto year 
 
 reshape wide pib avaragetasa, i(dpto) j(year)

 scatter avaragetasa2001 pib2000

 
 cluster averagelinkage pib2000 avaragetasa2001 , name(av)
 cluster dendrogram av 
 cluster gen g5cl=groups(5), name(av)

sort g5cl 
forvalues i=1/5{
displa	 " "
display "cluster `i'"
list dpto if g5cl==`i', noobs noheader separator(0)
}

table g5cl, contents(mean pib2000  mean avaragetasa2001)
