# Uses python3

def gcd_naive(a, b):
    if b == 0:
    	return(a)

    c = a % b
    return gcd_naive(b,c)

def lcm_naive(a, b):
    # for l in range(1, a*b + 1):
    #     if l % a == 0 and l % b == 0:
    #         return l

    # return a*b
    
    return int(a*b//gcd_naive(a,b))


a, b = map(int, input().split())
print(lcm_naive(a, b))

