import random as rd
import math

#Q1
def Q1():
 N = int(input("Write the number of founders :" ))
 M = int(input("Write the number of board positions :"))
 prob = 100/math.perm(N,M)
 print(f'The required probability is {prob} % ')

#Q2
def Q2():
 N = int(input("Write the number of cards :"))
 D = int(input("Write the no. of cards in a hand between 6 to 8 :"))
 prob = 100*math.comb(N-4,D-4)/math.comb(N,8)
 print(f'The required probability is {prob} % ')

#Q3
def Q3():
 count=0
 for i in range(10000000):
     x1 = rd.randint(1,6)
     x2 = rd.randint(1,6)
     sum = x1+x2
     if(sum%2==1 or sum>8):
         count = count +1
 prob = 100*count/10000000
 print(f'The required probability is {prob} % ') 

Q3()       