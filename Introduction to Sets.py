def average(array):
    res = sum(set(arr))
    res1 = res/(len(set(arr)))
    return res1
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
