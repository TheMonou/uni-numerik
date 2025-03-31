import numpy as np
import matplotlib.pyplot as plt


def main():
    # Example usage of numpy
    array = np.array([1, 2, 3])
    print("Numpy array:", array)

    x = np.linspace(0, 2 * np.pi, 100)

    # Example usage of matplotlib
    plt.plot(x, np.sin(x))
    plt.title("Sine Function")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()