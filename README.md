# congruences.py
Dessine les congruences des tables de multiplications modulo x. 
Il suffit de disposer de la librairie turtle, généralement pré-installée avec Python3.

Ce script comprend une unique fonction, dessine_congruences(p1,p2,p3,p4), qui:
 - trace avec Trutle un polygone régulier dont les sommets sont constitués des entiers naturels compris dans
   le nombre "modulo" (par exemple, modulo 10 paramètre un polygone régulier dont les sommets sont [0, 1, 2,
   3, 4, 5, 6, 7, 8, 9, 0]
 - trace dans ce polygone l'ensemble des liens qui unissent un sommet (multiplicateur) à son modulo (par exemple,
   dans la table de 12 modulo 10, le sommet "2", représentant la multiplication de 12 par 2 (c'est à dire 24),
   est lié au sommet 4, car (12*2) % 10 = 4.
  
Le script peut être lancé depuis n'importe quel environnement disposant de Python (attention aux limitations
de Jupyter Notebook).
Par défaut, il lance un exemple du schéma. 
La fonction peut être lancée avec le paramétrage suivant:
P1 (x0) = abcisse à l'origine, pour placer le schéma à droite, au centre ou à gauche du cadre (valeurs recommandées de -200 à 200)
P2 (y0) = ordonnée à l'origine, pour placer le schéma à la bonne hauteur.
P3 (n)  = le nombre dont on veut représenter la table de multiplications.
P4 (modulo) = ...le modulo de cette table.

# Les congruences.html
Il s'agit d'un petit cours avec les explications du modulo et des lignes du code, accompagnées de mises en application, à partir
d'un notebook.

# Pour aller plus loin:
https://www.mathemathieu.fr/art/articles-maths/38-beaute-multiplications (un cours complet et très pédago!)
https://www.geogebra.org/m/KdsHadMU  (une petite application en ligne pour reproduire rapidement des schémas de congruence).
https://www.youtube.com/watch?v=-X49VQgi86E (...l'excellente vidéo micmaths).
