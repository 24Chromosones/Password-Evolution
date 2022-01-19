import random


def similar(word1, word2):
    matches = 0
    if len(word1) == len(word2):
        comparison = list(zip(word1, word2))
        for i in comparison:
            if i[0] == i[1]:
                matches += 1
        return matches / len(word1)
    else:
        raise Exception("Parameter lengths are not the same")


def pair(population):
    temp = [i for i in population]
    random.shuffle(temp)
    temp = list(zip(temp[0::2], temp[1::2]))
    return temp


