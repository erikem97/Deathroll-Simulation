import matplotlib.pyplot as plt
import numpy as np

#Analytical solution of deathroll


Win_Rate = []
for n in range(2,10000):
    P = 0
    for i in Win_Rate:
        P -= i
    P = (1/(n+1))*(n+P)
    Win_Rate.append(P)


EV = []
for n in range(2, 10000):
    gold = n*0.1
    EV.append((2*gold*Win_Rate[n-2]-gold))

x = np.arange(3,10001)

fig, axs = plt.subplots(1, 2)
axs[0].plot(x, EV)
axs[1].plot(x, Win_Rate)
plt.show()

