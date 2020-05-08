import numpy as np
import matplotlib.pyplot as plt

x = list(range(20, 100))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(list(range(0, min(x)))+x, (min(x)*[0])+[21.8 for i in x], label=r"Undisclosed", color="black", linestyle="-")
plt.plot(list(range(0, min(x)))+x, (min(x)*[0])+[20 + (i*0.1) for i in x], label=r"Publicly Disclosed", color="black", linestyle="--")

plt.xlabel(r'Actual Stake', fontsize=32, labelpad=40)
plt.ylabel(r'Interest Rate', fontsize=32, labelpad=30)
plt.ylim((-5, 50))

plt.tick_params(axis='both', 
    which='both', 
    bottom='off', 
    top='off', 
    labelbottom='off', 
    right='off', 
    left='off', 
    labelleft='off')

plt.legend(loc=2, prop={'size': 32})
# plt.savefig('tex_demo')
plt.show()