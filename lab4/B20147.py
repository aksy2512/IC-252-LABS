import random
import matplotlib.pyplot as plt
import numpy as np
#Q1
def Q1a():
    N = int(input("Number of times the simulation should happen - "))
    c1 =0
    c2=0
    c3=0
    for i in range(N):
     X1=random.randint(0,1)
     X2=random.randint(0,1)
     if(X1==1):
         c1=c1+1
     if(X2==1):
         c2=c2+1
     if(X1==1 and X2==1):
         c3=c3+1
    print("Probability that X1 = 1 is", c1/N)
    print("Probability that X2 = 1 is", c2/N)
    print("Probability that X1 = 1 and X2 = 1 is", c3/N)       
    print("Probability by hand that X1 and X2 are independent (p(X1=1) * p(X2=1)) is", c1/N*c2/N, "which is approximately equal to the probability that both X1 = 1 and X2 = 1 thus independent") 

def Q1b():
    N = int(input("Number of times the simulation should happen - "))
    c1 =0
    c2=0
    c3=0
    for i in range(N):
     X1=random.randint(0,1)
     X2=random.randint(0,1)
     Z=X1+X2
     if(X1==1):
         c1=c1+1
     if(Z==2):
         c2=c2+1
     if(Z==1 and X1==1):
         c3=c3+1
    print("Probability that X1 = 1 is", c1/N)
    print("Probability that Z = 2 is", c2/N)
    print("Probability that X1 = 1 and Z = 2 is", c3/N)       
    print("Probability by hand that X1 and X2 are independent (p(X1=1) * p( Z=2)) is", c1/N*c2/N, "which is not equal to the probability that both X1 = 1 and Z = 2 thus dependent")
def Q1c():
    N = int(input("Number of times the simulation should happen - "))
    c1 =0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    for i in range(N):
     X1=random.randint(0,1)
     X2=random.randint(0,1)
     Z=X1+X2
     if(X1==1):
         c1=c1+1
     if(X2==1):
         c2=c2+1
     if(Z==1):
         c3=c3+1  
     if(X1==1 and Z==1):
         c4=c4+1
     if(X2==1 and Z==1):
         c5=c5+1    
     if(X1==1 and X2==1 and Z==1):
         c6=c6+1
    print("Probability X1 conditioned Z:", c4/c3)
    print("Probability X2 conditioned Z:", c5/c3)
    print("Probability that X1 conditioned Z and X2 conditioned Z:", c6/c3)
    print("Probability by hand:", c4/c3*c5/c3, "which is not equal to the probability that X1 conditioned Z and X2 conditioned Z thus dependent ")

#2
def Q2():
 N = int(input("Write the value of N: "))
 p = float(input("Write the value of p: "))

 p1 = int(p*100)
 lst = []
 for i in range(100):
   if(i<p1):
       lst.append('H')
   else:
       lst.append('T')    
 values = []
 for j in range(10000):

    count = 0
    for i in range(N):
        trial = random.choice(lst)

        if(trial=='H'):
            count =count+1

    values.append(count)


 plt.title(f'Histogram for number of heads obtained for N={N} and p={p}')
 plt.ylabel('Count')
 plt.xlabel('Frequency of heads')
 plt.hist(values, bins=list(range(1, N+1)))
 plt.grid(True)
 plt.show()


 # Solving using numpy:-
 # np.random.seed(42)
 # size=10000
 # values=np.random.binomial(n=N,p=p,size=size)
 # plt.title('Histogram for number of heads obtained')
 # plt.ylabel('Count')
 # plt.xlabel('Frequency of heads')
 # plt.hist(values, bins=list(range(1, N+1)))
 # plt.show()

#3
def Q3():
 p=float(input("Write the probability for a successful transmission: "))
 p1=int(p*100)
 lst=[]
 for i in range(100):
    if(i<p1):
        lst.append(1)
    else:
        lst.append(0)
 values = []
 for i in range(10000):
    count=0
    x=0
    while(x!=1):
        x=random.choice(lst)
        count=count+1
    values.append(count)
 plt.title(f'Histogram for number of trias needed for p={p} ')
 plt.ylabel('Count')
 plt.xlabel('Frequency of tries')
 plt.hist(values, bins=list(range(1,21)))
 plt.grid(True)
 plt.show()





         