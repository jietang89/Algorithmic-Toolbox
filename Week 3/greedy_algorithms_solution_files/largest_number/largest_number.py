#Uses python3

import sys

def Goe(a,b):
	first = a+b
	second = b+a
	if int(first) >= int(second): return True
	else: return False

def largest_number(a):
    #write your code here
    
    
    b = []
    while a:
    	max_digit = a[0]
    	for e in a:
    		if Goe(e,max_digit):
    			max_digit = e
    		else: continue
    	# print (max_digit)
    	# print (a)
    	# break
    	b.append(max_digit)
    	a.remove(max_digit)
    	# print(b)

    	# print (max_digit)
		# b.append(max_digit)
		# a.remove(max_digit)

    res = ""
    for x in b:
        res += str(x)
    return res

# if __name__ == '__main__':
input = sys.stdin.read()
data = input.split()
# data = input().split()

a = data[1:]
# print(a)
print(largest_number(a))
    
