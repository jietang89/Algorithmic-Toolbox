# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    # if n <= 1:
    #     return n

    # previous = 0
    # current  = 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current

    # return current % 10

    seq = [0,1]
    if n > 1:
        for i in range(2,n+1):
            a = seq[i-1]+seq[i-2]
            seq.append(a % 10)
    return(seq[n])


# input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit_naive(n))
