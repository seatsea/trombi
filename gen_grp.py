# !/usr/bin/python3
#-*- coding: utf-8 -*-

def construct_grp(grp,list_personne):

    file_init = open("%s.html" %(grp), 'w')
    file_init.write('<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><title>Groupe ' + grp + '"</title></head><body><p>Page du Groupe ' + grp + ' </p><table width = "100%">' + "\n")
    for personne in list_personne:
            file_init.write('<tbody> <tr> <td width = "16%" valign = "top" align = "center" ><img src = "/' + personne[1] + '" width = "120" height = "160&quot;" > <br> ' + personne[0] + ' </td> <td width = "16%" valign = "top" align  "center" ></tr></tbody></table></body></html>' "\n")

    file_init.write()
    file_init.close()

construct_grp('1A',[['Aqil Ridhwan Bin Mohd Shukri Muhammad', 'trombinos.unice.fr_fichiers/image_005.jpeg'], ['Nur Izzati Binti Abd Haris', 'trombinos.unice.fr_fichiers/image_046.jpeg'], ['Manon Bonino', 'trombinos.unice.fr_fichiers/image_019.jpeg'], ['Baptiste Bonnaudet', 'trombinos.unice.fr_fichiers/image_013.jpeg'], ['Dorian Dragoni', 'trombinos.unice.fr_fichiers/image_009.jpeg'], ['Leo Leffy', 'trombinos.unice.fr_fichiers/image_032.jpeg'], ['Marie-Amelie Maniscalco', 'trombinos.unice.fr_fichiers/image_026.jpeg'], ['Lakic Perovanovic', 'trombinos.unice.fr_fichiers/image_036.jpeg'], ['Erwan Pisano', 'trombinos.unice.fr_fichiers/image_023.jpeg'], ['Jeremie Rafinesque', 'trombinos.unice.fr_fichiers/image_012.jpeg'], ['Gaetan Rival', 'trombinos.unice.fr_fichiers/image_003.jpeg'], ['Theo Sigari', 'trombinos.unice.fr_fichiers/image_030.jpeg'], ['Andy Squadra', 'trombinos.unice.fr_fichiers/image_024.jpeg'], ['Thomas Tenret', 'trombinos.unice.fr_fichiers/image_038.jpeg']])