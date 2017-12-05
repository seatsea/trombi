#!/usr/bin/python3
"""
Cette fonction doit prendre en un fichier html correcte en entrée
Utilise html parse
Crée une liste de liste avec nom;prenom;lien image

"""

from bs4 import BeautifulSoup


def parse_html(file_h):													# Définition de la fonction
    opening = open(file_h, "r")											# Ouverture du fichier en mode read
    soup = BeautifulSoup(opening, "html.parser")							# Utilisation du parser html via Beautifulsoup
    a = soup.find_all("td", valign="top", width="16%", align="center")
    liste_user = []
    for user in a:
        nom = (user.get_text()).replace('\r', '').replace('\n', '')
        image = user.find("img").get('src')
        liste_user.append([nom,image])

    return liste_user
