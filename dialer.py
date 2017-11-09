#Copyright 2017 Harish N Sathishchandra harishns@bu.edu
#Copyright 2017 Donato Kava dkava@bu.edu
#Copyright 2017 Keval Khara kevalk@bu.edu

'''
This python function 'dialer(file_name,frame_rate,phone,tone_time)' 
creates a WAV file of the sound of a telephone number being dialed.

The parameters are as follows -

file_name, a string representing the name of the WAV file to be created. Do not append ".wav" to this string,

frame_rate, a number representing the number of samples per second to use in the sound,

phone, a string of digits representing a phone number to dial,

tone_time, a number representing the time in seconds of each tone to generate.
'''

import scipy.io.wavfile as wavfile
import numpy as np
def dialer(file_name,frame_rate,phone,tone_time):
    phone_no = []
    output = []

    for i in phone:
       phone_no.append(int(i))

    for i in phone_no:
        if i == 0:
            freq_low = 941
            freq_high = 1336
        if i == 1:
            freq_low = 697
            freq_high = 1209
        if i == 2:
            freq_low = 697
            freq_high = 1336
        if i == 3:
            freq_low = 697
            freq_high = 1477
        if i == 4:
            freq_low = 770
            freq_high = 1209
        if i == 5:
            freq_low = 770
            freq_high = 1336
        if i == 6:
            freq_low = 770
            freq_high = 1477
        if i == 7:
            freq_low = 852
            freq_high = 1209
        if i == 8:
            freq_low = 852
            freq_high = 1336
        if i == 9:
            freq_low = 852
            freq_high = 1477

        discrete = np.linspace(0,tone_time,tone_time*frame_rate,endpoint=False)
        low = np.sin(2*np.pi*freq_low*discrete)
        high = np.sin(2*np.pi*freq_high*discrete)
        out = high + low
        output = np.concatenate([output,out])

    output = np.array(output)
    wavfile.write(file_name,frame_rate,output)

#print(dialer('out',10000,[1,2,3,4,5,6],1))
