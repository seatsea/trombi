#!/usr/bin/python3
import csv											# Importation du module csv
def parse_csv(file):								# Définition de la fonction
	ouverture=open('rt2.csv','r')					# Ouverture du fichier csv en mode "read"
	lignes=csv.reader(ouverture,delimiter=';')		# Lecture du fichier csv avec un délimiteur ';'	
	liste_e=[]	
	print(lignes)									# Définition de la liste que l'on va remplir avec le for qui suit
	for i in lignes :								# Définition de la boocle 
		print(i)
		liste_e+=lignes
		print (liste_e)									
	
