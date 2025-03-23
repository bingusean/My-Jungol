l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
inp = int(input())
li = l[::2]
lis = li[0:inp//2+1]
lis.reverse()
print(lis)