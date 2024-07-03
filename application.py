import numpy as np

def chebyshev_distance(p1, p2):
    """Calcule la distance de Chebyshev entre deux points p1 et p2."""
    # Convertissons en tabelau numpy
    p1 = np.array(p1)
    p2 = np.array(p2)
    # Calculer les différences absolues
    differences = np.abs(p1 - p2)
    #  calcul de la distance maximal 
    return np.max(differences)

if __name__ == "__main__":
    
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    
    distance = chebyshev_distance(point1, point2)
    # Affichage de la distance de Chebyshev
    print("Distance de Chebyshev:", distance)
