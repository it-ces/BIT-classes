

**Esto es para ingreso principalmente pero vamos a tomar como proxy el PIB**

foreach x of varlist pib2000-pib2016{
gen ln`x'= ln(`x')
}



gen sdhistoric=.


foreach x of varlist  lnpib2000-lnpib2016{
quietly sum `x' 
scalar sd`x'= r(sd)
}



forvalue i=2000/2016{
replace  sdhistoric=sdlnpib`i' if year==`i'
}


** gráfica de la convergencia sigma.

graph twoway (line sdhistoric year)


graph2tex, eps(sd)




** gráfica introductoria

graph hbar pib2000 pib2016, over(dpto)


graph2tex, eps(intro)

** comparaciones en kdensity

twoway kdensity  pib2000 || kdensity  pib2007


****

***vamos a ver la evolución de algunos en el tiempo.
drop year 
reshape long pib, i(dpto) j(year)

xtset dpto year

xtline pib if dpto==2 | dpto==5 |dpto==18 | dpto==30, overlay


