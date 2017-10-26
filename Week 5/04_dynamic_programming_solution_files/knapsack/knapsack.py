# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    # value = [[0]*(W+1)]*(n+1) copy wrong!
    value = [[0]*(W+1) for i in range(n+1)]
    # print(value[0],value[1])
    for i in range(1,n+1):
    	# if i != 1: break
    	for e in range(1,W+1):
    		value[i][e] = value[i-1][e]

    		# print(value[i][e],i,e)
    		if w[i-1] <= e:
    			val = value[i-1][e-w[i-1]] + w[i-1]
    			if val > value[i][e]:
    				value[i][e] = val
    	# print(value)

    return value[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W, n, *w = list(map(int, input().split()))

    print(optimal_weight(W, w))
