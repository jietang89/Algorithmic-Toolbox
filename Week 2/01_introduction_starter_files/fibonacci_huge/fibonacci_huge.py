# Uses python3


def get_fibonacci_huge_naive(n, m):
    if m == 1: return (0)
    if n <= 1: return (n)

    period = [0,1]

    for i in range (2,n+1):
    	period.append((period[i-2]+period[i-1]) % m)
    	if period[i] == 1:
    		if period [i-1] == m-1:
    			# print(i+1)
    			return (period[n%(i+1)])
    
    return (period[n])
    	


    # previous = 0
    # current  = 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current

    # return current % m


n, m = map(int, input().split())
# n,m = 2015,3
print(get_fibonacci_huge_naive(n, m))
