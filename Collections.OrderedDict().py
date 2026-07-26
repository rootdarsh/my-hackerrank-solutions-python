from collections import OrderedDict

N = int(input())
list_final = OrderedDict()

for _ in range(N):
    key, value = input().rsplit(maxsplit=1)
    list_final[key] = list_final.get(key,0) + int(value)

for key, value in list_final.items():
    print(key, value)
