# LOG_HT 
LOG_HT is python module to perform Hankel transforms when the input signal is log sampled. The code calculates:

F(k)= \int_0^\infty f(r) (kr)^q J_\mu(kr) k dr 

f(r)= \int_0^\infty F(k) (kr)^{-q} J_\mu(kr) r dk , 

when f(r)/F(k) are input data that are sample in log space. 


LOG_HT is very fast! The algorithm is due to Andrew Hamilton (see http://casa.colorado.edu/~ajsh/FFTLog/) and
was originally inteded for cosmological correlation function and power spectrum calcualtions. 


I (Joseph McEwen) have rewritten the code in python. 


See the code LOG_HT_cosmo_test.py as an example of usage. 
