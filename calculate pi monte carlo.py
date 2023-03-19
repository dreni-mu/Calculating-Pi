#calculate pi using monte carlo integration
import numpy as np
import matplotlib.pyplot as plt

num=100000
vol=[]
graph_x=[]
for loop in range(100):
    print(loop+1,"/ 100")
    x=np.random.random(num)
    y=np.random.random(num)
    count=0
    for i in range(num):
        if x[i]**2+y[i]**2<1:
            count+=1
    vol.append((count/num)*4)
    graph_x.append(loop+1)
mean=np.mean(vol)
std=np.std(vol)
err=std/(np.sqrt(len(vol)))
print("pi =",mean,"±",err)
for i in range(len(vol)):
    if i==0:
        best=vol[i]
        worst=vol[i]
    else:
        if (np.pi-vol[i])**2 < (np.pi-best)**2:
            best=vol[i]
        if (np.pi-vol[i])**2 > (np.pi-worst)**2:
            worst=vol[i]
print("best =",best)
print("worst =",worst)
plt.plot(graph_x,vol)
pi_arr=[]
for i in range(len(vol)):
    pi_arr.append(np.pi)
plt.plot(graph_x,pi_arr,c='r')

mini=np.min(vol)
maxi=np.max(vol)


bw=np.linspace(mini*0.989,maxi*1.011,100)
g_best=[]
g_worst=[]
best_index=vol.index(best)
worst_index=vol.index(worst)
best_x=graph_x[best_index]
worst_x=graph_x[worst_index]

for i in range(len(bw)):
    g_best.append(best_x)
    g_worst.append(worst_x)
plt.plot(g_best,bw,c='orange',label='best')
plt.plot(g_worst,bw,c='g',label='worst')
plt.legend(bbox_to_anchor=(1,1))