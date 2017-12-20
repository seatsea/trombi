# !/usr/bin/python3
#-*- coding: utf-8 -*-

def gen_index(list_grp): # fonction servant à créé un fichier index.html qui va servir de référence pour trier les différents groupes
    file_init = open("index.html",'w') # ouverture et création du fichier index.html
    file_init.write('<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"></head><body>'+'\n') # début de syntaxe html
    for i in list_grp: # syntaxe html pour chaque groupe, dans une boucle pour réitérer l'opération pour chacun d'eux
        code = "<p>Bonjour. Vous souhaitez visiter <a href=\"%s.html\">Groupe %s</a> </p>" %(i,i)
        file_init.write(code+'\n') # écriture dans le fichier index.html

    file_init.write('</body></html>') # dernière syntaxe html du fichier
    file_init.close()
