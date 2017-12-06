#!/usr/bin/python3

import csv  # Importation du module csv


def parse_csv(file):  # Définition de la fonction
    ouverture = open(file, 'r', encoding='utf-8')  # Ouverture du fichier csv en mode "read"
    lignes = csv.reader(ouverture, delimiter=';')  # Lecture du fichier csv avec un délimiteur ';'
    liste_e = []
    liste_e += lignes
    liste_user =[]

    for i in range(0, len(liste_e)):
        liste_user.append([liste_e[i][1] + ' ' + liste_e[i][0],liste_e[i][2]])

    return liste_user
print(parse_csv('rt2.csv'))