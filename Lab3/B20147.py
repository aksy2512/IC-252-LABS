import random
import matplotlib.pyplot as plt
from collections import Counter

#Q1

def Q1():
 def die2coin(m,n):
  if(m==1):   
     
   d = random.randint(1,6)
   if(d==1 or d==2 or d==3):
        return 'H'
   else:
        return 'T'

  elif(m==2):  
   
   d = random.randint(1,6)
   if(d==1):
        return 'H'
   elif(d==2):
        return 'T'
  else:
   
    d = random.randint(1,6)
    if(d%2==0):
        return 'H'
    else:
        return 'T'
   
 m=int(input("Write the type of method :"))
 n= int(input("Write the number of times the trial should repeat :")) 
 phs = []
 pts=[]
 ch=0
 ct=0
 for i in range(1,n+1):
  tr = die2coin(m,n)
  if(tr=='H'):
    ch=ch+1
  elif(tr=='T'):
      ct=ct+1
  pts.append(ct)
  phs.append(ch)       
 plt.plot([i for i in range(1,n+1)],phs)
 plt.plot([i for i in range(1,n+1)],pts)
 plt.xlabel("Number of trials (n)") 
 plt.ylabel('Number of heads and tails')
 if(m==1):
     plt.title("Q1 - Method1")
 elif(m==2):
     plt.title("Q1 - Method2")    
 else:
     plt.title("Q1 - Method3")
 plt.legend(["Heads", "Tails"])
 plt.grid(True)
 plt.show() 

#2
def Q2():
    def die2biasedcoin(n):
            d=random.randint(1,6)
            if(d==1 or d==2):
                return 'H'
            else:
                return 'T'        
    n= int(input("Write the number of times the trial should repeat :")) 
    phs = []
    pts=[]
    ch=0
    ct=0
    for i in range(1,n+1):
     tr = die2biasedcoin(n)
     if(tr=='H'):
      ch=ch+1
     elif(tr=='T'):
      ct=ct+1
     pts.append(ct)
     phs.append(ch)       
    plt.plot([i for i in range(1,n+1)],phs)
    plt.plot([i for i in range(1,n+1)],pts)
    plt.xlabel("Number of trials (n)") 
    plt.ylabel('Number of heads and tails')
    plt.legend(["Heads", "Tails"])
    plt.title("Q2")
    plt.grid(True)
    plt.show() 

#3
  #a
def Q3a():
   count=[]
   coun = Counter()
   for n in range(1,367):
      b=random.randint(1,365)
      coun.update([b])
      c=n-len(coun)
      count.append(c)
   plt.plot([i for i in range(1,367)],count)
   plt.ylabel("Number of common Birthdays")
   plt.xlabel("Number of Birthdays")
   plt.title("Q3a")
   plt.grid(True)
   plt.show()
  #b
def Q3b():
   count=[]
   coun = Counter()
   for n in range(1,367):
      b=random.randint(1,687)
      coun.update([b])
      c=n-len(coun)
      count.append(c)
   plt.plot([i for i in range(1,367)],count)
   plt.ylabel("Number of common Birthdays")
   plt.xlabel("Number of Birthdays")
   plt.title('Q3b')
   plt.grid(True)
   plt.show() 
 #c
def Q3c():
    count =0
    for i in range(1000):
        coun = Counter()
        for n in range(1,51):
            b=random.randint(1,365)
            coun.update([b])
        c=50-len(coun)+1
        if(c>=2):
           count=count+1
    prob=count/1000
    print("The required probability is",prob)
def Q3d():
   count=[]
   coun = Counter()
   for n in range(1,367):
      if(n<=244):
       b=random.randint(1,150)
      else:
        b=random.randint(151,365)   
      coun.update([b])
      c=n-len(coun)
      count.append(c)
   plt.plot([i for i in range(1,367)],count)
   plt.ylabel("Number of common Birthdays")
   plt.xlabel("Number of Birthdays")
   plt.title("Q3d")
   plt.grid(True)
   plt.show()
Q3c()

