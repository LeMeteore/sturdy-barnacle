def chebyshev_distance(p1, p2, dim=0):
    """Docstring..."""
    if dim == len(p1):
        return 0
    return max(abs(p1[dim] - p2[dim]), chebyshev_distance(p1, p2, dim + 1))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
