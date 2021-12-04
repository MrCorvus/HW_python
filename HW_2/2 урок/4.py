counts = [14.12, 51.1, 16.43, 17, 56.51, 65.1, 34, 15.66]
counts = [str(e) for e in counts]


for i, e in enumerate(counts):
    if len(e) == 4:
        counts[i] = f'{e[0:2]}.0{e[3:]}'
    if len(e) == 2:
        counts[i] = f'{float(e):.02f}'
for i, e in enumerate(counts):
    if len(e) == 5:
        counts[i] = f'{e[0:2]}r{e[3:]}kk'

print(counts)
counts.sort()
print(counts)
rev_counts = list(reversed(counts))
print(rev_counts)
print(list(sorted(rev_counts[0:5])))
