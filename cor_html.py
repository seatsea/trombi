# !/usr/bin/python3
#-*- coding: utf-8 -*-
import os

"""
Cette fonction doit prendre en un fichier html et corriger ces erreurs
"""

def correction(file_o):
	file_split = file_o.split(".")
	file_split[-2] += "_correct"
	file_c = ".".join(file_split)
	print(file_c)
	pass
	os.system("cp %s %s"%(file_o, file_c))
	f_c = open(file_c,"w")  # ouvrir le fichier
	chaine = f_c.read()                   # le charger dans une chaine de caractères
	f_c.close()                           # fermer le fichier
	result0=chaine.replace("</header>", "</header></body>") # remplacer les données que tu souhaites
	result1=chaine.replace("cellpading", "cellpadding") # remplacer les données que tu souhaites
	result2=chaine.replace("nowrap=\"true\" align=\"left\"", "align=\"left\" nowrap") # remplacer les données que tu souhaites       
	result3=chaine.replace("<td valign=\"center\"", "<td valign=\"middle\"") # remplacer les données que tu souhaites
	f_c.write(result)                     # écrire le résultat dans le fichier
	f_c.close()
	return(file_c)                           # fermer le fichier

correction('trombinos.unice.fr.html')
