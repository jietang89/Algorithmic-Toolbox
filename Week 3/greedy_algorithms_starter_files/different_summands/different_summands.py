# Uses python3
import sys
# from sympy import *

# def optimal_summands(n):
#     summands = []
#     #write your code here

#     x = Symbol('x')
#     xl = sorted(solve(x*(x+1)-2*n,x),reverse = True)

#     max_num = int(xl[0])
#     # print(xl)
#     summands = [i for i in range(1,max_num+1)]
#     summands[-1] = summands[-1] + (n-(max_num+1)*max_num/2)
#     return summands

def optimal_summands(n):
	summands = []

	for i in range(int((2*n)**(1/2)),0,-1):
		sump = i*(i+1)/2
		if sump > n: continue

		summands = [i for i in range(1,i+1)]
		summands[-1] = summands[-1] + (n - i*(i+1)/2)
		return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = int(input())

    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(int(x), end=' ')
