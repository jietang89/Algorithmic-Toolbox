# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def min_index(c,index1,*index2):
    index = index1
    value = c[0]
    j = 1
    for i in index2:
        if c[j] < value: 
            value,index = c[j],i
            j += 1
    return value+1,index

def optimal_dp(n):
    if n < 2: return [1]

    c = [0] * (n+1)
    t = [0] * (n+1)

    c[2] = 1
    t[2] = 1
    for i in range(3,n+1):
        if i % 3 == 0:
            if i % 2 == 0:
                c[i],t[i] = min_index([c[i//2],c[i//3],c[i-1]],\
                    i//2,i//3,i-1)
            else:
                c[i],t[i] = min_index([c[i//3],c[i-1]],\
                    i//3,i-1)
        elif i % 2 ==0:
            c[i],t[i] = min_index([c[i//2],c[i-1]],\
                    i//2,i-1)
        else:
            c[i] = c[i-1] + 1
            t[i] = i-1

    m = [0] * (c[n] + 1)
    m[0] = n
    for i in range(len(m)-1):
        m[i+1] = t[m[i]]
    m.sort()
    return m



# input = sys.stdin.read()
n = int(input())
sequence = optimal_dp(n)
# sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
