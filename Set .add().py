# the logic here is to add all the elements to a set, as a set doesn't allow duplicates to be stored- 'set1' only accepted unique inputs 

N = int(input())
set1 = set()
for _ in range(N):
    set1.add(input())
    
print(len(list(set1)))
