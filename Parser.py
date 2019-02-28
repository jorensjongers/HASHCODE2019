import numpy as np

f = open("a_example.txt", "r")
H = []
V = []

def parse_input(file):
    list = [line.split(' ') for line in file.read().split('\n')]
    return list


def getNumberOfPhotos(list):
    number = int((list.pop(0))[0])
    return number


def sortLists(list):
    for i in range(0,len(list)):
        tup = [i] + list[i]
        if list[i][0] == 'H':
            H.append(tup)
        elif list[i][0] == 'V':
            V.append(tup)





l = parse_input(f)
n = getNumberOfPhotos(l)
sortLists(l)
print('h:')
print(H)
print('v:')
print(V)