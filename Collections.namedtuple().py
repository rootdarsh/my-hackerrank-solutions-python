from collections import namedtuple
stud_total_marks = 0
N = int(input())
col_name = input().split()
Student = namedtuple('Student', col_name)
for _ in range(N):
    student = Student(*input().split())
    stud_total_marks += int(student.MARKS)

print(stud_total_marks/N)
