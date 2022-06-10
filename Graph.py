import Parsing
import numpy as np
import matplotlib.pyplot as plt

def show(address):
    lines = Parsing.parse(address)
    t = np.arange(0, 597, 1)
    plt.ylabel('mV')
    plt.xlabel('Номер снятия отсчета')
    plt.plot(t, lines)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    show(input("File name: "))

