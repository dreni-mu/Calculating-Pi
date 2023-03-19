#calculate pi newtonian method
import numpy as np
import math as m
import matplotlib.pyplot as plt

runs=100
n1=1/2
n=[]
for i in range(0,runs):
    n.append(n1)
    n1-=1

x=np.arange(0,runs,1)
y=np.zeros(runs)
z=[]
for i in range (0,runs):
    z.append(np.pi)
p=0 #power of x after sub
total=0
for i in range (0,runs):
    nmult=1
    for j in range(0,i):
        if i ==0:
            nmult=1
        else:
            nmult*=n[j]
    if i == 0:
        total=4
    else:
        total-=4*abs(nmult/((m.factorial(i))*(p+1)))
    y[i]=total
    p+=2
plt.plot(x,y)
plt.plot(x,z)

plt.xlabel("iterations")
plt.ylabel("value")

print(y[len(y)-1])