import numpy as np

def original_alg(p, q):
    """
        ursprünglicher Algorithmus
    """
    return p*-1+np.sqrt(np.square(p) + q)

def alternative_alg(p, q):
    """
        alternativer Algorithmus
    """
    x1 = -p - np.sqrt(np.square(p) + q)
    return -q/x1

p = [1e2, 1e4, 1e6, 1e7, 1e8]
q = 1

def f(x,p,q):
    return x*x + 2*p*x -q

for value in p:
    x2 = original_alg(value, q)
    x2_ = alternative_alg(value, q)

    # Ausgabe der Werte in formatierter Form
    print(f"n={value:<15}"
          f"x2={x2:<25}"
          f"x2'={x2_:<25}"
          f"f(x2)={f(x2,value,q):<25}" 
          f"f(x2')={f(x2_,value,q):<25}")
print("\nLEGENDE:")
print(" x2 = uhrprünglicher Algorithmus")
print(" x2' = alternativer Algorithmus")
print(" f(x2)/f(x2') ist die der Funktionswert der 2. Nullstelle \n Da der zu erwartende Wert '0' ist somit auch die Abweichung vom echten Wert")

# Aus Ergebnissen folgt alternativer Algorithmus ist genauer für große p