def total(d):

    #set variable total to the number of items in all the lists that occur as values in d.

    total = 0
        for k in d:
        total = total + len(d[k])
    return total


'''L = []
for k in d:
    L.extend(d[k])

total = len(L)
'''

