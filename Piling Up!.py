from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    d = deque(map(int, input().split()))
    
    top_block = float('inf')
    possible = True
    
    while d:
        if d[0] >= d[-1]:
            chosen = d.popleft()
        else:
            chosen = d.pop()
            
        if chosen > top_block:
            possible = False
            break
            
        top_block = chosen
        
    print("Yes" if possible else "No")
