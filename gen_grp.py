# !/usr/bin/python3
#-*- coding: utf-8 -*-

def construct_grp(list_grp):

    for i in list_grp:
        file_init = open("%s.html" %(i), 'w')
        file_init.write('<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"><title>Groupe %s</title></head><body><p>Page du Groupe %s </p></body></html>' %(i,i))
        <table width = \"100%\"><tbody><tr><td width = \"16%\" valign = \"top\" align = \"center\" ><img src = \"trombinos.unice.fr_fichiers/image_043.jpeg\" width = \"120\" height = \"160&quot;\" > <br> Amin Abdessadki </td> <td width = \"16%\" valign = \"top\" align  \"center\" >

    file_init.close()

construct_grp(['1A','1B','2A','2B','3'])