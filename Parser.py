import numpy as np




file = open("a_example.in", "r")


def parse_input(file):
    list = [line.split(' ') for line in file.read().split('\n')]
    print(list)
    return list


def getNumberOfRows(list):
    return int(list[0][0])


def getNumberOfCollumnz(list):
    return int(list[0][1])


def getMinIngredients(list):
    return int(list[0][2])


def getMaxCells(list):
    return int(list[0][3])


def getPizza(list):
    result = []
    for row in list[1:-1]:
        r = []
        for i in range(0, getNumberOfCollumnz(list)):
            r.append(row[0][i])
        result.append(r)
    return result


list = parse_input(file)
print(getPizza(list))