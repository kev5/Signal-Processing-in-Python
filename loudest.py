# Copyright 2017 Keval Khara kevalk@bu.edu

from numpy.fft import *
import numpy as np
import math
import scipy.io.wavfile as wavefile
import wave
import struct
from numpy import pi, cos, sin

def loudest_band(music, frame_rate, bandwidth):
	# waveFile = wave.open('bach10sec.wav', 'r')
	# length = waveFile.getnframes()
	# samples = []
	# for i in range(0, length):
	# 	waveData = waveFile.readframes(1)
	# 	data = struct.unpack(">h", waveData)
	# 	samples.append(int(data[0]))
	
	samples = np.array(music)
	dft = fft(samples)
	absolute = np.absolute(dft)
	energy = np.square(absolute)

	window = bandwidth * len(energy)/frame_rate

	bands = []
	
	# sliding window
	for i in range(0, (len(energy)//2-int(window) + 1)):
		#maxes[i] = np.amax(energy[i:i+int(window)])
		bands.append(np.sum(energy[i:i+int(window)]))

	index_of_low = bands.index(max(bands))

	low = dft[index_of_low]
	high = low + bandwidth

	loudest = []
	for i in range(0, index_of_low):
		loudest.append(0)
	for i in range(index_of_low, len(energy)//2):
		loudest.append(dft[index_of_low])

	result = loudest + loudest[::-1]

	inverse = ifft(result)

	# wavfile.write('out1',frame_rate,inverse)

	return (low, high, inverse)

print(loudest_band(0.8*cos(2*pi*200*2) + 1.2*sin(2*pi*200* 12), 44100, 4))
# np.array([1.0,2,-3,-3,2,1.0])
