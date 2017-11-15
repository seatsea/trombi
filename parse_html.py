"""
Cette fonction doit prendre en un fichier html correcte en entré
Utilise html parse
Crée un csv avec nom;prenom;lien image
"""


def parse_html(src):
    file = open(src)  # Ouvre le fichier
