import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
t = str.upper(t)

indexing_list = [ord(letter)-65 for letter in t]
aux = []
for letter in indexing_list:
    if  letter == -1:
        aux.append(26)
    else : 
        aux.append(letter)
indexing_list = aux 

for i in range(h):
    row = input()
    result = ""
    for index in indexing_list:
        result = result + row[index*l: index*l + l ]
    print(result)
        
