# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here

    return -1


def get_majority_element2(a,n):
    ma = 0
    for e in a:
        if e > ma: 
            ma = e
    # print(ma)
    count = [0]*ma
    # print(count)
    for e in a:
        count[e-1] = count[e-1] + 1
    # print(count)
        if count[e-1] > int(n/2): return e
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, *a = list(map(int, input().split()))

    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)

    if get_majority_element2(a, n) != -1:
        print(1)
    else:
        print(0)
    # get_majority_element2(a,n)