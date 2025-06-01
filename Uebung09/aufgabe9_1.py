import numpy as np


def f(x):
    a = 9.8606
    c = -1.1085*10**(25)
    d = 0.029
    return (a / (1 - c * np.exp(-d*x))) - 9

def diff_f(x):
    a = 9.8606
    c = -1.1085 * 10 ** (25)
    d = 0.029
    return -a * c * d * np.exp(-d * x) / (1 - c * np.exp(-d * x)) ** 2

def newton(f, diff_f, x0, epsilon):
    x_prev = x0
    x_curr = x0 - (f(x0) / diff_f(x0))
    i = 1
    while not np.isclose(x_curr, x_prev, atol=np.finfo(float).eps):
        x_prev = x_curr
        x_curr = x_prev- (f(x_prev) / diff_f(x_prev))
        i += 1
    return x_curr, i

def sekanten(f, x_1, x_2):
    x_prev_prev = x_2
    x_prev = x_1
    x_curr = x_prev - ((x_prev - x_prev_prev) / (f(x_prev) - f(x_prev_prev))) * f(x_prev)
    i = 1
    while not np.isclose(x_curr, x_prev, atol=np.finfo(float).eps):
        x_prev_prev = x_prev
        x_prev = x_curr
        x_curr = x_prev - ((x_prev - x_prev_prev) / (f(x_prev) - f(x_prev_prev))) * f(x_prev)
        i += 1
    return x_curr, i


def main():
    epsilon = np.finfo(float).eps
    print("Newton-Verfahren")
    x0_newton = 1961
    print(f"x0: {x0_newton}")
    newton_result, iterationen = newton(f, diff_f, x0_newton, epsilon)
    print(f"9-Milliarden-Grenze: {newton_result}, gefunden in {iterationen} Iterationen")
    print("\n")
    print("Sekanten-Verfahren")
    x_1 = 2000
    x_2 = 1961
    sekanten_result, iterationen = sekanten(f, x_1, x_2)
    print(f"9-Milliarden-Grenze: {sekanten_result}, gefunden in {iterationen} Iterationen")


if __name__ == '__main__':
    main()