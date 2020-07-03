n = int(input())
l = list(map(int, input.split()))[:n]
from statistics import median

q1 = median(l)

ql1 = l[:q1]
q2 = median(ql1)

ql2 = l[q1:]
q3 = median(ql2)

print(q1)
print(q2)
print(q3)