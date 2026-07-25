def is_leap(year):
    leap = True
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 ==0 and year % 400 == 0):
        return leap
    else:
        return not leap
    
    
year = int(input())
print(is_leap(year))
