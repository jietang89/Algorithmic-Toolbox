# Uses python3
import sys
import math

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here

    def binary(a,left,right,x):
        if right < left: return -1
        mid = int((left+right)/2)
        if x == a[mid]: return mid
        elif x < a[mid]: return binary(a,left,mid-1,x)
        else: return binary(a,mid+1,right,x)
    return binary(a,left,right,x)

    # if right < left: return -1
    # mid = int((left+right)/2)
    # if x == a[mid]: return mid
    # elif x < a[mid]: return binary_search(a[:mid],x)
    # else: 
    #     check = binary_search(a[mid+1:],x)
    #     if check != -1: return check+mid+1
    #     return check

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    # data = list(map(int, input().split()))

    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
        # print(linear_search(a, x), end = ' ')
