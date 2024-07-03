def chebyshev_distance(p1, p2):
    """Calcule la distance de Chebyshev entre deux points p1 et p2."""
    # Initialisation de la distance maximale
    max_distance = 0
   
    for x, y in zip(p1, p2):
        # Calcul de valeur absolue entre x et  y 
        distance = abs(x - y)
        # calcul de la distance maximal 
        if distance > max_distance:
            max_distance = distance
   
    return max_distance

if __name__ == "__main__":
    
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Distance de Chebyshev:", distance)
