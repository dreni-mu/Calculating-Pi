#This code uses 3 different methods to approximate pi and plots their course to show how efficient each one is
import math as m
import numpy as np
import matplotlib.pyplot as plt
#calculate pi w/ infinite series
runs=10
pi=0
y1=np.zeros(runs)
y2=np.zeros(runs)
y3=np.zeros(runs)
x=np.arange(0,runs,1)
z=[]
for i in range (0,runs):
    z.append(np.pi)
for n in range(1,runs+1):
    pi+=6*(1/(n**2))
    sqrtpi=m.sqrt(pi)
    y1[n-1]=sqrtpi
print(y1)


#calculate pi w/ infinite series
pi=0
for n in range(0,runs):
    pi+=4*((-1)**n)/(2*n+1)
    y2[n]=pi
print(y2)

#calculate pi using newton
n1=1/2
n=[]
for i in range(0,runs):
    n.append(n1)
    n1-=1



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
    y3[i]=total
    p+=2

plt.plot(x,y1, label='(pi^2)/6')
plt.plot(x,y2, label='pi/4')
plt.plot(x,z)
plt.plot(x,y3, label='newton')

plt.xlabel("iterations")
plt.ylabel("value")

plt.legend(loc="upper right")
plt.show