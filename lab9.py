import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, norm

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
