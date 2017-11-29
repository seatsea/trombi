#!/usr/bin/python3
import csv											# Importation du module csv
def parse_csv(file):								# Définition de la fonction
	ouverture=open(file,'r')					# Ouverture du fichier csv en mode "read"
	lignes=csv.reader(ouverture,delimiter=';')		# Lecture du fichier csv avec un délimiteur ';'	
	liste_e=[]										# Définition de la liste que l'on va remplir avec le for qui suit
	
	for i in lignes :								# Définition de la boocle 
		liste_e+=lignes
