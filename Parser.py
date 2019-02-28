import numpy as np
import hashcode_main as m

f = open("c_memorable_moments.txt", "r")
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
        if list[i][0] == 'H':
            H.append(tup)
        elif list[i][0] == 'V':
            V.append(tup)


#
# def getHorizontalPhotos():
#     return H
#
#
# def getVerticalPhotos():
#     return V
#
#
# def getNumberOfPhotos():
#     return n





#--------------------------------------

def output(slideshow):
    submission= open("submission_memerable_moments.txt","w+")
    c = len(slideshow)
    submission.write("%d \n" % c)
    for i in range(0,c):
        if isinstance(slideshow[i][0] , int):
            submission.write("%d \n" % slideshow[i][0])
        else:
            submission.write("%d" % slideshow[i][0][0])
            submission.write(" %d \n" % slideshow[i][0][1])


l = parse_input(f)
n = getNumber(l)
sortLists(l)
test =[[1,"a"],[[1,2],"b"]]
V_assembled = m.assembleVerticals(V)
final_show = m.create_slideshows(H+V_assembled)
output(final_show)