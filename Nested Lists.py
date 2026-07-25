if __name__ == '__main__':
    names = []
    scores = []
    stud_data = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        stud_data.append([name, score])

scores = sorted(set(scores))

sec_lowest_score = scores[1]
#print(sec_lowest_score)
sec_lowest_stud = [name for name, score in stud_data if score == sec_lowest_score]
sec_lowest_stud.sort()
for i in sec_lowest_stud:
    print(i)
