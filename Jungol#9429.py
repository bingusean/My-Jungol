List = [1, 2, 3, 4]
ListToTuple = tuple(List)
TupleToList = list(ListToTuple)
Indexing = ListToTuple[3]
Slice = ListToTuple[1:3]

print('list: ' + str(List))
print('list -> tuple: ' + str(ListToTuple))
print('tuple -> list: ' + str(TupleToList))
print('indexing: ' + str(Indexing))
print('slicing: ' + str(Slice))