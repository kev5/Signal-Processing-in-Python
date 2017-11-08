# Copyright 2017 Keval Khara kevalk@bu.edu
# Copyright 2017 Harish N Sathishchandra harishns@bu.edu
# Copyright 2017 Donato Kava dkava@bu.edu

# Finding the DFT of a signal without using the in-built 'fft' function

from numpy import zeros, exp, array, pi
def DFT(x):
    try:
        N = len(x)
        out = array(1 + zeros((N,),dtype ="complex128"))
        for k in range(N):
            temp = []
            for n in range(N):
                temp.append(x[n]*exp((-2j*pi*n*k)/N))
            y = sum(temp)
            out[k] = y  
        return out
    except:
        raise ValueError
