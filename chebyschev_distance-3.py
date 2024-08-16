import numpy as np

def chebyshev_distance_v3(p1, p2):
    """Calculate Chebyshev distance using NumPy."""
    return np.max(np.abs(np.array(p1) - np.array(p2)))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance_v3(point1, point2)
    print("Chebyshev Distance (Version 3):", distance)
