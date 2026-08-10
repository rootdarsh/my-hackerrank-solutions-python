set_A = set(map(int, input().split()))
n = int(input())

count = 0

for _ in range(n):
    other_set = set(map(int, input().split()))
    if set_A.issuperset(other_set):
        count += 1
    else:
        count += 0

if count == int(n):
    print("True")
else:
    print("False")
