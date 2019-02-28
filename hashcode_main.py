# ik wil geen parser file

from operator import itemgetter

COMPARE_CONST = 100

verticals = [(1, 'V', 2, 'bla', 'blad'),
             (2, 'V', 3, 'a', 'b', 'c'),
             (3, 'V', 2, 'r', 't'),
             (4, 'v', 4, 'r', 's', 'bla', 'k')]


# Assemble verticals into single slides in a way that maximizes the number of unique tags per slide
# and averages out the number of tags per slide.

def interest_factor(slide1, slide2):
    tags1 = getTags(slide1)
    tags2 = getTags(slide2)
    unique_tags1 = tags1  - tags2
    unique_tags2 = tags2  - tags1
    common_tags = tags1  & tags2
    return min(len(unique_tags1), len(unique_tags2), len(common_tags))


def getTags(picture):
    #print(picture)
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
    for tag in unionTags:
         slide.append(tag)
    return slide

def sort_pictures(pictures):
    return sorted(pictures, key=itemgetter(2))

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


# returns optimal following slide to given slide from slideset sorted_slides.
# search whithin limited range.
# Assume the given slide is not in the list of sorted slides.

def find_best_next(slide, index, sorted_slides):

    search_range = 100#len(sorted_slides) // COMPARE_CONST
    if search_range == 0:
        search_range = 2
    start_index = min(max(0, index - (search_range//2 + 1)), len(sorted_slides) - (search_range//2 + 1))
    best_score = 0
    best_next = []

    for i in range(0, min(search_range,(len(sorted_slides)//2-1))):
        if start_index <= len(sorted_slides):
            start_index = 0
        to_compare = sorted_slides[index]
        score = interest_factor(slide, to_compare)

        if score > best_score:
            best_next = []
            best_next.append(to_compare)
            best_score = score
        elif (score == best_score):
            best_next.append(to_compare)

        start_index += 1

    return best_next

def create_slideshows(list):
    slideshow =[]
    currentslide = list[0]
    i = 0
    while len(list) != 1:
        slideshow.append(currentslide)
        index =list.index(currentslide)
        list.remove(currentslide)
        nextslides = find_best_next(currentslide,index, list)
        if nextslides == []:
            slideshow.append(list[0])
            nextslide = list[0]
        else:
            nextslide= sort_pictures(nextslides)[0]
        currentslide = nextslide
        i+= 1
    slideshow.append(list[0])
    return slideshow

