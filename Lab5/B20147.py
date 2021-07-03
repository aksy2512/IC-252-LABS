import random
import matplotlib.pyplot as plt

#Q1
c0 =0
c1=0
for i in range(10000):
    x=random.randint(0,1)

    if(x==1):
        y=random.randint(1,100)
        if(y<=35):
            c0=c0+1
        else:
            c1=c1+1
                
    if(x==0):
        y=random.randint(1,100)
        if(y<=75):
            c0=c0+1
        else:
            c1=c1+1
px0 = c0 / 10000
px1 = c1 / 10000
print(f"Simulation result for p(Y=0) = {px0} and p(Y=1) = {px1}")
print(f"Analytical result for p(Y=0) = {0.75*0.5 + 0.35*0.5} and p(Y=1) = {0.25*0.5+0.65*0.5}")
prob = [px0,px1]
x=["P(Y=0)","P(Y=1)"]
plt.bar(x,prob)
plt.ylabel("Probability")
plt.title("PMF")
plt.grid(True)
plt.show()

#Q2
x0y0=0
x1y0=0
x0y1=0
x1y1=0
x1=0
x0=0
for i in range(10000):
    x=random.randint(0,1)

    if(x==1):
        x1=x1+1
        y=random.randint(1,100)
        if(y<=35):
            x1y0=x1y0+1
        else:
            x1y1=x1y1+1
                
    if(x==0):
        x0=x0+1
        y=random.randint(1,100)
        if(y<=75):
            x0y0=x0y0+1
        else:
            x0y1=x0y1+1
prob=[x0y0/x0,x0y1/x0,x1y0/x1,x1y1/x1]
xaxis = ["P(Y=0|X=0)","P(Y=1|X=0)","P(Y=0|X=1)","P(Y=1|X=1)"]
print(f'Simulation result for P(Y=0|X=0)={prob[0]},P(Y=1|X=0)={prob[1]},P(Y=0|X=1)={prob[2]} and P(Y=1|X=1)={prob[3]}')
plt.grid(True)
plt.bar(xaxis,prob)
plt.ylabel("Probability")
plt.title("Joint PMF")
plt.show()
ax = plt.axes(projection='3d')
x=[0,0,1,1]
y=[0,1,0,1]
ax.scatter(x,y,prob)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("Joint PMF")
plt.show()

