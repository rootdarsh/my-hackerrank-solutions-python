N = int(input())
integers =  list(map(str, input().split()))
print(all(int(x) > 0 for x in integers) and any(x == x[::-1] for x in integers))
