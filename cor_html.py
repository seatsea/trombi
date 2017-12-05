# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os


def correction(file_o):
    file_split = file_o.split(".")  # Modification du nom du fichier pour que le fichier corrigé soit de la forme *_correct.html
    file_split[-2] += "_correct"
    file_c = ".".join(file_split)
    f_init = open(file_o, "r")  # ouvrir le fichier original en lecture
    contenu = ''
    for i in f_init:
        line = i
        line = line.replace("</header>", "</header></body>")  # remplacement des erreurs dans le fichier html
        line = line.replace("cellpading", "cellpadding")  # remplacement des erreurs dans le fichier html
        line = line.replace("nowrap=\"true\" align=\"left\"",
                            "align=\"left\" nowrap")  # remplacement des erreurs dans le fichier html
        line = line.replace("<td valign=\"center\"",
                            "<td valign=\"middle\"")  # remplacement des erreurs dans le fichier html
        contenu = contenu + line

    f_c = open(file_c,'w')  # ouverture du fichier corrigé en écriture pour inscrire l'ensemble du contenu du fichier original
    f_c.write(contenu)  # Remplacement des éléments corrigés
    f_c.close()  # fermer le fichier


correction("trombinos.unice.fr.html")  # appel de la fonction pour le fichier trombinos.unice.fr.html
