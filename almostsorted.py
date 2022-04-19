#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    newarr = [x for x in arr]
    newarr.sort()
    inverted = []

    rank = {}  
    for i in range(len(newarr)):
        rank[newarr[i]]=i
        if arr[i]!=newarr[i]:
            inverted.append(i)
        
    if len(inverted)==2:
        print("yes")
        print("swap",inverted[0],inverted[1])
    else:
        check=True
        print("Inverted:",len(inverted),inverted[0],inverted[-1])
        #print(arr[inverted[0]:inverted[-1]])
        currentRank=rank[arr[inverted[0]]]
        for i in range(1,len(inverted)):
            if rank[arr[inverted[i]]]>=currentRank:
                print(currentRank, rank[arr[inverted[i]]],inverted[i],arr[inverted[i]])
                check=False
                break
            else:
                currentRank=rank[arr[inverted[i]]]
        if check==True:
            print("yes")
            print("reverse",inverted[0]+1,inverted[-1]+1)
        else:
            print("no")


#6
#1 5 4 3 2 6

if __name__ == '__main__':
    f = open("data.txt", "r")
    n = int(f.readline())
    print(n)
    arr = list(map(int, f.readline().split()))
    print(len(arr))
    
    #n = int(input().strip())
    #n =6
    #arr = list(map(int, input().rstrip().split()))
    
    #arr = [1, 5, 4, 3, 2, 6]
    almostSorted(arr)
