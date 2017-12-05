# !/usr/bin/python3
#-*- coding: utf-8 -*-

def construct_grp(grp,list_personne):

    for personne in list_personne:
        file_init = open("%s.html" %(personne[0]), 'w')
        file_init.write("<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"><title>Groupe %s</title></head><body><p>Page du Groupe %s </p><table width = \"100%\">") %(personne[0]) %(personne[0])
        file_init.write("<tbody> <tr> <td width = \"16%\" valign = \"top\" align = \"center\" ><img src = \"/%s\" width = \"120\" height = \"160&quot;\" > <br> %s </td> <td width = \"16%\" valign = \"top\" align  \"center\" ></tr></tbody></table></body></html>") %(personne[1][1]) %(personne[1][0])
    file_init.close()

construct_grp('1A',['Amin Abdessaki','http://iutsa.unice.fr/~mgautero/ext/M3206/trombino/trombinos.unice.fr_fichiers/image_043.jpeg'])