import numpy as np
import pandas as pd

lstx=[15,17,20,21,25]
lsty=[9,13,16,18,21]


#1
def Q1():
 ex=np.mean(np.array(lstx))
 ey=np.mean(np.array(lsty))
 cov=0
 for i in range(len(lstx)):
    cov+=((lstx[i]-ex)*(lsty[i]-ey))
 cov=cov/(len(lstx)-1)
 print(cov)

#2
def corr(lstx,lsty):
 vx=0
 vy=0
 ex=np.mean(np.array(lstx))
 ey=np.mean(np.array(lsty))
 cov=0
 for i in range(len(lstx)):
    cov+=((lstx[i]-ex)*(lsty[i]-ey))
 cov=cov/(len(lstx)-1)
 for i in range(len(lstx)):
    vx+=(lstx[i]-ex)**2
    vy+=(lstx[i]-ex)**2
 sdx=(vx/len(lstx)-1)**0.5
 sdy=(vy/len(lstx)-1)**0.5
 corr = cov/(sdx*sdy)
 return corr

#3
df = pd.read_csv('BNG-Device.csv')

ac = df['Active-Count'].tolist()
cpu = df['CPU-Utilization'].tolist()
tmu = df['Total-Memory-Usage'].tolist()
at = df['Average-Temperature'].tolist()
a = corr(ac,cpu)
b = corr(cpu,tmu)
c = corr(cpu,at)
d = corr(ac,at)
e = corr(tmu,at)
corr = [a,b,c,d,e]
print(a,b,c,d,e)
rel=[]
for i in range(len(corr)):
    if(corr[i]==0):
        rel.append('None')
    elif((corr[i]>0 and corr[i] <=0.1) or(corr[i]<0 and corr[i]>=-0.1)):
            rel.append('Weak')
    elif((corr[i]>0.1 and corr[i] <=0.3) or(corr[i]<-0.1 and corr[i]>=-0.3)):
            rel.append('Moderate')
    elif((corr[i]>0.3 and corr[i] <=0.5) or(corr[i]<-0.3 and corr[i]>=-0.5)):
            rel.append('Strong')
    elif((corr[i]>0.5 and corr[i] <=1) or(corr[i]<-0.5 and corr[i]>=-1)):
            rel.append('Very Strong')
    elif( corr[i]==1 or corr[i]==-1):
            rel.append('Perfect')   
    else:
        rel.append('None')  
    
data = pd.DataFrame({'values':corr,'Relation':rel},index=['a','b','c','d','e'])
data['values']=data['values'].fillna(0)
print(data)                                       
