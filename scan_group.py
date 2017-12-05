#!/usr/bin/python3
import csv


def group(liste):
    groups = []
    for i in liste:
        if i[2] not in groups:
            groups.append(i[2])
            print(groups)

    groups.sort()

    return groups
