import numpy as np
import pandas as pd




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
    vx=vx+(lstx[i]-ex)**2
    vy=vy+(lsty[i]-ey)**2
 sdx=(vx/(len(lstx)-1))**0.5
 sdy=(vy/(len(lsty)-1))**0.5
 ans = cov/(sdx*sdy)
 return ans

#3

df = pd.read_csv('Lab 7/BNG-Device.csv')

ac = df['Active-Count'].tolist()
cpu = df['CPU-Utilization'].tolist()
tmu = df['Total-Memory-Usage'].tolist()
at = df['Average-Temperature'].tolist()
a = corr(ac,cpu)
b = corr(cpu,tmu)
c = corr(cpu,at)
d = corr(ac,at)
e = corr(tmu,at)
val = [a,b,c,d,e]
print(a,b,c,d,e)
rel=[]
for i in range(len(val)):
 if(val[i]==0):
  rel.append('None')
 elif((val[i]>0 and val[i] <=0.1) or(val[i]<0 and val[i]>=-0.1)):
        rel.append('Weak')
 elif((val[i]>0.1 and val[i] <=0.3) or(val[i]<-0.1 and val[i]>=-0.3)):
        rel.append('Moderate')
 elif((val[i]>0.3 and val[i] <=0.5) or(val[i]<-0.3 and val[i]>=-0.5)):
        rel.append('Strong')
 elif((val[i]>0.5 and val[i] <=1) or(val[i]<-0.5 and val[i]>=-1)):
        rel.append('Very Strong')
 elif( val[i]==1 or val[i]==-1):
        rel.append('Perfect')   
 else:
  rel.append('None')  

data = pd.DataFrame({'values':val,'Relation':rel},index=['a','b','c','d','e'])
data['values']=data['values'].fillna(0)
print(data)  

lstx=[15,17,20,21,25]
lsty=[9,13,16,18,21]
print(corr(lstx,lsty))
