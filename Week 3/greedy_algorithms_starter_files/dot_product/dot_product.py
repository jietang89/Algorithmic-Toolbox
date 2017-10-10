#Uses python3

import sys

# def sorted(x,y):
#     if x == []:return y    
#     a = max(x)
#     y.append(a)
#     x.remove(a)
#     return sorted(x,y)



def max_dot_product(a, b):
    #write your code here

    # a = sorted(a,[])
    # b = sorted(b,[])

    a = list(sorted(a,reverse=True))
    b = list(sorted(b,reverse=True))

    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = list(map(int, input().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    # print(sorted(a),y=[])
    # print(sorted(b),y=[])
    # print(a)
    # print(b)
    print(max_dot_product(a, b))
    
