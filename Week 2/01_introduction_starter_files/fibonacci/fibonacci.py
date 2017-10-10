# Uses python3
# naive 
# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
	seq = [0,1]
	if n > 1:
		for i in range(2,n+1):
			seq.append(seq[i-1]+seq[i-2])
	return seq[n]

n = int(input())
# assert(n <= 45 & n>= 0)

print(calc_fib(n))
