''' 
Small example script used to convert a cosmological power spectrum into
a correlation funciton using LOG_HT.py. 

Joseph E. McEwen 
McEwen Laboratories (c) 2016 
email: jmcewen314@gmail.com
'''


import numpy as np
from LOG_HT import r_to_k, k_to_r 

# load power spectrum data 
data=np.loadtxt('Pk_test.dat')
k=data[:,0]
P=data[:,1]
	
# get correlation function from power spectrum	
r,xi=k_to_r(k,P)
# get power spectrum from correlation function (this is the roundtrip power spectrum) 
k2,P2=r_to_k(r,xi)
	
	
import matplotlib.pyplot as plt

fig=plt.figure()

ax=fig.add_subplot(121)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(r'$r$', size=30)
ax.set_ylabel(r'$\xi(r)$', size=30)
	

ax.plot(r,xi, color='black', label='fftlog-python' )
	
ax.legend()
ax.grid()

ax=fig.add_subplot(122)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(r'$k$', size=30)
ax.set_ylabel(r'$P(k)$', size=30)
	
ax.plot(k,P,color='black',label='original power spectrum')
ax.plot(k2,P2,'--', color='red',label='round trip fftlog-python power spectrum')
	
ax.legend(loc=3,fontsize=10)
ax.grid()	
plt.show()
fig.savefig('HT_example_plot.pdf')
	
	
