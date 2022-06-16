from array import array
import Parsing
import CICFilter
import numpy as np
import matplotlib.pyplot as plt


def show_orig(lines):
    plt.subplot(1, 2, 1)
    plt.ylabel('mV')
    plt.xlabel('Номер снятия отсчета')
    plt.plot(lines)
    plt.grid(True)

def show_decimation(lines):
    cic = CICFilter.CicFilter(lines)
    lines = cic.decimator(25, 10)
    print(lines)
    plt.subplot(1, 2, 2)
    plt.ylabel('mV')
    plt.xlabel('Номер снятия отсчета')
    plt.plot(lines)
    plt.grid(True)

def start(address):
    lines = Parsing.parse(address)
    show_orig(lines)
    show_decimation(lines)
    plt.show()

if __name__ == "__main__":
    start(input("File name: "))

