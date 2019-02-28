# ik wil geen parser file

from operator import itemgetter

COMPARE_CONST = 1000

verticals = [(1, 'V', 2, 'bla', 'blad'),
             (2, 'V', 3, 'a', 'b', 'c'),
             (3, 'V', 2, 'r', 't'),
             (4, 'v', 4, 'r', 's', 'bla', 'k')]


# Assemble verticals into single slides in a way that maximizes the number of unique tags per slide
# and averages out the number of tags per slide.

def getTags(picture):
    result = set()
    for tag in picture[3:]:
        result.add(tag)
    return result

def makeSlide(pic1, pic2, unionTags):
    slide = []
    idlist = []
    idlist.append(pic1[0])
    idlist.append(pic2[0])
    nbtags = len(unionTags)
    slide.append(idlist)
    slide.append('V')
    slide.append(nbtags)
    slide.append(unionTags)
    return slide


def assembleVerticals(verticals):

    verticals = sorted(verticals, key=itemgetter(2))
    assembled_verticals = []

    # TODO: alles in aparte dict per aantal tags

    i = 0
    j = 0

    while len(verticals) > 1:
        picture1 = verticals[i]
        picture2 = verticals[-1]
        tags1 = getTags(picture1)
        tags2 = getTags(picture2)
        if len(tags1 & tags2) == j:
            union_tags = tags1 | tags2
            assembled_verticals.append(makeSlide(picture1, picture2, union_tags))
            verticals.remove(picture1)
            verticals.remove(picture2)
            i, j = 0, 0

        else:
            i += 1
            if i == len(verticals)-1:
                j += 1
                i = 0

    return assembled_verticals



