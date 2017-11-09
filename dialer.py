#Copyright 2017 Harish N Sathishchandra harishns@bu.edu
#Copyright 2017 Donato Kava dkava@bu.edu
#Copyright 2017 Keval Khara kevalk@bu.edu

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
