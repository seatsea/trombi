# !/usr/bin/python3
#-*- coding: utf-8 -*-

import os

def correction(file_o):
	file_split = file_o.split(".")
	file_split[-2] += "_correct"
	file_c = ".".join(file_split)
	f_init = open(file_o,"r")  # ouvrir le fichier
	                                    
	contenu = ''
	for i in f_init :
		line = i
		line=line.replace("</header>", "</header></body>") # remplacer les données que tu souhaites
		line=line.replace("cellpading", "cellpadding") # remplacer les données que tu souhaites
		line=line.replace("nowrap=\"true\" align=\"left\"", "align=\"left\" nowrap") # remplacer les données que tu souhaites       
		line=line.replace("<td valign=\"center\"", "<td valign=\"middle\"") # remplacer les données que tu souhaites
		contenu = contenu+line

	
	f_c=open(file_c,'w')
	f_c.write(contenu)                    # écrire le résultat dans le fichier
	f_c.close()                      # fermer le fichier

correction("trombinos.unice.fr.html")
