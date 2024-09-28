#!/usr/bin/env python

"""
Filename: expedition_martienne.py
Author: Nero
Description
Usage:
"""

# Commande :

# 🔶 19. Expédition martienne !

# *Allô Houston, on a un challenge.*

# Sur la carte, vous avez en bleu les quatre sites d'atterrissage possibles,
# en vert l'endroit précis où se trouve l'artefact et en blanc les différents points de passage.

# Votre mission (si vous l'acceptez) est de déterminer quel site d'atterrissage
# il faut sélectionner pour atteindre l'artefact en parcourant le moins de distance possible.

# ## 🔹 Étapes

# - Récupérer la liste des distances entre chaque point fourni en ressources.
# - Déterminer le nombre de checkpoints et pour chacun d'eux, ses voisins directs avec leur distance.
# - Pour chaque point d'atterrissage, calculer le chemin le plus court vers le point `Z`
#       en indiquant la distance totale de km à parcourir.
# - Annoncer le meilleur site d'atterrissage.

# ## 🔹 Conditions
# - L'affichage se fait via la console.
# - Pour calculer le chemin le plus court, vous devez utiliser
#   [l'algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra).
# - Votre algorithme devra prendre en input n'importe quel point de départ et d'arrivé du parcours
#       pour déterminer le chemin le plus court (par exemple, le chemin le plus court entre `X` et `AC`).
# - N'oubliez pas de gérer les inputs utilisateurs.

# ## 🔹 Ressources

# - Le fichier contenant les distances de chaque liaison ainsi que la carte de Mars avec les différents checkpoints.
