# Uses python3
# import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum % 10

def fibonacci_sum(n):
    
    sseq = [0,1,2]
    if n > 2:
        for i in range(3,n+1):
            aa = sseq[i-2]+sseq[i-1]+1
            sseq.append(aa % 10)
            if sseq[i-1] == 9:
                if sseq[i] == 0:
                    return (sseq[n%(i+1)])
    return(sseq[n])


n = int(input())
assert(n >= 0)
print(fibonacci_sum(n))
