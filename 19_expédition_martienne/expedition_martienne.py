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

for distance in DISTANCES_DES_LIAISONS:
    if distance[0][0] in checkpoints:
        points_neighbors[distance[0][0]][distance[0][1]] = distance[1]
    else:
        points_neighbors[distance[0][0]] = {distance[0][1]: distance[1]}
        checkpoints.add(distance[0][0])

    if distance[0][1] in checkpoints:
        points_neighbors[distance[0][1]][distance[0][0]] = distance[1]
    else:
        points_neighbors[distance[0][1]] = {distance[0][0]: distance[1]}
        checkpoints.add(distance[0][1])


# checkpoints contient un set des points
checkpoints = sorted(checkpoints)
# points_neighbors contient un dictionnaire des points et des voisins associés
# avec la distance entre le point courant chaque voisin.
points_neighbors = dict(sorted(points_neighbors.items()))


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
    unvisited_nodes = dict.fromkeys(checkpoints, 99999)
    print(f'Le chemin le plus court en partant de {start_point} vers {arrival_point} est :')
    # le point de départ est à une distance 0, c'est le point sur lequel on se trouve
    unvisited_nodes[start_point] = 0
    # on récupère le point correspondant à la distance min (càd le point de départ ici)
    current_node = min(unvisited_nodes, key=unvisited_nodes.get)
    path = [] # liste qui va garder en mémoire le chemin depuis le point de départ vers l'arrivée
    total_distance = 0 # distance totale calculée entre départ et arrivée
    # on continue la boucle tant que l'on n'a pas atteint le point d'arrivée
    while current_node != arrival_point:
        path.append(current_node) # on ajoute le point courant dans le chemin
        # dans la boucle suivante on compare la distance entre le point courant et tous ses voisins
        # on s'assure de suivre le chemin le plus court en ajoutant la distance
        # déjà parcourue à la distance au prochain voisin
        for neighbor in points_neighbors[current_node]:
            if unvisited_nodes.get(neighbor) is not None:
                unvisited_nodes[neighbor] = unvisited_nodes[current_node] + points_neighbors[current_node][neighbor]
            if neighbor == arrival_point:
                # si un voisin est le point d'arrivée,
                # il faut le choisir en priorité même si la distance n'est pas la plus faible
                current_node = arrival_point
                # la distance ayant été ajoutée au fur et à mesure la distance totale est la distance du neighbor
                # qui est également la distance du current node puisqu'on se trouve sur le point d'arrivée
                total_distance = unvisited_nodes[neighbor]
                path.append(current_node) # ajout du dernier point
                print(f'{Colors.RED} {path} pour une distance totale de {total_distance/1000} kms{Colors.END}\n')
                return (path, total_distance)
        # avant de mettre à jour le point courant il faut retirer le point que l'on a déjà visité
        unvisited_nodes.pop(current_node)
        # enfin on met à jour le point courant sur le point ayant la distance totale minimale
        current_node = min(unvisited_nodes, key=unvisited_nodes.get)


if __name__ == "__main__":
    path_dict = {}
    # on teste chaque point de départ
    for POINT_DEPART in POINTS_DEPART:
        path_dict[POINT_DEPART] = dijkstra(POINT_DEPART, POINTS_ARRIVEE)[1]
    # on récupère le chemin avec la distance minimale
    display = min(path_dict, key=path_dict.get)
    print(f'{Colors.GREEN}Le site d\'atterissage recommandé est le site {display}{Colors.END}')
