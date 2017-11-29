import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as cf

time_type = "$T_2$"

data_dir = "../Data/"
prefix = "2017-11-28-"
suffix = "-pulse-NMR-data"

T2_files = ["105856", "111023", "112038", "112817", "113807", "183508", "183928", "114941", "115303", "115554", "115933", "120402", "184420", "184623"]

sample_names = ["0.1M $CuSO_4$", "0.05M $CuSO_4$", "0.04M $CuSO_4$", "0.03M $CuSO_4$", "0.02M $CuSO_4$", "0.07M $CuSO_4$", "0.09M $CuSO_4$", "0.05M $FeCl_3$", "0.1M $FeCl_3$", "0.04M $FeCl_3$", "0.03M $FeCl_3$", "0.02M $FeCl_3$", "0.07M $FeCl_3$", "0.09M $FeCl_3$"]

T2_values = []
T2_uncertainties = []
concentrations = [0.1, 0.05, 0.04, 0.03, 0.02, 0.07, 0.09, 0.05, 0.1, 0.04, 0.03, 0.02, 0.07, 0.09]

for i in range(len(T2_files)):
    number = T2_files[i]
    sample_type = sample_names[i]

    print("Working on {}, {}". format(number, sample_type))

    filename = prefix + number + suffix

    data = np.loadtxt(data_dir+filename+".txt", delimiter = '\t', skiprows = 1)
    amp = data[:,0]
    time = data[:,1]
    width = data[:,2]
    residuals = data[:,3]

    uncertainty = 100*(max(width)**2 + abs(max(amp)-max(residuals))**2)**(1/2)
    T2_uncertainties.append(uncertainty)

    def decay(t, A, b):
        return A*np.exp(-t/b)

    popt, pcov = cf(decay, time, amp, p0 = [10, 7E-3])

    T2_values.append(1000*popt[-1])

    plt.figure()
    plt.title(time_type + " Digital Data Analysis " + filename)
    plt.errorbar(time, amp, xerr = width/2, yerr = 0.1E-3, capsize=3, elinewidth=1, fmt = 'o', label = "Digital Data", fillstyle = "none")
    plt.plot(time, decay(time, *popt), label = "Fit $Ae^{-t/T_2}$")
    plt.xlabel("Time Delay Between $\pi/2$ and $\pi$ Pulses (s)")
    plt.ylabel("Gaussian Fit Amplitude (V)")
    plt.text(max(time)/2, max(amp), "$T_2$ = {} $\pm$ {} ms".format(round(1000*popt[-1], 3), round(uncertainty,3)))
    plt.text(min(time), min(amp), sample_type)
    plt.savefig("../Plots/"+filename+".png")

plt.figure()
plt.xlabel("Concentration (M)")
plt.ylabel("$T_2$ (ms)")
# plt.title("$T_2$ Values Versus Concentration, $CuSO_4$")
# plt.errorbar(concentrations[0:7], T2_values[0:7], yerr = 2*np.array(T2_uncertainties[0:7]), capsize=3, elinewidth=1, fmt = 'o', fillstyle = 'none')
# plt.savefig("../Plots/"+"T2_concentrations_cuso4.png")
plt.title("$T_2$ Values Versus Concentration, $FeCl_3$")
plt.errorbar(concentrations[8:15], T2_values[8:15], yerr = T2_uncertainties[8:15], capsize=3, elinewidth=1, fmt = 'o', fillstyle = 'none')
plt.savefig("../Plots/"+"T2_concentrations_fecl3.png")
