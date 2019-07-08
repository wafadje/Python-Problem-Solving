"""
Function Description

Complete the plusMinus function. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following 3 lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.

"""

import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    div = len(arr)
    
    cp, cne, cn = 0, 0, 0

    for a in arr:
        if a < 0:
            cne += 1
        elif a > 0:
            cp += 1 
        else :
            cn += 1

    print("{0:.6f}".format(cp/div,2))
    print("{0:.6f}".format(cne/div,2))
    print("{0:.6f}".format(cn/div,2))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
