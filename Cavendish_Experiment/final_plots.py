import matplotlib.pyplot as plt
import numpy as np

G_vals = [1.72E-10, 1.54E-10, 1.29E-10, 1.73E-10]
G_errs = [0.50E-10, 0.13E-10, 0.11E-10, 1.44E-10]
trial_name = ["Driven Osc 1", "Driven Osc 2", "Driven Osc 3", "Static Method"]
trial_number = [1,2,3,4]

# thetad_vals = [1.289, 1.153, 0.961, 1.292]
# thetad_errs = [0.004, 0.004, 0.003, 1.032]

# thetad_vals = [1.289, 1.153, 0.961]
# thetad_errs = [0.04, 0.04, 0.03]
#
# for i in range(len(trial_number)):
#     # plt.plot(trial_number[i], G_vals[i])
#     plt.errorbar(trial_number[i], G_vals[i]/2.3423, xerr = 0, yerr = G_errs[i], fmt = 'o', label = "{}".format(trial_name[i]))
# plt.title("Calculated Values of G")
# plt.xlabel("Trial")
# plt.ylabel("G (m^3 kg^(-1) s^(-2))")
# plt.axhline(y = 6.67E-11, xmin = 0, xmax = 4, label = "Expected Value of G", c = 'm', ls = '--')
# plt.xticks(trial_number)
# plt.legend(loc='upper left')
# plt.tight_layout()
# plt.savefig("final_plots_of_G_scaled.png")
#
# print(np.array(G_vals)/2.3423)
print(np.average(G_vals), np.average(G_errs))




# for i in range(len(trial_number)-1):
#     plt.errorbar(trial_number[i], thetad_vals[i], xerr = 0, yerr = thetad_errs[i], fmt = 'o', label = "{}".format(trial_name[i]))
# plt.title("Values of Displacement Angle from Equilibirum, Theta D")
# plt.xlabel("Trial")
# plt.ylabel("Angle (mrad)")
# plt.xticks(trial_number)
# plt.legend(loc='upper left')
# plt.tight_layout()
# plt.savefig("theta_d_plots_driven_only.png")
