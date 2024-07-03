import torch

def chebyshev_distance(p1, p2):
    """Calcule la distance de Chebyshev entre deux points p1 et p2 en utilisant PyTorch."""
    # Convertissons  les points en tensors PyTorch
    p1 = torch.tensor(p1, dtype=torch.float32)
    p2 = torch.tensor(p2, dtype=torch.float32)
    # Calculer les différences absolues
    differences = torch.abs(p1 - p2)
    # Retourner la distance maximale trouvée (distance de Chebyshev)
    return torch.max(differences).item()

if __name__ == "__main__":

    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    # Affichage de la distance de Chebyshev
    print("Distance de Chebyshev:", distance)
