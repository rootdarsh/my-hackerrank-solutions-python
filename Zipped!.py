N,  X = input().split()
marks = []
for _ in range(int(X)):
    marks.append(list(map(float, input().split())))

marks_zip = zip(*marks)
for i in marks_zip:
    print(sum(i)/int(X))
