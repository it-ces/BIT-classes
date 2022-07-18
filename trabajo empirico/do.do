clear all
 use "C:\Users\TOSHIBA\Desktop\trabajo orjuela\trabajo empirico\base.dta", clear

foreach x of varlist pib2000-pib2016{
egen nal`x'= sum(`x') 
}



forvalue i=2000/2016{

gen p`i'= (pib`i'/nalpib`i')*100
}


foreach x of varlist pib2000-pib2016{

sum `x'

gen min`x'= r(min)

gen max`x'= r(max)

gen tasa`x' = (max`x'/min`x')*100


}



forvalue i=2000/2016{
 sum tasapib`i', meanonly
 display "tasa del año `i' = " r(mean)	
 scalar a`i' = r(mean)
  }

gen list=.  

forvalue i=2000/2016{
replace list= a`i' if year==`i'
  }
  
  
  graph twoway line list year

  graph2tex, epsfile(gamma) 
