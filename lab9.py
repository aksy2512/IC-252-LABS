import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, norm
import seaborn as sea
import threading


m = [10,100,500,1000,5000,10000,50000]
exp=[]
unif = []
bern = []

for i in range(len(m)):
    exp.append(np.mean(np.random.exponential(1,m[i])))
    unif.append(np.mean(np.random.uniform(1,2,m[i])))
    bern.append(np.mean(bernoulli.rvs(p=0.2,size=m[i])))
fig,axs = plt.subplots(1,3,figsize=(12,4))
axs[0].plot(m,exp,color='b',linestyle ='solid')
axs[0].plot(m,[1,1,1,1,1,1,1],color = 'r',linestyle='dashdot')
axs[0].set_title("Exponential")
axs[0].grid(True)

axs[1].plot(m,unif,color='b',linestyle ='solid')
axs[1].plot(m,[1.5,1.5,1.5,1.5,1.5,1.5,1.5],color = 'r',linestyle='dashdot')
axs[1].set_title("Uniform")
axs[1].grid(True)

axs[2].plot(m,bern,color='b',linestyle ='solid')
axs[2].plot(m,[0.2,0.2,0.2,0.2,0.2,0.2,0.2],color = 'r',linestyle='dashdot')
axs[2].set_title("Bernoulli")
axs[2].grid(True)
plt.suptitle("DEMONSTRATION OF WLLN")
plt.show()

#2
def varexp(lamda):
   return (1/lamda)*(1/lamda)

def varunif(a,b):
    return (b-a)*(b-a)/12

def varbern(p):
    return p*(1-p)

#a
#1
ex=[]
uni = []
ber = []
n=[1,2,4,8,16,32]
for i in n:
    exp=np.zeros(1000)
    unif = np.zeros(1000)
    bern = np.zeros(1000)
    for j in range(i):
       exp=exp+np.random.exponential(1,1000)
       unif = unif + np.random.uniform(1,2,1000)
       bern = bern + bernoulli.rvs(p=0.2,size=1000)
    ex.append(exp/i)
    uni.append(unif/i)
    ber.append(bern/i)



# plt.plot([i for i in range(1000)],ex)
# plt.plot([i for i in range(1000)],n)
#2b
fig,axs = plt.subplots(2,3,figsize=(12,4))
count, bins, ignored = axs[0][0].hist(uni[0], 200, density=True)
axs[0][0].plot(bins, norm.pdf(bins, loc=np.mean(uni[0]),scale = (varunif(1,2)/n[0])**0.5), linestyle="dashdot")
axs[0][0].set_title("n=1")

count, bins, ignored = axs[0][1].hist(uni[1], 200,density=True)
axs[0][1].plot(bins, norm.pdf(bins, loc = np.mean(uni[1]),scale = (varunif(1,2)/n[1])**0.5), linestyle="dashdot")
axs[0][1].set_title("n=2")
count, bins, ignored = axs[0][2].hist(uni[2],200, density=True)
axs[0][2].plot(bins, norm.pdf(bins, loc= np.mean(uni[2]), scale = (varunif(1,2)/n[2])**0.5), linestyle="dashdot")
axs[0][2].set_title("n=4")
count, bins, ignored = axs[1][0].hist(uni[3], 200,density=True)
axs[1][0].plot(bins, norm.pdf(bins, loc=np.mean(uni[3]),scale = (varunif(1,2)/n[3])**0.5), linestyle="dashdot")
axs[1][0].set_title("n=8")
count, bins, ignored = axs[1][1].hist(uni[4],200, density=True)
axs[1][1].plot(bins, norm.pdf(bins, loc=np.mean(uni[4]),scale =(varunif(1,2)/n[4])**0.5), linestyle="dashdot")
axs[1][1].set_title("n=16")
count, bins, ignored = axs[1][2].hist(uni[5],200,density=True)
axs[1][2].plot(bins, norm.pdf(bins, loc=np.mean(uni[5]),scale =(varunif(1,2)/n[5])**0.5), linestyle="dashdot")
axs[1][2].set_title("n=32")
plt.suptitle("CLT FOR UNIFORM DISTRIBUTION")
plt.show()


