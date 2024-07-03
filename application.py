def chebyshev_distance(p1, p2):
    """Deuxième autre version de chebyshev_distance"""
    max_distance = 0
    for x, y in zip(p1, p2):
        max_distance = max(max_distance, abs(x-y))
        return max_distance

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
