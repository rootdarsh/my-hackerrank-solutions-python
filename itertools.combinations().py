from itertools import combinations

S, k = input().split()

for x in range(1, (int(k)+1)):
    result =  list(combinations(sorted(S), int(x)))
    for _ in result:
        print("".join(_))
