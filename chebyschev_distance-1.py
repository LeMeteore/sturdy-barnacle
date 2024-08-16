def chebyshev_distance_v1(p1, p2):
    """Calculate Chebyshev distance using a for loop."""
    max_dist = 0
    for x, y in zip(p1, p2):
        dist = abs(x - y)
        if dist > max_dist:
            max_dist = dist
    return max_dist

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance_v1(point1, point2)
    print("Chebyshev Distance (Version 1):", distance)
