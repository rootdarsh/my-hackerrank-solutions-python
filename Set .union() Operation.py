a = int(input())
english = set(map(int, input().split()))
b= int(input())
french = set(map(int, input().split()))

req = english.union(french)
print(len(req))
