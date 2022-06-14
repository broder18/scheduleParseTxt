import numpy as np

def parse(address):
    f = open(address, 'r')
    fstream = f.read()
    lines = fstream.split('\n')
    lines = np.array(lines)
    lines = lines.astype(int)
    f.close()
    return lines
