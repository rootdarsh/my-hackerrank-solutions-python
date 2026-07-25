import calendar
mm, dd, yyyy = map(int, input().split())
weekday_index = calendar.weekday(yyyy, mm, dd)
print((calendar.day_name[weekday_index]).upper())
