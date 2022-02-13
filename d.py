# import numpy as np
# time = [0,2,4,6,8,10,12,14]
# step = 3
# new_time = [0,]
# amp =[12,23,3223,54,5,6]
# # time_interval = np.arange(0, 100, 0.01)
# # print(len(time_interval))
# import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
# t = np.arange(256)
# sp = np.fft.fft(np.sin(t))
# freq = np.fft.fftfreq(t.shape[-1])
# plt.plot(freq, sp.real, freq, sp.imag)
# plt.show()
# t = np.arange(0, 5, .001)
# x=np.sin(2*np.pi*10*t)+np.sin(2*np.pi*20*t)+np.sin(2*np.pi*50*t)+np.sin(2*np.pi*230*t)
# spectrum = np.fft.fft(x)
# freq = np.fft.fftfreq(len(spectrum))
# threshold = 0.5 * max(abs(spectrum))
# mask = abs(spectrum) > threshold
# peaks = freq[mask]
# peaks=abs(peaks)
# print(max(peaks)*1000)
data1 = pd.read_csv(data)
    t = data1['# t']
    x = data1['x']
    spec = numpy.fft.rfft(x)
    peak = numpy.argmax(spec)
    val = numpy.abs(peak) # Find magnitude
    print(val/6)
    print("2Fmax at: "+str((val/6)*100))   
