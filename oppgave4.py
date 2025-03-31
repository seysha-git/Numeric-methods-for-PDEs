import numpy as np
import matplotlib.pyplot as plt
import animasjon
# Funksjon for eksplisitt Euler
def eksplisitt_euler(N, M, k, h):
    r = k / h**2
    x = np.linspace(0, 2 * np.pi, N + 1)
    u = np.sin(x)  # Initialbetingelse
    u_new = np.zeros(N + 1)
    
    # Løsning i tid
    for _ in range(M):
        for i in range(1, N):
            u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1])
        u[:] = u_new[:]
    
    return x, u


# Parametere
N = 50  # Antall punkter i x
M = 200  # Antall tidsskritt
h = 0.5  # Romsteg
k = h**2/2  # Tidssteg


animasjon.animasjon(eksplisitt_euler,"Eksplisitt euler", N, M, k, h)