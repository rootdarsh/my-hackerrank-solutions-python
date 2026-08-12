lower_case = []
upper_case = []
odd_num = []
even_num = []
S = input()
for char in S:
    if char.isalpha():
        if char.isupper():
            upper_case.append(char)
        else:
            lower_case.append(char)
    elif char.isdigit():
        if int(char) % 2==0:
            even_num.append(char)
        else:
            odd_num.append(char)
lower_case.sort()
upper_case.sort()   
odd_num.sort()
even_num.sort()
print(f"{''.join(lower_case)}{''.join(upper_case)}{''.join(odd_num)}{''.join(even_num)}") 
