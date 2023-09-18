import numpy as np
#import scipy.stats as norm 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
##from scipy.stats import multivariate_normal
from scipy import stats
#==========================Question 1a===================================
#Write the code for generating the gs variable. 
#This is the simplest random variable of the problem and can be generated independent of the others.
 
#np.random.normal(loc = 7.25,scale = 0.875 ,size = 10000) #mean, Standard deviation, size
gs = np.random.normal(loc = 7.25,scale = 0.875 ,size = 10000)
#sns.distplot(np.random.normal(loc = 7.25,scale = 0.875 ,size = 10000))
sns.distplot(gs)
#plt.show()
print("")

#==========================Question 1b===================================


Sigma = np.matrix('1.0, 0.6, -0.9; 0.6, 1.0, -0.5; -0.9, -0.5, 1.0')

print(Sigma)

mu = np.average(Sigma, axis=0)
print(mu)


mvrnorm = np.random.multivariate_normal([0,0,0],Sigma,10000)

mvrnorm.mean(axis=0)
np.cov(mvrnorm.T)

np.corrcoef(mvrnorm.T)[0,1]
cor =np.corrcoef(mvrnorm.T)[0,1]


plt.plot(mvrnorm[:, 0], mvrnorm[:, 1], '.', alpha=0.5)
plt.axis('equal')
plt.grid()
plt.show()

print(cor)

