T = int(input())
for i in range(T):
    try:
        a, b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
