#Uses python3
import sys
import math
from operator import itemgetter

def distance (x1,x2,y1,y2):
	dis = ((x1-x2)**2+(y1-y2)**2)**0.5
	return round(dis,4)

def minimum_distance(x, y,left,right):
    #write your code here
    n = right - left
    if n <= 3:
    	if n == 2 : return distance(x[left],x[right-1],y[left],y[right-1])
    	elif n == 3:
    		dis = [0] * 3
    		dis[0] = distance(x[left],x[left+1],y[left],y[left+1])
    		dis[1] = distance(x[right-1],x[left+1],y[right-1],y[left+1])
    		dis[2] = distance(x[left],x[right-1],y[left],y[right-1])
    		return min(dis)
    mid = n // 2
    d1 = minimum_distance(x,y,left,mid)
    d2 = minimum_distance(x,y,mid,right)
    d = min(d1,d2)
    left_selected = []
    right_selected = []
    
    for e in range(mid-1,left-1,-1):
    	if abs(x[e]-x[mid]) <= d:
    		left_selected.append((x[e],y[e]))

    for e in range(mid,right):
    	if abs(x[e] - x[mid]) <= d:
    		right_selected.append((x[e],y[e]))

    right_selected.sort(key=itemgetter(1))

    for tupl in left_selected:
    	for tupr in right_selected:
    		if abs(tupl[1]-tupr[1]) <= d:
    			dc = distance(tupl[0],tupr[0],tupl[1],tupr[1])
    			if dc < d : d = dc
    		else: break
    
    return d

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data = list(map(int, input().split()))

    n = data[0]
    x = data[1::2]
    y = data[2::2]

    x_sorted = [0] * n
    y_sorted = [0] * n
    i = 0
    index = sorted(range(n),key = x.__getitem__)
    
    for e in index:
    	x_sorted[i] = x[e]
    	y_sorted[i] = y[e]
    	i += 1
    # print(x_sorted)
    # print(y_sorted)


    print("{0}".format(minimum_distance(x_sorted, y_sorted,0,n)))
