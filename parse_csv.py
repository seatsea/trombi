#!/usr/bin/python3
import csv  # Importation du module csv


def parse_csv(file):  # Définition de la fonction
    ouverture = open(file, 'r', encoding='utf-8')  # Ouverture du fichier csv en mode "read"
    lignes = csv.reader(ouverture, delimiter=';')  # Lecture du fichier csv avec un délimiteur ';'
    liste_e = []  # Définition de la liste que l'on va remplir avec le for qui suit
    liste_e += lignes

    for i in range(0,len(liste_e)):
        liste_e[i] = liste_e[i][0:3]

    return liste_e
