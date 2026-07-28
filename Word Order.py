from collections import Counter
n = input()
unique_words = []
for _ in range(int(n)):
    unique_words.append(input())
distinct_list = set(unique_words)

print(len(distinct_list))
unique_words_counts = Counter(unique_words)

for unique_word, count in unique_words_counts.items():
    print(count, end= " ")
