"""
Cette fonction doit prendre en un fichier html et corriger ces erreurs
"""


def cor_html(src):
    file = open(src)  # Ouvre le fichier









# !/usr/bin/python3
#-*- coding: utf-8 -*-

f = file("trombicorrige.html","r")    # ouvrir le fichier
chaine = f.read()                   # le charger dans une chaine de caractères
f.close()                           # fermer le fichier
result=chaine.replace("</header>", "</header></body>") # remplacer les données que tu souhaites
f = file("trombicorrige.html","w")    # ouvrir le fichier de sortie
                       # en écriture  Tu peux ouvrir le même si tu veux l'écraser
f.write(result)                     # écrire le résultat dans le fichier
f.close()                           # fermer le fichier
