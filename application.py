def chebyshev_distance(p1, p2):
    """Docstring..."""
    assert len(p1) == len(p2)
    distance = 0
    for i in range(len(point1)):
        distance = max(distance, abs(point1[i] - point2[i]))
    return distance

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
