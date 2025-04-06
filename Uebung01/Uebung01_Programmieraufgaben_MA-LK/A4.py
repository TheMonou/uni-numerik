import numpy as np
import time

def time_it(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Elapsed time: {end - start:.6f} seconds")
    return result

def trapetzregel_vektor(f,a,b,n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1) #  einen Vektor mit sämtlichen Stützstellen a + ih erzeugen
    y = f(x) # den Integranden f auf diesen Vektor anwenden
    summe = np.sum(y[1:-1]) # den Vektor der Ergebnisse mit der Funktion sum geeignet aufsummieren.
    return h * (0.5 * y[0] + summe + 0.5 * y[-1]) # 1/2 in die Klammer gezogen

def trapetzregel_normal(f,a,b,n):
    h = (b-a)/n
    summe = sum(f(a+i*h) for i in range(1,n))
    return h/2 * ( f(a) + 2*summe + f(b))

time_it(trapetzregel_vektor,lambda x: np.log(x),1,10,500000)
time_it(trapetzregel_normal,lambda x: np.log(x),1,10,500000)
