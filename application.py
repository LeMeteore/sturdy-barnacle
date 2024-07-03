import numpy as np

def chebyshev_distance(p1, p2):
    """Docstring..."""
    return max(abs(x - y) for x, y in zip(p1, p2))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)

def chebyshev_distance2(point1, point2):
    max = 0
    for a, b in zip(point1, point2):
        distance = abs(a - b)
        if distance > max:
            max = distance
    return max

def chebyshev_distance3(point1, point2):
    """Docstring..."""
    return max([abs(point1[i] - point2[i]) for i in range(len(point1))])

def chebyshev_distance4(point1, point2):
    """Docstring..."""
    return np.max(np.abs(np.array(point1) - np.array(point2)))