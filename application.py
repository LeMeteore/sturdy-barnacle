def chebyshev_distance(p1, p2):
    """Calcul de la distance de Chebyshev entre deux points p1 et p2."""
    return max(map(lambda x, y: abs(x - y), p1, p2))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
