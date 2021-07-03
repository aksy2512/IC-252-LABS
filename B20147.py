

#Q1
def Q1():
 P = float(input())
 R = float(input())
 prob = (P*(1-R))/(P*(1-R)+R*(1-P))
 print(prob)

#Q2
def Q2():
 x = int(input("Enter the number of Type1 transistors :"))
 y = int(input("Enter the number of Type2 transistors :"))
 z = int(input("Enter the number of Type3 transistors :"))
 sum = x+y+z
 prob = z/(y+z)
 print(f'The required probability is {prob}')

def Q3():
 file = open('fileA-TimeMachine.txt','r',encoding="utf8")
 data = file.read().replace(" ","")
 count =0
 for i in data:
    if(i==' ' or i=='.' or i==':' or i==',' or i=='-'):
        continue
    elif(i.isalpha()):
        count=count+1
 data=data.lower()
 X=input("Write the first alphabet: ")
 Y=input("Write the second alphabet: ")
 X=X.lower()
 Y=Y.lower()
 cx=0
 cy=0
 for i in data:
    if(i==X):
        cx=cx+1
    if(i==Y):
     cy=cy+1

#a
 probx = cx/count
 print(f'Probability of {X} is {probx}')
#b
 proby = cy/count
 print(f'Probability of {Y} is {proby}')
#c
# X given Y
 Z1=Y+X

 p1=(data.count(Z1))/(data.count(Y))
 print(f'Probability of occurrence of X given Y is {p1}')

# Y given X
 Z2=X+Y
 p2=(data.count(Z2))/(data.count(X))
 print("Probability of occurrence of Y given X is",p2)


Q3()