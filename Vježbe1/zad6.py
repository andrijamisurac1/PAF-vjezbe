import numpy as np
import matplotlib.pyplot as plt

F = float(input("Unesite iznos sile u N: "))
m = float(input("Unesite masu čestice u kg: "))

a = F / m

t_start = 0
t_end = 10
dt = 0.01
t = np.arange(t_start, t_end + dt, dt)
broj_tocaka = len(t)

x = np.zeros(broj_tocaka)
v = np.zeros(broj_tocaka)
a_array = np.full(broj_tocaka, a)

x[0] = 0
v[0] = 0

for i in range(1, broj_tocaka):
    v[i] = v[i-1] + a * dt
    x[i] = x[i-1] + v[i-1] * dt

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

#x-t graf
axs[0].plot(t, x, color='blue')
axs[0].set_xlabel('t [s]')
axs[0].set_ylabel('x [m]')
axs[0].set_title('x - t graf')
axs[0].grid(True)

#v-t graf
axs[1].plot(t, v, color='red')
axs[1].set_xlabel('t [s]')
axs[1].set_ylabel('v [m/s]')
axs[1].set_title('v - t graf')
axs[1].grid(True)

#a-t graf
axs[2].plot(t, a_array, color='green')
axs[2].set_xlabel('t [s]')
axs[2].set_ylabel('a [m/s²]')
axs[2].set_title('a - t graf')
axs[2].grid(True)

#plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
plt.show()