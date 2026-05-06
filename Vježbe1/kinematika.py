import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, t_start=0, t_end=10, dt=0.01):
    
    a = F / m
    
    t = np.arange(t_start, t_end + dt, dt)
    N = len(t)
    
    x = np.zeros(N)
    v = np.zeros(N)
    a_array = np.full(N, a)
    
    for i in range(1, N):
        v[i] = v[i-1] + a * dt
        x[i] = x[i-1] + v[i-1] * dt
        
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    
    #x-t graf
    axs[0].plot(t, x, color='blue', linewidth=2)
    axs[0].set_ylabel('x [m]')
    axs[0].set_title('Položaj - Vrijeme (x-t)')
    axs[0].grid(True)
    
    #v-t graf
    axs[1].plot(t, v, color='red', linewidth=2)
    axs[1].set_ylabel('v [m/s]')
    axs[1].set_title('Brzina - Vrijeme (v-t)')
    axs[1].grid(True)
    
    #a-t graf
    axs[2].plot(t, a_array, color='green', linewidth=2)
    axs[2].set_xlabel('t [s]')
    axs[2].set_ylabel('a [m/s²]')
    axs[2].set_title('Ubrzanje - Vrijeme (a-t)')
    axs[2].grid(True)
    
    plt.subplots_adjust(hspace=0.5)
    plt.show()
    

