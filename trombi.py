#!/usr/bin/python3
from cor_html import cor_html
from parse_html import parse_html

src_html = "index.html"  # Nom du fichier html a scanner
src_csv = "rt2.csv"  # Nom du CSV

html = cor_html(src_html) # Corrige l'html

list_h = parse_html(html) # Prend l'html et retourne une liste de persones

list_c = parse_csv(src_csv) # Prend le csv et retourne une liste

list_m = merge_list(list_h,list_c) # Regroupe les deux listes par noms

groups = scan_groups(list_m)

for g in groups:
    pass