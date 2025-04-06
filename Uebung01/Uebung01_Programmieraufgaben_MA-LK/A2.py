from math import factorial, exp
import matplotlib.pyplot as plt
from tabulate import tabulate

# Optimierung: Itertativ berechnen
def exp_forwards(x: float,n: int) -> float:
    result  = 1.
    term = 1.  # Initialwert für x^0 / 0! = 1
    for k in range(1,n+1):
        term *= x / k  # Verwendet die vorherige Berechnung, um Rechenzeit zu sparen
        result += term
    return result

def exp_backwards(x: float,n: int)  -> float:
    return sum((x**(n-k) / factorial(n-k) for k in range(n+1) ))

# Plot Unterschied echt und alg
def plot_diff(x,nrange):
    n_values = range(1, nrange)
    approximations = [exp_forwards(x, n) for n in n_values]
    exact_value = exp(x)

    plt.title(f"Konvergenz der Exponentialreihe für x = {x}")
    plt.xlabel("n (Anzahl der Summanden)")
    plt.ylabel("e^x Approximation")
    plt.plot(n_values, [exp_forwards(x, n) for n in n_values], marker="o", label="Approximation")
    plt.axhline(y=exact_value,color="r", linestyle="--", label="Exakter Wert")
    plt.legend()
    plt.grid()
    plt.show()

# Optional: Ploten der Annäherung
# plot_diff(12,50)


# Vergleich der Algorithmen:
valuePairs = [(0, 1), (1, 10), (5, 100), (10, 500), (10, 10)]
headers = ["x", "n", "approx", "exp(x)", "Fehler %"]
values = [(x, n, exp_forwards(x,n), exp(x)) for x, n in valuePairs]
table = [(x, n, approx, exact,f"{abs((approx - exact) / exact) * 100}%") for x, n, approx, exact in values]
print(tabulate(table, headers=headers, tablefmt="grid"))
