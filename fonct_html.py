# !/usr/bin/python3
# -*- coding: utf-8 -*-
from getpass import getpass

from bs4 import BeautifulSoup
from robobrowser import RoboBrowser


def test_login_url_helper():
    client = cas.CASClientBase(
                        renew=False,
                        extra_login_params=False,
                        server_url='http://www.example.com/cas/',
                        service_url='http://testserver/'
                    )
    actual = client.get_login_url()
    expected = 'http://www.example.com/cas/login?service=http%3A%2F%2Ftestserver%2F'

def dl_src():

    browser = RoboBrowser(parser='html.parser')
    browser.open(str(input("Saissisez l'URL de la page (http://iutsa.unice.fr/~mgautero/ext/M3206/trombino): ")))

    form = browser.get_form()
    form['username'].value = str(input("Saissisez votre identifiant: "))
    form['password'].value =str(getpass("Saissisez votre mot de pass: "))
    browser.submit_form(form)
    out = open('dl.html', 'w')
    out.write(browser.parsed)
    out.close()

def cor_html(file_o):
    file_split = file_o.split(".")  # Modification du nom du fichier pour que le fichier corrigé soit de la forme *_correct.html
    file_split[-2] += "_correct"
    file_c = ".".join(file_split)
    f_init = open(file_o, "r")  # ouvrir le fichier original en lecture
    contenu = ''
    for i in f_init:
        line = i
        line = line.replace("</header>", "</header></body>")  # remplacement des erreurs dans le fichier html
        line = line.replace("cellpading", "cellpadding")  # remplacement des erreurs dans le fichier html
        line = line.replace("nowrap=\"true\" align=\"left\"",
                            "align=\"left\" nowrap")  # remplacement des erreurs dans le fichier html
        line = line.replace("<td valign=\"center\"",
                            "<td valign=\"middle\"")  # remplacement des erreurs dans le fichier html
        contenu = contenu + line

    f_c = open(file_c, "w")  # ouverture du fichier corrigé en écriture pour inscrire l'ensemble du contenu du fichier original
    f_c.write(contenu)  # Remplacement des éléments corrigés
    f_c.close()  # fermer le fichier

    return file_c

def parse_html(file_h):													# Définition de la fonction
    opening = open(file_h, "r")											# Ouverture du fichier en mode read
    soup = BeautifulSoup(opening, "html.parser")							# Utilisation du parser html via Beautifulsoup
    a = soup.find_all("td", valign="top", width="16%", align="center")
    liste_user = []
    for user in a:
        nom = (user.get_text()).replace('\r', '').replace('\n', '')  # Prend juste le texte et enlelve les espaces blancs
        image = user.find("img").get('src')
        liste_user.append([nom,image])

    return liste_user
