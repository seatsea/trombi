# !/usr/bin/python3
#-*- coding: utf-8 -*-

def construct_grp(grp,list_personne):

    for personne in list_personne:
        personne = i
        file_init = open("%s.html" %(i[0]), 'w')
        file_init.write("<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"><title>Groupe %s</title></head><body><p>Page du Groupe %s </p><table width = \"100%\">") %(i[0]) %(i[0])
        file_init.write("<tbody> <tr> <td width = \"16%\" valign = \"top\" align = \"center\" ><img src = \"%s\" width = \"120\" height = \"160&quot;\" > <br> %s %s </td> <td width = \"16%\" valign = \"top\" align  \"center\" ></tr></tbody></table></body></html>") %(j[1][2]) %(j[1][0]) %(j[1][1])
    file_init.close()

construct_grp('1A',['Amin','Abdessaki','trombinos.unice.fr_fichiers/image_043.jpeg'])