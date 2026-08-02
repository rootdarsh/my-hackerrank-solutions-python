el_A = int(input())
A = set(map(int, input().split()))
N = int(input())
commands = []
sets = []
for _ in range(int(N)):
    commands.append(input().split()[0])
    sets.append(set(map(int, input().split())))
    
for i,command in enumerate(commands):
    if command == "intersection_update":
        A.intersection_update(sets[i])
    elif command == "update":
        A.update(sets[i])
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(sets[i])
    elif command == "difference_update":
        A.difference_update(sets[i])

print(sum(A))
