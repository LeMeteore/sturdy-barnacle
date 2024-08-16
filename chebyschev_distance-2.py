def chebyshev_distance_v2(p1, p2):
    """Calculate Chebyshev distance using the max function."""
    return max(abs(x - y) for x, y in zip(p1, p2))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance_v2(point1, point2)
    print("Chebyshev Distance (Version 2):", distance)
