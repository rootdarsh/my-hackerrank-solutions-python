from collections import Counter
K =int(input())
entries = list(map(int, input().split()))
counts = Counter(entries)
for entry, count in counts.items():
    if count == 1:
        print(entry)
