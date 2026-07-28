N = input()
operations = []
for i in range(int(N)):
    commands = input().split(maxsplit=1)
    command = commands[0]
    integer = int(commands[1]) if len(commands) > 1 else 0
    operations.append((command,integer))

# for i,j in commands.items():
#     print(i,j)

for command, integer in operations:
    if command == "pop":
        try:
            s.pop()
        except KeyError:
            None
    elif command == "remove" and integer in s:
        try:
            s.remove(integer)
        except KeyError:
            None
    elif command == "discard" and integer in s:
        s.discard(integer)
    else:
        None
    
print(sum(s))
