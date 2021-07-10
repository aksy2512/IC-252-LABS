import numpy as np
import math

#1
def Q1():
 s = [100,1000,10000] 
 for i in range(len(s)):
  x = np.random.uniform(-1,1 ,s[i] )
  y = np.random.uniform(-1,1,s[i] )
 #print(x)
  x = [round(val, 3) for val in x]
  y = [round(val, 3) for val in y]
  cnt =0
  for j in x:
     for k in y:
         if (j**2+k**2<=1):
             cnt=cnt+1
  print(4*cnt/(s[i]*s[i]))

#2
def Q2():
 s = [100,1000,10000] 
 for i in range(len(s)):
  x = np.random.uniform(0,1 ,s[i] )
  y = np.random.uniform(0,2,s[i] )
 #print(x)
  x = [round(i, 3) for i in x]
  y = [round(i, 3) for i in y]
  cnt =0
 for j in x:
     for k in y:
         if (k-2/(1+j*j)<=0):
             cnt=cnt+1
 print(2*cnt/(s[i]*s[i]))
#3


def f3(arr):
    for i in range(len(arr)):
        if arr[i]==i:
            return 0
    return 1

sizes = [100, 1000, 10000]
for s in sizes:
    ans=0
    for i in range(10000):
        
        k = np.random.permutation(s)
        flag = True
        for j in range(len(k)):
          if(k[j]==j):
             flag = False
             break
        if(flag==True):
            ans = ans +1     
    

    print("For n=", s, " Value of e is {:.5f}".format(10000/ans))