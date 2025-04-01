import numpy as np

def f_derr(x):
    return np.exp(x)

def f_approx(h, x=1.5):
    return (f_derr(x+h)-f_derr(x-h)) / (2*h)

n = 0
h = 0.1
ny_feil = 9
feil = 10
while(feil > ny_feil):
    feil = ny_feil
    n += 1
    print("h = ", round(h, 10))
    if n != 0:
        print(f"Feilen er", round(ny_feil, 8))
    print(f"{n} iter. f'(x): {round(f_derr(1.5), 4)}. Approximert: {round(f_approx(h), 4)}")
    
    ny_feil = abs(f_approx(h) - f_derr(1.5))
    h /= 10

print(n)

