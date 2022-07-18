** índice de Theil**

sum ingreso [w=pondera] if ingreso>0
local media = r(mean)
gen each = ingreso/`media'*ln(ingreso/`media')

