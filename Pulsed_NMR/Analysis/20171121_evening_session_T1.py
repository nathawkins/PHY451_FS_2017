import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as cf

amp = np.array([5.66, 5.4, 5.3, 5.2, 5.1, 4.84, 4.7, 4.56])
amp_u = np.array([0.04, 0.1, 0.05, 0.04, 0.05, 0.04, 0.1, 0.04])
time = np.array([500, 800, 1600, 1800, 2100, 2500, 2800, 3200])

sample_type = "0.1 M $CuSO_4$"

def decay(t, A, b):
    return A*np.exp(-t/b)

popt, pcov = cf(decay, time, amp, p0 = [10, 1E4])

plt.title("$T_1$ Hand Measured Analysis")
plt.errorbar(time, amp, yerr = amp_u, fmt = 'o', label = "Hand Taken Data", fillstyle = "none")
plt.plot(time, decay(time, *popt), label = "Fit $Ae^{-t/T_2}$")
plt.legend()
plt.xlabel("Time Delay Between $\pi$ and $\pi/2$ Pulses ($\mu$s)")
plt.ylabel("Echo Amplitude (mV)")
plt.text(max(time)/2-min(time), max(amp), "$T_1$ = {} $\mu$s".format(round(popt[-1], 3)))
plt.text(min(time), min(amp), sample_type)
# plt.show()
plt.savefig("../Plots/20171121_hand_measured_T1_cuso4.png")
