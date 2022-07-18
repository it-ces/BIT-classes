# Solow Model under the assumption of Cobb- Douglas production Function.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print("Welcome to the simulation of solow model")
print("--"*80)
print("Author:Iván Trujillo Abella")
print("In this program we Work with COB DOUGLAS production function") 
gp=float(input("Enter the value of growth rate of population: "))
alpha=float(input("Enter the value of share of  capital in GDP: "))
if alpha>=1:
    print("Your value its revalue to 0.5")
    alpha=0.5
if alpha<=0:
    alpha=0.5
dep=float(input("Enter the value of depretiation: "))
save=float(input("Enter the value of saving: "))
depreciation=(gp+dep)
ksteady=float((save/depreciation)**(1/(1-alpha)))
print("The value of Capital of steady state is : ", ksteady)
# We can allow us more interactions?
# How change the growth with differents levels of k.
def rate(ki):
    k=float((save*(ki**(alpha-1)))-(depreciation))
    return k



    
#Programa
#remeber that with plt we can graph
if ksteady <=800:
 lista=[[i,rate(i),i**alpha,((i**alpha)*save),i*depreciation] for i in np.arange(0,ksteady*2,0.01)]
else:
 lista=[[i,rate(i),i**alpha,((i**alpha)*save),i*depreciation] for i in np.arange(0,ksteady*2,1)]
lista=pd.DataFrame(lista, columns=["Capital", "Rate of Growth","output","saving","depreciation"])
plt.subplot()
plt.plot("Capital","output", data=lista)
plt.plot("Capital","saving", data=lista)
plt.plot("Capital","depreciation", data=lista)
plt.axvline(x=ksteady,color='red',linestyle='--')
plt.title("Capital of Steady State- Solow Model")
plt.show()
plt.plot("Capital","Rate of Growth", data=lista)
plt.axhline(y=depreciation,color='red',linestyle='--')
plt.title("Rate of growth- Solow Model")
plt.show()

print('succes', rate(ksteady))

