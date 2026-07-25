from itertools import permutations

list1 = []
list2 = []
S , k = input().split()
for i in S:
    list1.append(i)


result = list(permutations(list1, int(k)))
for x in result:
    r = ''.join(x)
    list2.append(r)

list2.sort()
for _ in list2:
    print(_)
