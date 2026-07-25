balance = 0
demand = []

num_shoes = input()
shoe_sizes_av = list(map(int, input().split()))
num_cust = int(input())
for _ in range(num_cust):
    size, price_exp = input().split()
    demand.append((int(size), int(price_exp)))

for i, j in demand:
    if i in shoe_sizes_av:
        balance += j
        shoe_sizes_av.remove(i)
    elif i not in shoe_sizes_av:
        balance += 0

print(balance)
