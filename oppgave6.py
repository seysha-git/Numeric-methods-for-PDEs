import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

h = 0.25
k = 0.01
x = np.arange(0, 1+h, h)
t = np.arange(0, 1+k, k)
n, m = len(x), len(t)
u = np.zeros((n, m))
u[:, 0] = np.sin(x)
r = k / h**2

A = np.diag(2 * np.ones(n)) + np.diag(-1 * np.ones(n - 1), 1) + np.diag(-1 * np.ones(n - 1), -1)
I = np.eye(n)

M1 = 2*I + r * A
M2 = 2*I - r * A

for j in range(m - 1):
    u[1:-1, j+1] = np.linalg.solve(M1[1:-1, 1:-1], M2[1:-1, 1:-1] @ u[1:-1, j])

fig, ax = plt.subplots()
line, = ax.plot(x, u[:, 0])
def update(frame):
    line.set_ydata(u[:, frame])
    return line,
ani = animation.FuncAnimation(fig, update, frames=m, interval=100)
plt.show()
