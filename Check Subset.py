T = int(input())
for _ in range(T):
    n_A = int(input())
    set_A = set(map(int, input().split()))
    n_B = int(input())
    set_B = set(map(int, input().split()))
    if len(set_A.intersection(set_B)) == len(set_A):
        print("True")
    else:
        print("False")


#      ////// A better and shorter method //////  (likely to be used in this problem)
      
#T = int(input())
#for _ in range(T):
#    n_A = int(input())
#    set_A = set(map(int, input().split()))
#    n_B = int(input())
#    set_B = set(map(int, input().split()))
#   result = set_A.issubset(set_B)
#    print(result)
