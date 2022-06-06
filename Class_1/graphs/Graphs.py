import matplotlib.pyplot as plt
"""
# Birthday paradox implementation: 
#k it is the number of person and n it is days of year
def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)

def permutation(n,k):
  return fact(n) / fact(n-k)

def paradox(n,k):
  result = 1-(permutation(n,k)/(n**k))
  return result
e=100
k = [i for i in range(1,e)]
probs = [paradox(360,i) for i in k]
fig=plt.plot(k,probs, 'black')
#plt.title(r'Birdthday paradox', fontsize=20)
plt.xlabel('K persones', fontsize=10)
plt.ylabel('Probability of two conincidences days in population', fontsize=10)
plt.savefig("paradox.eps")
plt.show()

print(paradox(360,5))

"""


### Graphs about PI estimation
"""
import numpy as np
import matplotlib.pyplot as plt
dots = 5000
c1,c2=-1,1
x = np.random.uniform(c1,c2, size=dots)
y = np.random.uniform(c1,c2, size=dots)
coordenates_circle = (x**2)+(y**2) < 1
circle_y=y[coordenates_circle]
circle_x=x[coordenates_circle]
pi = 4*np.sum(coordenates_circle) / dots
plt.scatter(x,y, color='yellow')
plt.scatter(circle_x,circle_y)
plt.title('Approximation of $\pi$ = {}'.format(pi))
plt.savefig('PiOne.eps')


"""
## Monty game:
import numpy as np
import matplotlib.pyplot as plt
import random
def monty_game():
  doors=[1,2,3]
  #doors_variable = doors.copy() 
  winner = random.randint(1,3)
  select_one = random.randint(1,3)
  values = [winner,select_one]
  switch = list( set(doors) - set(values))
  select_two = random.randint(switch[0], switch[-1])
  s1,s2 = 0,0
  if winner == select_one:
    s1 += 1
  else:
    s2 +=1
  return [s1,s2]

trials=2000
s1_=[]
s2_=[]
for n in range(1,trials):
  prob_s1 = sum([monty_game()[0] for x in range(1,n)])/n
  s1_.append(prob_s1)
  prob_s2 = sum([monty_game()[1] for x in range(1,n)])/n
  s2_.append(prob_s2)
plt.plot(np.arange(1,trials),s1_, label='Stick')
plt.plot(np.arange(1,trials),s2_, label='Switch',color='yellow')
plt.title('$P(Sticking)$ = {:.4},  $P(Switching)$ = {:.4} '.format(prob_s1,prob_s2))
plt.xlabel('Number of trials or games')
plt.ylabel('Probability of win')
plt.legend()
plt.savefig('Monty.eps')

    

