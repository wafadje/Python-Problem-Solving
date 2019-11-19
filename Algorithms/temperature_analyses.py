import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
arr = []

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    arr.append(int(i))
 

Val_min = min([ abs(e) for e in arr])
if Val_min in arr and -Val_min in arr:
    print(Val_min)
elif  -Val_min in arr :
    print(-Val_min)
elif  Val_min in arr :
    print(Val_min)
    
