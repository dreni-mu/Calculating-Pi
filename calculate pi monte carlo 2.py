#calculate pi using monte carlo integration
import numpy as np
import matplotlib.pyplot as plt
import random as r

#draw the square
sq_x=[0,2,2,0,0]
sq_y=[2,2,0,0,2]

#draw the circle
c_x=np.linspace(0,2,1000000)
c_y1=[]
c_y2=[]
for i in c_x:
    y_coord=np.sqrt(1-((i-1)**2))+1
    c_y1.append(y_coord)
    c_y2.append(2-y_coord)

#monte carlo part :)
x=[]
y=[]
total=0
count=0
for i in range(100):
    total+=1
    ran_x=r.random()*2
    ran_y=r.random()*2
    x.append(ran_x)
    y.append(ran_y)
    
    #count in circle
    if (((ran_x-1)**2)+((ran_y-1)**2))<1:
        count+=1
#plot at very end
f,ax=plt.subplots()
ax.set_aspect('equal',adjustable='box')
ax.plot(sq_x,sq_y,c='k') #plots the square
ax.plot(c_x,c_y1,c='k')
ax.plot(c_x,c_y2,c='k')
ax.scatter(x,y,marker='.',s=1,c='r')
print('count=',count,'   total=',total)
print('pi is approximately:',(count/total)*4)