import numpy as np

f = open("a_example.txt", "r")
H = []
V = []

def parse_input(file):
    list = [line.split(' ') for line in file.read().split('\n')]
    return list


def getNumber(list):
    number = int((list.pop(0))[0])
    return number


def sortLists(list):
    for i in range(0,len(list)-1): # je mag niet meer als 1 keer dit doen
        tup = [i] + list[i]
        tup[2] = int(float(tup[2]))
        print(tup)
        if list[i][0] == 'H':
            H.append(tup)
        elif list[i][0] == 'V':
            V.append(tup)


def getHorizontalPhotos():
    return H


def getVerticalPhotos():
    return V


def getNumberOfPhotos():
    return n


l = parse_input(f)
n = getNumberOfPhotos(l)
sortLists(l)

