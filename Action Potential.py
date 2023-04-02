import numpy as np
import matplotlib as plt1
import matplotlib.pyplot as plt
# importing package

# first of all we should import libraries which we need in this program


t = np.arange(0, 0.025, 0.0001)


t_n = 0.003
t_m = 0.0002
t_h = 0.005

n = 1 - np.exp(-t / t_n)
m = 1 - np.exp(-t / t_m)
h = np.exp(-t / t_h)

# making these values and using pre.values to make them.
N = np.power(n, 4)
M = np.power(m, 3) * h


# first plot here
plt.subplot(3, 1, 1)
plt.plot(t, N)
plt.title("Potassium")



# 2nd plot here
plt.subplot(3, 1, 2)
plt.plot(t, M)
plt.title("Sodium")

# 3rd plot here
# plot lines
plt.subplot(3, 1, 3)
plt.plot(t, n, label = "line 1")
plt.plot(t, m, label = "line 2")
plt.plot(t, h, label = "line 3")
plt.legend()
plt.show()
