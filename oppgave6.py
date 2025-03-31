import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from animasjon import animasjon
from oppgave4 import eksplisitt_euler
from oppgave5 import implisitt_euler


# Funksjon for Crank-Nicolson
def crank_nicolson(N, M, k, h):
    r = k / (2 * h**2)
    x = np.linspace(0, 2 * np.pi, N + 1)
    u = np.sin(x)  # Initialbetingelser
    u_new = np.zeros(N + 1)
    
    # Lag A og B matriser
    A = np.diag((1 + r) * np.ones(N-1)) + np.diag(-r * np.ones(N-2), 1) + np.diag(-r * np.ones(N-2), -1)
    B = np.diag((1 - r) * np.ones(N-1)) + np.diag(r * np.ones(N-2), 1) + np.diag(r * np.ones(N-2), -1)
    
    # Tidsskriving
    for _ in range(M):
        u_new[1:N] = np.linalg.solve(A, B @ u[1:N])
        u[:] = u_new[:]  # Oppdater u til u_new
    
    return x, u

# Funksjon for animasjon av alle metodene i ett plot
def full_animasjon(N, M, k, h):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)

    line1, = ax.plot([], [], label="Eksplisitt Euler")
    line2, = ax.plot([], [], label="Implisitt Euler")
    line3, = ax.plot([], [], label="Crank-Nicolson")

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        line3.set_data([], [])
        return line1, line2, line3

    def update(frame):
        # Oppdatering for de tre metodene
        x, u_exp = eksplisitt_euler(N, frame, k, h)
        _, u_imp = implisitt_euler(N, frame, k, h)
        _, u_cn = crank_nicolson(N, frame, k, h)
        
        # Sett dataene for plottene
        line1.set_data(x, u_exp)
        line2.set_data(x, u_imp)
        line3.set_data(x, u_cn)
        return line1, line2, line3

    # Lag animasjon
    ani = animation.FuncAnimation(fig, update, frames=range(1, M+1), init_func=init, blit=True, interval=100)
    plt.legend()
    plt.show()

# Parametere
N = 50  # Antall punkter i x
M = 200  # Antall tidsskritt
h = 0.001
k = 0.005

full_animasjon(N, M, k, h)