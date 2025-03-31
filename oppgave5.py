import numpy as np
import matplotlib.pyplot as plt
import animasjon
def implisitt_euler(N, M, k, h):
    r = k / h**2
    x = np.linspace(0, 2 * np.pi, N + 1)
    u = np.sin(x)
    u_new = np.zeros(N + 1)
    
    A = np.diag((1 + 2 * r) * np.ones(N-1)) + np.diag(-r * np.ones(N-2), 1) + np.diag(-r * np.ones(N-2), -1)
    
    for j in range(M):
        u_new[1:N] = np.linalg.solve(A, u[1:N])
        u[:] = u_new[:]
    
    return x, u

# Parametere
N = 50  # Antall punkter i x
M = 200  # Antall tidsskritt
h = 0.5  # Romsteg
k = h**2/2  # Tidssteg


#animasjon.animasjon(implisitt_euler,"Implisitt euler", N, M, k, h)