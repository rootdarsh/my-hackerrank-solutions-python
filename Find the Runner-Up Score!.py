if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
list1 = set(arr)  #to remove any duplicates
list2 = sorted(list1)   #to rearrange the list (arr) in increasing order
print(list2[-2])
