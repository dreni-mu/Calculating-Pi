#This code uses 100 iteration of an infinite sum to estimate the value of pi
import numpy as np
import matplotlib.pyplot as plt

summ_arr=[]
summ=0
iterations=100
for k in range(iterations):
    summ+=((-1)**k)/((2*k)+1)
    summ_arr.append(summ*4)
print("pi is approximately:",summ*4)

#plot
x=np.linspace(1,len(summ_arr),len(summ_arr))

pi=[]
for i in range(len(x)):
    pi.append(np.pi)

plt.plot(x,summ_arr,label='infinite sum')
plt.plot(x,pi,label='pi')
plt.legend(bbox_to_anchor=(1,1))