"""
Cette fonction doit prendre en un fichier html correcte en entrée
Utilise html parse
Crée une liste de liste avec nom;prenom;lien image

"""
#!/usr/bin/python3
import os
	

from bs4 import BeautifulSoup  

def parse_html(file_h): 
	opening = open(file_h, "r")
	soup = BeautifulSoup(opening, "html.parser")
	a = soup.find_all("td", valign="top", width="16%", align="center")
	liste = []
	personne = []
	
	for td in a:
		print(td)
		
		
		liste += personne
		

parse_html('M3206.html')
