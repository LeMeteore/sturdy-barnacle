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
