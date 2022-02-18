def removeDuplicates(myTuple):
    return list(set([i for i in myTuple]))
myTuple = ('Red','Blue','Green','Red','Orange','Green')
print(removeDuplicates(myTuple))