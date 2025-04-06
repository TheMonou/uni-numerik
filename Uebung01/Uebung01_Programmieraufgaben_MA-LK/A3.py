import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from tabulate import tabulate

calc_h = lambda a,b,n: (b-a)/n

def linksseitig(f,a,b,n):
    h = calc_h(a,b,n)
    return h * sum(f(a+i*h) for i in range(n))

def rechtsseitig(f,a,b,n):
    h = calc_h(a,b,n)
    return h * sum(f(a+i*h) for i in range(1,n+1))

def trapetzregel(f,a,b,n):
    h = calc_h(a,b,n)
    summe = sum(f(a+i*h) for i in range(1,n))
    return h/2 * ( f(a) + 2*summe + f(b))

def plot_diff(f,a,b,f_string,range,exact_value):
    plt.title(f"Integral ∫[{a}, {b}] {f_string}")
    plt.xlabel("n (Anzahl der Unterteilungen)")
    plt.ylabel(f"Approximation Integralwert")
    plt.axhline(y=exact_value,color="r", label="Exakter Wert")
    plt.plot(range, [linksseitig(f, a, b, n) for n in range], label="linksseitig")
    plt.plot(range, [rechtsseitig(f, a, b, n) for n in range], label="rechtsseitig")
    plt.plot(range, [trapetzregel(f, a, b, n) for n in range], label="trapezregel")
    plt.legend()
    plt.grid()
    plt.show()

def plot_diff_help(f_dict: dict, n_values: range,exact_value):
    """
    Helper function to call plot_diff with a function dictionary.
    """
    print(f"Starting plotting of ∫[{f_dict['a']}, {f_dict['b']}] {f_dict['description']}...")
    plot_diff(f_dict["func"], f_dict["a"], f_dict["b"], f_dict["description"], n_values,exact_value)
    print("Plotting finished!")

def print_diff(f_dict,n_range,exact_value):
    print(f"Approximated Integral and Difference(Δ) from {exact_value} = ∫[{f_dict['a']}, {f_dict['b']}] {f_dict['description']}:")
    a = f_dict ["a"]
    b = f_dict["b"]
    f = f_dict["func"]
    headers = ["n"] + [f"{n}" for n in n_range]
    table = [
        ["linksseitig"] + [f"{wert} \nΔ={abs(exact_value-wert)}" for n in n_range if (wert := linksseitig(f, a, b, n))],  # Gleiche Fix für die Datenzeilen
        ["rechtsseitig"] + [f"{wert} \nΔ={abs(exact_value-wert)}" for n in n_range if (wert := rechtsseitig(f, a, b, n))],
        ["trapetzregel"] + [f"{wert} \nΔ={abs(exact_value-wert)}" for n in n_range if (wert := trapetzregel(f, a, b, n))],
    ]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def calc_actual(f_dict):
    return sp.integrate.quad(f_dict["func"], f_dict["a"], f_dict["b"])[0]

# Unterschiede Darstellen:

n_values = [2,10,50,100,1000,100_000,500_000,1_000_000]

f1 = {
    "func": lambda x: 1 / (x ** 2),
    "description": "1/x² dx",
    "a": 1/10,
    "b": 10
}
#plot_diff_help(f1,range(100,10000,10),99/10) # Optional
print_diff(f1,n_values,calc_actual(f1))

f2 = {
    "func": lambda x: np.log(x),
    "description": "ln(x)",
    "a": 1,
    "b": 2,
}
#plot_diff_help(f2,range(1,200,1),(2*np.log(2)-1)) # Optional
print_diff(f2,n_values,calc_actual(f2))


