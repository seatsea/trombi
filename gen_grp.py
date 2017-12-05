# !/usr/bin/python3
#-*- coding: utf-8 -*-

def construct_grp(list_grp):

    for i in list_grp:
        file_init = open("%s.html" %(i), 'w')
        file_init.write("<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"><title>Groupe %s</title></head><body><p>Page du Groupe %s </p><table width = \"100%\">") %(i,i))

        for j in list_stu:
            file_init.write("<tbody> <tr> <td width = \"16%\" valign = \"top\" align = \"center\" ><img src = \"%s\" width = \"120\" height = \"160&quot;\" > <br> %s %s </td> <td width = \"16%\" valign = \"top\" align  \"center\" ></tr></tbody></table></body></html>") %(j[],j[],j[],j[])
    file_init.close()

construct_grp(['1A','1B','2A','2B','3'])