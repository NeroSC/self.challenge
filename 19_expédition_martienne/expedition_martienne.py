#!/usr/bin/env python

"""
Filename: expedition_martienne.py
Author: Nero
Description: Trouve le chemin le plus court entre deux points à partir d'un fichier de ressources
Usage: python expedition_martienne.py
"""

from enum import StrEnum
from typing import Tuple

from ressources_mars import POINTS_ARRIVEE, POINTS_DEPART, DISTANCES_DES_LIAISONS


class Colors(StrEnum):
    """Classe de coloration syntaxique
    """
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

#############################################
# Récupération de la liste des distances
#############################################


checkpoints = set()
points_neighbors = {}

for points, distance in DISTANCES_DES_LIAISONS:
    p1, p2 = points
    if p1 in points_neighbors:
        points_neighbors[p1][p2] = distance
    else:
        points_neighbors[p1] = {p2: distance}

    if p2 in points_neighbors:
        points_neighbors[p2][p1] = distance
    else:
        points_neighbors[p2] = {p1: distance}

# points_neighbors contient un dictionnaire des points et des voisins associés
# avec la distance entre le point courant chaque voisin.
points_neighbors = dict(points_neighbors.items())

print(points_neighbors)


def dijkstra(start_point: str, arrival_point: str = "Z") -> Tuple[list, float]:
    """Algorithme de Djikstra pour déterminer le chemin le plus court

    Args:
        start_point (str): Point de départ
        arrival_point (str, optional): Arrivée. Defaults to "Z".

    Raises:
        SystemExit: _description_

    Returns:
        Tuple[list,float]: Retourne le chemin parcouru ainsi que la distance totale
    """
    # Mise à l'infini des distances de chaques points
    unvisited_nodes = dict.fromkeys(points_neighbors, 99999)
    print(f'Le chemin le plus court en partant de {start_point} vers {arrival_point} est :')
    # le point de départ est à une distance 0, c'est le point sur lequel on se trouve
    unvisited_nodes[start_point] = 0
    # on récupère le point correspondant à la distance min (càd le point de départ ici)
    current_node = min(unvisited_nodes, key=unvisited_nodes.get)
    path = []
    # on continue la boucle tant que l'on n'a pas atteint le point d'arrivée
    while current_node != arrival_point:
        path.append(current_node)  # on ajoute le point courant dans le chemin
        # dans la boucle suivante on compare la distance entre le point courant et tous ses voisins
        # on s'assure de suivre le chemin le plus court en ajoutant la distance
        # déjà parcourue à la distance au prochain voisin
        for neighbor in points_neighbors[current_node]:
            if neighbor in unvisited_nodes:
                unvisited_nodes[neighbor] = unvisited_nodes[current_node] + points_neighbors[current_node][neighbor]
            if neighbor == arrival_point:
                current_node = arrival_point
                path.append(arrival_point)  # ajout du dernier point
                return (path, unvisited_nodes[neighbor])
        # avant de mettre à jour le point courant il faut retirer le point que l'on a déjà visité
        unvisited_nodes.pop(current_node)
        # enfin on met à jour le point courant sur le point ayant la distance totale minimale
        current_node = min(unvisited_nodes, key=unvisited_nodes.get)


if __name__ == "__main__":
    path_dict = {}
    # on teste chaque point de départ
    # on récupère le chemin avec la distance minimale
    for POINT_DEPART in POINTS_DEPART:
        path_temp, path_dict[POINT_DEPART] = dijkstra(POINT_DEPART, POINTS_ARRIVEE)
        print(f'{Colors.RED} {path_temp} pour une distance totale de {path_dict[POINT_DEPART]/1000} kms{Colors.END}\n')
    display = min(path_dict, key=path_dict.get)
    print(f'{Colors.GREEN}Le site d\'atterissage recommandé est le site {display}{Colors.END}')
