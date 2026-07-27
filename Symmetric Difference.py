M = int(input())
set_a = set(map(int, input().split()))
N = int(input())
set_b = set(map(int, input().split()))
c = set_a.difference(set_b)
d = set_b.difference(set_a)
set_final = sorted(list(c.union(d)))
for i in list(set_final):
    print(i)
