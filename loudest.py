# Copyright 2017 Keval Khara kevalk@bu.edu

'''
The Python function 'loudest_band(music,frame_rate,bandwidth)' 
returns a tuple (low,high,loudest) containing information about the loudest part of music.

The input parameters are -

music: an ndarray of shape (N,) representing a continuous time signal which has been digitized. 
Assuming that music is real, and so the Fourier Transform will be conjugate symmetric.

frame_rate: the sampling rate that was used to sample music

bandwidth: the width of the frequency band to be selected (the loudest band)

The output parameters (low,high,loudest) are -

low: the low end of the loudest frequency band in music

high: the high end of the loudest frequency band in music

loudest: a time signal extracted (filtered) from music which contains only the frequencies of music that are in the loudest band.

The units of frame_rate, bandwidth, low, and high are all Hz.
'''

import numpy as np
from scipy.fftpack import fft, ifft

def loudest_band(music, frame_rate, bandwidth):
    size = len(music)
    samples = np.array(music, complex)
    dft = np.empty((size,), complex)
    energy = np.empty((size,), complex)

    dft = fft(samples)
    energy = np.square(np.absolute(dft))
    window = int(bandwidth * size/frame_rate)

    bands = 0
    maximum = 0
    low, high = 0, 0
    for i in range(0, (size//2 - window)):
    	if i==0:
    		bands = np.sum(energy[0:window])
    	else:
    		bands = bands - energy[i-1] + energy[i+window-1]
    	if bands>maximum:
    		maximum = bands
    		low = i 
    		high = low + window

    loudest = np.empty((size,), complex)

    for i in range(0, size):
        if(i >= low and i< high):
            loudest[i] = dft[i]
        elif(i >= (size - high) and i < (size - low)):
            loudest[i] = dft[i]
        else:
            loudest[i] = 0
   
    inverse = ifft(loudest)
 
    low = int(low * frame_rate / size)
    high = low + bandwidth

    return (low, high, inverse)

def main():
    music = np.array([1.0, 2.0, 1.0, -1.0, 1.5, 2.6, 7.2, 2.6, 1.5, -1.0, 1.0, 2.0, 1.0])
    print(loudest_band(music, 1, 2))

if __name__ == '__main__':
    main()
