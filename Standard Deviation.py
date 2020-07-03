import math

n = int(input())
l = list(map(int, input().split()))[:n]

µ = sum(l)//n
sumsqa = 0
for i in range(n):
  sumsqa += (l[i] - µ)*(l[i] - µ)
sumsqa = sumsqa / n


print(math.sqrt(sumsqa))  

# Using Statistic Library
# pstdev-> population standard deviation
# stdev-> sample standard deviation
from statistics import pstdev
input(), print(round(pstdev(map(int,input().split())), 1))