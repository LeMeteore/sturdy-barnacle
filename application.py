def chebyshev_distance(p1, p2):
    """Docstring..."""
    return max(abs(x - y) for x, y in zip(p1, p2))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)

def chebyshev_distance_v2(point1, point2):
    dimensions = len(point1)
    max_dist = 0
    for i in range(dimensions):
        max_dist = max(max_dist, abs(point1[i] - point2[i]))
    return max_dist

import numpy as np

def chebyshev_distance_v3(point1, point2):
    return np.max(np.abs(point1 - point2))