#
#2c
fig,axs = plt.subplots(2,3,figsize=(12,4))
count, bins, ignored = axs[0][0].hist(ber[0], density=True)
axs[0][0].plot(bins, norm.pdf(bins, loc=np.mean(ber[0]),scale = (varbern(0.2)/n[0])**0.5), linestyle="dashdot")
axs[0][0].set_title("n=1")
count, bins, ignored = axs[0][1].hist(ber[1],density=True)
axs[0][1].plot(bins, norm.pdf(bins, loc = np.mean(ber[1]),scale = (varbern(0.2)/n[1])**0.5), linestyle="dashdot")
axs[0][1].set_title("n=2")
count, bins, ignored = axs[0][2].hist(ber[2], density=True)
axs[0][2].plot(bins, norm.pdf(bins, loc= np.mean(ber[2]), scale = (varbern(0.2)/n[2])**0.5), linestyle="dashdot")
axs[0][2].set_title("n=4")
count, bins, ignored = axs[1][0].hist(ber[3],density=True)
axs[1][0].plot(bins, norm.pdf(bins, loc=np.mean(ber[3]),scale = (varbern(0.2)/n[3])**0.5), linestyle="dashdot")
axs[1][0].set_title("n=8")
count, bins, ignored = axs[1][1].hist(ber[4], density=True)
axs[1][1].plot(bins, norm.pdf(bins, loc=np.mean(ber[4]),scale =(varbern(0.2)/n[4])**0.5), linestyle="dashdot")
axs[1][1].set_title("n=16")
count, bins, ignored = axs[1][2].hist(ber[5],density=True)
axs[1][2].plot(bins, norm.pdf(bins, loc=np.mean(ber[5]),scale =(varbern(0.2)/n[5])**0.5), linestyle="dashdot")
axs[1][2].set_title("n=32")
plt.suptitle("CLT FOR BERNOULLI DISTRIBUTION")
plt.show()
#2c
fig,axs = plt.subplots(2,3,figsize=(12,4))
count, bins, ignored = axs[0][0].hist(ex[0], 100, density=True)
axs[0][0].plot(bins, norm.pdf(bins, loc=np.mean(ex[0]),scale = (varexp(1)/n[0])**0.5), linestyle="dashdot")
axs[0][0].set_title("n=1")
count, bins, ignored = axs[0][1].hist(ex[1], 100,density=True)
axs[0][1].plot(bins, norm.pdf(bins, loc = np.mean(ex[1]),scale = (varexp(1)/n[1])**0.5), linestyle="dashdot")
axs[0][1].set_title("n=2")
count, bins, ignored = axs[0][2].hist(ex[2],100, density=True)
axs[0][2].plot(bins, norm.pdf(bins, loc= np.mean(ex[2]), scale = (varexp(1)/n[2])**0.5), linestyle="dashdot")
axs[0][2].set_title("n=4")
count, bins, ignored = axs[1][0].hist(ex[3], 100,density=True)
axs[1][0].plot(bins, norm.pdf(bins, loc=np.mean(ex[3]),scale = (varexp(1)/n[3])**0.5), linestyle="dashdot")
axs[1][0].set_title("n=8")
count, bins, ignored = axs[1][1].hist(ex[4],100, density=True)
axs[1][1].plot(bins, norm.pdf(bins, loc=np.mean(ex[4]),scale =(varexp(1)/n[4])**0.5), linestyle="dashdot")
axs[1][1].set_title("n=16")
count, bins, ignored = axs[1][2].hist(ex[5],100,density=True)
axs[1][2].plot(bins, norm.pdf(bins, loc=np.mean(ex[5]),scale =(varexp(1)/n[5])**0.5), linestyle="dashdot")
axs[1][2].set_title("n=32")
plt.suptitle("CLT FOR EXPONENTIAL DISTRIBUTION")
plt.show()

