# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

# result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

ls=max(a)
a.remove(ls)
rs=max(a)
result=ls*rs
print(result)
