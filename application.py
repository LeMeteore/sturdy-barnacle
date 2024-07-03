def chebyshev_distance(p1, p2):
    """Docstring..."""
    return max(abs(x - y) for x, y in zip(p1, p2))

def chebyshev_distance_for_loop(p1, p2):
    """Calcul de la distance de Chebyshev en utilisant une boucle for"""
    max_distance = 0
    for x, y in zip(p1, p2):
        distance = abs(x - y)
        if distance > max_distance:
            max_distance = distance
    return max_distance

def chebyshev_distance_list_comprehension(p1, p2):
    """Calcul de la distance de Chebyshev en utilisant une compréhension de liste"""
    return max([abs(x - y) for x, y in zip(p1, p2)])

def chebyshev_distance_map_lambda(p1, p2):
    """Calcul de la distance de Chebyshev en utilisant map et lambda"""
    return max(map(lambda x_y: abs(x_y[0] - x_y[1]), zip(p1, p2)))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    distance_1 = chebyshev_distance_for_loop(point1, point2)
    distance_2 = chebyshev_distance_list_comprehension(point1,point2)
    distance_3 = chebyshev_distance_map_lambda(point1,point2)
    print("Chebyshev Distance:", distance)
    print("Chebyshev Distance with for loop:", distance_1)
    print("Chebyshev Distance with list comprehension:", distance_2)
    print("Chebyshev Distance with map and lambda:", distance_3)

