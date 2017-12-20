# !/usr/bin/python3
#-*- coding: utf-8 -*-

def construct_grp(grp,list_personne): # fonction permettant de trier chaque groupe et d'en afficher

    file_init = open("%s.html" %(grp), 'w') # création du fichier **.html suivrant le nom du groupe
    file_init.write('<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><title>Groupe ' + grp + '"</title></head><body><p>Page du Groupe ' + grp + ' </p><table width = "100%"><tbody> <tr> ' + "\n")
    # syntaxe html début de mise en page de tri entre les photos et infos des étudiants
    c = 0
    for personne in list_personne: # remplis avec les infos des étudiants et leurs photos dans une boucle
        file_init.write('<td width = "16%" valign = "top" align = "center" ><img src = "' + personne[1] + '" width = "120" height = "160&quot;" > <br> ' + personne[0] + ' </td>' "\n")
        c += 1
        if c > 3:
            file_init.write("</tr> \n <tr>")
            c = 0


    file_init.write('</tbody></table></body></html>')
    file_init.close()
# syntaxe html de fin de fichier permettant de finir proprement le code html