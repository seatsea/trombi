# !/usr/bin/python3
#-*- coding: utf-8 -*-

def gen_index(list_grp):
    print(list_grp)
    file_init = open("index.html",'w')
    file_init.write('<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"></head><body>'+'\n')
    for i in list_grp:
        code = "<p>Bonjour. Vous souhaitez visiter <a href=\"%s.html\">Groupe %s</a> </p>" %(i,i)
        file_init.write(code+'\n')

    file_init.write('</body></html>')
    file_init.close()
