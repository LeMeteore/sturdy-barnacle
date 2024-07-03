def chebyshev_distance(p1, p2):
    """Troisième autre version de chebyshev_distance"""
    max_distance = 0
    while i < len(p1):
        distance = abs(p1[i] - p2[i])
        if distance > max_distance:
            max_distance = distance
        i +=1
    return max_distance


if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
