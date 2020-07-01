import subprocess
import pickle
import matplotlib.pyplot as plt
import math

#for i in range(2,67):
# subprocess.call(["python", "Deathroll.py", str(i)])


EV = []
roll_number = []
number_simulation = []
r2_win = []
winrate = []
std_mean_EV = []


for i in range(2,101):
    file_name = "checkpoint_Deathroll"+str(i)+".pkl"
    with open(file_name, "rb") as cp_file:
        cp = pickle.load(cp_file)
    roll_number.append(cp["roll_number"])
    EV.append(cp["EV"])
    r2_win.append(cp["r2_win"])
    number_simulation.append(cp["number_simulation"])
    std_mean_EV.append(cp["std_mean"])
    winrate.append(r2_win[-1]/number_simulation[-1])


Win_Rate_Analytics = []
for n in range(2,101):
    P = 0
    for i in Win_Rate_Analytics:
        P -= i
    P = (1/(n+1))*(n+P)
    Win_Rate_Analytics.append(P)


EV_Analytics = []
for n in range(2, 101):
    gold = n*0.1
    EV_Analytics.append((2*gold*Win_Rate_Analytics[n-2]-gold))

Percent_Error_EV = []
Percent_Error_Win_Rate = []
for i in range(len(EV_Analytics)):
    Percent_Error_EV.append(abs((EV[i]-EV_Analytics[i])/(EV_Analytics[i]))*100)
    Percent_Error_Win_Rate.append(abs((winrate[i] - Win_Rate_Analytics[i]) / (Win_Rate_Analytics[i])) * 100)

std_mean_winrate = []
for i in range(len(winrate)):
    std_mean_winrate.append(math.sqrt(winrate[i] - (winrate[i] ** 2)) / math.sqrt(number_simulation[i]))




fig = plt.figure()
fig.suptitle('Deathroll simulation and analytical solution, 2nd player', fontsize=16)
#  plots for heat transfer
ax = plt.subplot(321)
ax.plot(roll_number, EV, '-g', label='Simulated data')
ax.set(ylabel='EV net profit, Simulated [Gold]', xlabel='Starting roll')
#ax.errorbar(roll_number, EV, yerr = std_mean_EV, fmt = ' ', ecolor='black', elinewidth=2, capsize=2, barsabove=True, label='95% CI')
ax.grid()
ax.legend()


ax2 = plt.subplot(322)
ax2.plot(roll_number, winrate,'-g', label='Simulated data')
ax2.set(ylabel='Winrate simulated', xlabel='Starting roll')
#ax2.errorbar(roll_number, winrate, yerr=std_mean_winrate, fmt=' ', ecolor='black', elinewidth=2, capsize=2, barsabove=True, label='95% CI')
ax2.grid()
ax2.legend()


ax3 = plt.subplot(323)
ax3.plot(roll_number, EV_Analytics, '-b')
ax3.set(ylabel='EV net profit, Analytical [Gold]', xlabel='Starting roll')
ax3.grid()

ax4 = plt.subplot(324)
ax4.plot(roll_number, Win_Rate_Analytics, '-b')
ax4.set(ylabel='Winrate Analytical', xlabel='Starting roll')
ax4.grid()

ax5 = plt.subplot(325)
ax5.plot(roll_number, Percent_Error_EV, '-r')
ax5.set(ylabel='Relative error EV [%]', xlabel='Starting roll')
ax5.grid()

ax6 = plt.subplot(326)
ax6.plot(roll_number, Percent_Error_Win_Rate, '-r')
ax6.set(ylabel='Relative error Winrate [%]', xlabel='Starting roll')
ax6.grid()

plt.show()

