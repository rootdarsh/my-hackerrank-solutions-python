from itertools import product

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

result = list(product(s1,s2))
for i in result:
    print(i, end=" ")
