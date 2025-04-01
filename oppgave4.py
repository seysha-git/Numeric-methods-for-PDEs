import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

h = 0.5
k = 0.05
x = np.arange(0, 1+h, h)
t = np.arange(0, 1+k, k)
randkrav = [0, 0]
initialkrav = np.sin(x)
n = len(x)
m = len(t)
u = np.zeros((n, m))
u[0, :] = randkrav[0]
u[-1, :] = randkrav[-1]
u[:, 0] = initialkrav
r = k / h**2

for j in range(m - 1):
    for i in range(1, n - 1):
        u[i, j+1] = u[i, j] + r * (u[i+1, j] - 2 * u[i, j] + u[i-1, j])
 
fig, ax = plt.subplots()
line, = ax.plot(x, u[:, 0])
ani = animation.FuncAnimation(fig, lambda f: line.set_ydata(u[:, f]), frames=m, interval=500)
plt.show()


