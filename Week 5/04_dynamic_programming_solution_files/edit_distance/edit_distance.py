# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    value = [[0]*(n+1) for i in range(m+1)]
    value[0] = [i for i in range(n+1)]
    for i in range(m+1):
    	value[i][0] = i
    # print(value)
    for j in range(1,n+1):
    	for i in range(1,m+1):
    		if s[i-1] == t[j-1]:
    			value[i][j] = value[i-1][j-1]
    		else:
    			value[i][j] = min(value[i-1][j-1],value[i-1][j],value[i][j-1])+1
    return value[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
