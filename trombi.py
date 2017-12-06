#!/usr/bin/python3
from fonct_html import *
from parse_csv import parse_csv
from gen_index import gen_index
# from gen_grp import construct_grp

src_csv = "rt2.csv"  # Nom du CSV

option = 0
option = int(input("Fichier en ligne: 1 Fichier local : 2 : " ))# Mode de fonction
if option == 1:
    dl_src()
    html = cor_html('dl.html')
elif option == 2:
    src_html = str(input("Nom du fichier html: "))
    html = cor_html(src_html)
else:
    print("Choix invalide")
    exit(5)

list_h = parse_html(html) # Prend l'html et retourne une liste de persones

list_c = parse_csv(src_csv) # Prend le csv et retourne une liste

groups = []
for key in list_c:
    if key[1] not in groups:
        groups.append(key[1])


for i in groups:
    users_group = []
    for n in range(0,len(list_c)):
        if list_c[n][1] == i:
            for x in range(0,len(list_h)):
                if list_h[x][0] == list_c[n][0]:
                    users_group.append(list_h[x])
    print(users_group)
    # construct_grp(i,users_group)


gen_index(groups)
