happ_count = 0
n, m = input().split()
arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

for i in arr:
    if i in set_A:
        happ_count += 1
    elif i in set_B:
        happ_count -= 1
   
print(happ_count)
