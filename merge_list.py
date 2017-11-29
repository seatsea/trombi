#!/usr/bin/python3

def merge_list(list_h, list_c):
    list_h = map(list, list_h)
    list_c = map(list, list_c)
    print(list_h)
    print(list_c)

    for item in list_h:
        item += [x[1] for x in list_c if x[0] == item[0]]

    list_h += [x for x in list_c if not any(i for i in list_h if x[0] == i[0])]

    print
    list_h

merge_list([('to','toto','img'),('ta','tata','img2')],[('to','toto','1A'),('ta','tata','1B')])