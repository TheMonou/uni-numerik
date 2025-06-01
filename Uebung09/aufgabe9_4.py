import numpy as np

def eval_jacobi(D, x):
    return np.array([[D[i, j](x[0], x[1]) for j in range(D.shape[1])] for i in range(D.shape[0])])


def f(x, y):
    return np.array([np.sin(x) - y, np.exp(-y) - x])

def f11(x, y):
    return np.cos(x)

def f12(x, y):
    return -1

def f21(x, y):
    return -1

def f22(x, y):
    return np.exp(-y)


def newton(f, D, x0, epsilon):
    x_prev = x0
    x_curr = x_prev - np.linalg.inv(eval_jacobi(D, x_prev)) @ f(x_prev[0], x_prev[1])
    i = 1
    while not np.isclose(np.linalg.norm(x_curr), np.linalg.norm(x_prev), atol=np.finfo(float).eps):
        x_prev = x_curr
        x_curr = x_prev - np.linalg.inv(eval_jacobi(D, x_prev)) @ f(x_prev[0], x_prev[1])
        i += 1
    return x_curr, i


def main():
    print("Nullstellen \n")
    D = np.array([[f11, f12], [f21, f22]])
    x0 = np.array([1, 1])
    epsilon = np.finfo(float).eps
    x, iterationen = newton(f, D, x0, epsilon)
    print(f" Newton-Verfahren: \n {x} \n in {iterationen} Iterationen \n")

if __name__ == '__main__':
    main()