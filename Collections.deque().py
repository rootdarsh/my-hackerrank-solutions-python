from collections import deque

d = deque()
N = int(input())
operations = []

for _ in range(N):
    commands = input().split()
    command = commands[0]
    integer = commands[1] if len(commands) > 1 else 0
    operations.append((command,integer))

for command,integer in operations:
    if command == "append":
        d.append(integer)
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()
    elif command == "appendleft":
        d.appendleft(integer)
    else:
        None

print(*d)
