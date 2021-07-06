import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #1A
X = np.linspace(0,0.3,300)
Y=[]
for i in range(len(X)):
    Y.append(57*np.exp(-57*X[i]))
plt.xlabel("Wait time in hours")
plt.ylabel("Probability density")
plt.title("Exponential Distribution")
plt.plot(X,Y)    
plt.show() 

# #1B
ans = 1-np.exp(-57*(1/60))
print(f'Probability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute is {ans}')

#1C
c=1-np.exp(-57*(2/60)) - 1+np.exp(-57*(1/60))
print(f'Probability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes is {c}')

#1D
d=np.exp(-57*(2/60))
print(f'probability of the wait time for the next Covid-19 confirmed case to be more than 2 minutes is {d}')

#1E
e=1-np.exp(-57*2*(2/60)) - 1+np.exp(-57*2*(1/60))
print(f'probability of wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes when the average number of cases per hour is doubled is {e}')

#2A
df = pd.read_csv("lab8/IC252_Lab8.csv")
df.Status[df.Status=="Recovered"]=2
df.Status[df.Status=="Hospitalized"]=1
df.Status[df.Status=="Dead"]=3

#2B
st = df["Status"].tolist()
pop = df["Population"].tolist()
sr = df["SexRatio"].tolist()
lit = df["Literacy"].tolist()
ag = df["Age"].tolist()
smt = df["SmellTrend"].tolist()
ge = df["Gender"].tolist()

a = np.corrcoef(st,pop)[0,1]
b = np.corrcoef(st,sr)[0,1]
c = np.corrcoef(st,lit)[0,1]
d = np.corrcoef(st,ag)[0,1]
e = np.corrcoef(st,smt)[0,1]
f = np.corrcoef(st,ge)[0,1]
val = [a,b,c,d,e,f]
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

data = pd.DataFrame({'values':val,'Relation':rel},index=['a','b','c','d','e','f'])
data['values']=data['values'].fillna(0)
print(data)  


