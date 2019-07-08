"""

Complete the simpleArraySum function. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers representing the array's elements.

Output Format

Print the sum of the array's elements as a single integer.

"""

#!/bin/python3

import os
import sys

# Complete the simpleArraySum function below.

def simpleArraySum(ar):
    
    res = 0
    for a in ar:
        res += a
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')

    fptr.close()
