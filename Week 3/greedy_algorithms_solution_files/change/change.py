# Uses python3

def get_change(m):
    #write your code here
    sort = [10,5,1]
    n = 0
    for i in range(3):
    	(num,rest) = divmod(m,sort[i])
    	n = n + num
    	if rest == 0:break
    	m = rest
    return n


m = int(input())
print(get_change(m))
