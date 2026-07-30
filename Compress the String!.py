from itertools import groupby

groups = []
S= input()
for k,g in groupby(S):
    grp_length = len(list(g))
    print((grp_length, int(k)), end=" ")
