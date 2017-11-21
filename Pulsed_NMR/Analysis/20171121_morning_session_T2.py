import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as cf

data_dir = "../Data/"

filename = "2017-11-21-113723-pulse-NMR-data"
sample_type = "0.1 M $FeCl_3$"

# filename = "2017-11-21-110112-pulse-NMR-data"
# sample_type = "0.1 M $CuSO_4$"



data = np.loadtxt(data_dir+filename+".txt", delimiter = '\t', skiprows = 1)
amp = data[:,0]
time = data[:,1]
width = data[:,2]
residuals = data[:,3]

def decay(t, A, b):
    return A*np.exp(-t/b)

popt, pcov = cf(decay, time, amp, p0 = [10, 7E-3])

plt.title("$T_2$ Digital Data Analysis " + filename)
plt.errorbar(time, amp, xerr = width/2, yerr = 0.1E-3, fmt = 'o', label = "Digital Data", fillstyle = "none")
plt.plot(time, decay(time, *popt), label = "Fit $Ae^{-t/T_2}$")
plt.legend()
plt.xlabel("Time Delay Between $\pi/2$ and $\pi$ Pulses (s)")
plt.ylabel("Gaussian Fit Amplitude (V)")
plt.text(max(time)/2, max(amp), "$T_2$ = {} s".format(round(popt[-1], 6)))
plt.text(min(time), min(amp), sample_type)
plt.savefig("../Plots/"+filename+".png")
# plt.show()


# plt.hist(amp-decay(time, *popt), 20)
# plt.title("Histogram of Residuals from Exponential Fit")
# plt.ylabel("Counts")
# plt.xlabel("Residuals")
# plt.show()
