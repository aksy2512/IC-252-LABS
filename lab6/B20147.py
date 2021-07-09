import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Exp(lst):
    return sum(lst)/len(lst)
def Var(lst):
    m = Exp(lst)
    v=0
    for i in lst:
        v+=(i-m)**2
    return v/(len(lst)-1)
def Q1():        
 df = pd.read_csv("lab6/Covid19IndiaData_30032020.csv")
 #a
 plt.hist(df['Age'] ,bins = [i for i in range(0,101,1)], density = True,edgecolor="black")
 print('The expectation of the age of infected person is ',Exp(df['Age']))
 print('The Varaiance of the age of infected person is',Var(df['Age']))
 plt.xlabel('Ages')
 plt.ylabel('Probabilities')
 plt.title('PMF for Infected Ages')
 plt.grid(True)
 plt.show()
 #b
 data = df.loc[df['StatusCode']=='Recovered' ]
 plt.hist(data['Age'] ,bins = [i for i in range(0,101,1)], density = True,edgecolor="black")
 plt.grid(True)
 plt.xlabel('Ages')
 plt.ylabel('Probabilities')
 plt.title('PMF for Recovered Ages')
 plt.show()
 print('The expectation of the age of Recovered person is ',Exp(data['Age']))
 print('The Variance of the age of Recovered person is ',Var(data['Age']))

 dat = df.loc[df['StatusCode']=='Dead' ]
 plt.hist(dat['Age'] ,bins = [i for i in range(0,101,1)], density = True,edgecolor="black")
 plt.grid(True)
 plt.xlabel('Ages')
 plt.ylabel('Probabilities')
 plt.title('PMF for Dead Ages')
 plt.show()
 print('The expectation of the age of Dead person is ',Exp(dat['Age']))
 print('The variance of the age of Dead person is ',Var(dat['Age']))

 #c
 dats = df.loc[df['GenderCode0F1M']==0 ]
 plt.hist(dats['Age'] ,bins = [i for i in range(0,101,1)], density = True,edgecolor="black")
 plt.grid(True)
 plt.xlabel('Ages')
 plt.ylabel('Probabilities')
 plt.title('PMF for Female Infected Ages')
 plt.show()
 print('Conditional Expectation of the age of all infected patients of the Female patient is',Exp(dats['Age']))
 print('Conditional Variance of the age of all infected patients of the Female patient is',Var(dats['Age']))

 dats = df.loc[df['GenderCode0F1M']==1 ]
 plt.hist(dats['Age'] ,bins = [i for i in range(0,101,1)], density = True,edgecolor="black")
 plt.grid(True)
 plt.xlabel('Ages')
 plt.ylabel('Probabilities')
 plt.title('PMF for Male Infected Ages')
 plt.show()
 print('Conditional Expectation of the age of all infected patients of the Male patient is',Exp(dats['Age']))
 print('Conditional Variance of the age of all infected patients of the Male patient is',Var(dats['Age']))

def Q2():
    death = pd.read_excel('lab6/linton_supp_tableS1_S2_8Feb2020.xlsx',sheet_name=1)
    export = pd.read_excel('lab6/linton_supp_tableS1_S2_8Feb2020.xlsx',sheet_name=0)
    #2a
    exp = export.dropna(how='all', axis='columns')
    eo = exp.dropna(subset = ['ExposureL', 'Onset'])
    dur = eo['Onset'] - eo['ExposureL']

    
    dur = dur.dt.days.astype('int32')
    plt.hist(dur,bins =[i for i in range(0,36,1)], density = True,edgecolor="red")
    plt.grid(True)
    plt.xlabel("Days")
    plt.ylabel('Probabilities')
    plt.title('PMF of the incubation period')
    plt.show()
    print('The mean incubation period is', Exp(dur))
    print('The Variance of the distribution is',Var(dur))

    #2b
    q2 = eo.loc[exp['ExposureType']!='Lives-works-studies in Wuhan']
    dur = q2['Onset'] - q2['ExposureL']


    dur = dur.dt.days.astype('int32')
    plt.hist(dur,bins =[i for i in range(0,36,1)], density = True,edgecolor="red")
    plt.grid(True)
    plt.xlabel("Days")
    plt.ylabel('Probabilities')
    plt.title('PMF of the incubation period excluding Wuhan residents')
    plt.show()
    print('The mean incubation period by excluding Wuhan residents is', Exp(dur))
    print('The Variance of the distribution by excluding Wuhan residents is',Var(dur))

    #2c
    fig,axs = plt.subplots(1,3,figsize=(12,4))
    oh = death.dropna(subset=['Onset','Hospitalization/Isolation'])
    dur =  oh['Hospitalization/Isolation'] - oh['Onset'] 
    dur = dur.dt.days.astype('int32')
    axs[0].hist(dur,bins =[i for i in range(0,36,1)], density = True,edgecolor="red")
    axs[0].grid(True)
    axs[0].set(xlabel ="Days" ,ylabel = 'Probabilities')
   
    axs[0].set_title('PMF of the onset to hospitalization (H-O) for the dead patients')

    

    od = death.dropna(subset=['Onset','Death'])
    dur = od['Death'] - od['Onset'] 
    dur = dur.dt.days.astype('int32')
    axs[1].hist(dur,bins =[i for i in range(0,36,1)], density = True,edgecolor="red")
    axs[1].grid(True)
    
    axs[1].set(xlabel ="Days" ,ylabel = 'Probabilities')
    axs[1].set_title('PMF of the onset to death (X-O) for the dead patients')

    hd = death.dropna(subset=['Hospitalization/Isolation','Death'])
    dur = hd['Death'] - hd['Hospitalization/Isolation'] 
    dur = dur.dt.days.astype('int32')
    axs[2].hist(dur,bins =[i for i in range(0,36,1)], density = True,edgecolor="red")
    axs[2].grid(True)
    
    axs[2].set(xlabel ="Days" ,ylabel = 'Probabilities')
    axs[2].set_title('PMF of the hospitalization to death (X-H) for the dead patients')
    plt.tight_layout()
    plt.show()

    do = exp.dropna(subset = ['DateHospitalizedIsolated', 'Onset'])
    dur =  do['DateHospitalizedIsolated'] - do['Onset']


    dur = dur.dt.days.astype('int32')
    plt.hist(dur,bins =[i for i in range(0,36,1)], density = True,edgecolor="red")
    plt.grid(True)
    plt.xlabel("Days")
    plt.ylabel('Probabilities')
    plt.title('PMF of the onset to hospitalization (H-O) for the surviving patients')
    plt.show()

    
