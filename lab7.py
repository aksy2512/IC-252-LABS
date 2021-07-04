import numpy as np
import pandas as pd

lstx=[15,17,20,21,25]
lsty=[9,13,16,18,21]
ex=np.mean(np.array(lstx))
ey=np.mean(np.array(lsty))

#1
cov=0
for i in range(len(lstx)):
    cov+=((lstx[i]-ex)*(lsty[i]-ey))
cov=cov/(len(lstx)-1)
print(cov)

#2
vx=0
vy=0
for i in range(len(lstx)):
    vx+=(lstx[i]-ex)**2
    vy+=(lstx[i]-ex)**2
sdx=(vx/len(lstx)-1)**0.5
sdy=(vy/len(lstx)-1)**0.5
corr = cov/(sdx*sdy)
print(corr)
