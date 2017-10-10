# Uses python3
# import sys

def fibonacci_partial_sum(from_, to):
    
    # sum = 0

    # current = 0
    # next  = 1

    # for i in range(to + 1):
    #     if i >= from_:
    #         sum += current

    #     current, next = next, current + next

    # return sum % 10


    def period():
    
        sseq = [0,1]
        i = 2
        while True:
            aa = sseq[i-2]+sseq[i-1]+1
            sseq.append(aa % 10)
            if sseq[i-1] == 9:
                if sseq[i] == 0:
                    return (i+1,sseq)
            i = i + 1
    
    k,sseq = period()
    if from_ == 0: return (sseq[to%k])
    else: return((sseq[to%k]-sseq[(from_-1)%k]+10)%10)



from_, to = map(int, input().split())
assert(from_<=to)
print(fibonacci_partial_sum(from_, to))