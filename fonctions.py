import numpy as np

def chebyshev_distance_v1(x, y):
    return max(abs(a - b) for a, b in zip(x, y))
def chebyshev_distance_v2(x, y):
    return np.max(np.abs(np.array(x) - np.array(y)))