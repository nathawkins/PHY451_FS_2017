import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as cf

time_type = "$T_1$"

data_dir = "../Data/"
prefix = "2017-11-28-"
suffix = "-pulse-NMR-data"

T1_files = ["190345", "194315", "193909", "191139", "191848", "192518", "193141"]

sample_names = ["0.1M $CuSO_4$", "0.09M $CuSO_4$","0.07M $CuSO_4$",  "0.05M $CuSO_4$", "0.04M $CuSO_4$", "0.03M $CuSO_4$", "0.02M $CuSO_4$"]

T1_values = []
T1_uncertainties = []
concentrations = [0.1, 0.09, 0.07, 0.05, 0.04, 0.03, 0.02]

for i in range(len(T1_files)):
    number = T1_files[i]
    sample_type = sample_names[i]

    print("Working on {}, {}". format(number, sample_type))

    filename = prefix + number + suffix

    data = np.loadtxt(data_dir+filename+".txt", delimiter = '\t', skiprows = 1)
    amp = data[:,0]
    amp = -1*np.array(amp)
    time = data[:,1]
    width = data[:,2]
    residuals = data[:,3]


    uncertainty = 100*(max(width)**2 + abs(max(amp)-max(residuals))**2)**(1/2)
    T1_uncertainties.append(uncertainty)

    def decay(t, A, b):
        return A*(1-2*np.exp(-t/b))

    to_remove = []
    for k in range(len(width)):
        if abs(width[k]) > np.mean(width):
            to_remove.append(k)

    print(to_remove)


    amp = [amp[j] for j in range(len(amp)) if j not in to_remove]
    time = [time[j] for j in range(len(time)) if j not in to_remove]
    width = [width[j] for j in range(len(width)) if j not in to_remove]

    time = np.array(time)

    popt, pcov = cf(decay, time, amp, p0 = [max(amp), 10E-3])

    T1_values.append(1000*popt[-1])

    plt.figure()
    plt.title(time_type + " Digital Data Analysis " + filename)
    plt.errorbar(time, amp, xerr = np.array(width)/2, yerr = 0.1E-3, capsize=3, elinewidth=1, fmt = 'o', label = "Digital Data", fillstyle = "none")
    plt.plot(time, decay(time, *popt))
    plt.xlabel("Time Delay Between $\pi$ and $\pi/2$ Pulses (s)")
    plt.ylabel("Gaussian Fit Amplitude (V)")
    plt.text(max(time)/3, max(amp), "$T_1$ = {} $\pm$ {} ms".format(round(1000*popt[-1], 3), round(uncertainty,3)))
    plt.text(2*min(time), min(amp), sample_type)
    plt.savefig("../Plots/"+filename+".png")


def decay(t, A, b):
    return A*np.exp(-t/b)

popt, pcov = cf(decay, np.array(concentrations), np.array(T1_values), p0 = [max(T1_values), 7E-3])

plt.figure()
plt.xlabel("Concentration (M)")
plt.ylabel("$T_1$ (ms)")
plt.title("$T_1$ Values Versus Concentration, $CuSO_4$")
plt.errorbar(concentrations, T1_values, yerr = np.array(T1_uncertainties), capsize=3, elinewidth=1, fmt = 'o', fillstyle = 'none')
plt.plot(concentrations, decay(np.array(concentrations),*popt), 'r--')
plt.savefig("../Plots/"+"T1_concentrations_cuso4.png")
