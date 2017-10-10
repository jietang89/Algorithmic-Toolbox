# Uses python3
import sys

def get_optimal_value(n,capacity, weights, values):
    # write your code here
    rate = [values[x]/weights[x] for x in range(n)]
    index = list(reversed(sorted(list(range(n)),key=rate.__getitem__)))
    total_val = 0
    for i in range(n):
    	j = index[i]
    	num = min(capacity,weights[j])
    	total_val = total_val + num * rate[j]
    	capacity = capacity - num
    	if capacity == 0: break
    	

    return round(total_val,4)



data = list(map(int, sys.stdin.read().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
# print(data)
opt_value = get_optimal_value(n,capacity, weights, values)
print(opt_value)
