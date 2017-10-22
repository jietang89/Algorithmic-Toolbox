# Uses python3
import sys
from operator import itemgetter

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    # starts_new = sorted(starts)
    n = len(starts)
    starts_new = [0] * n
    ends_new = [0] * n
    it = 0
    indexl = sorted(range(n), key=starts.__getitem__)
    for e in indexl:
        # print(e,'indexl')
        starts_new[it] = starts[e]
        ends_new[it] = ends[e]
        # print(starts_new,ends_new,it)
        it += 1

    # print(indexl)
    # print(starts_new)
    # print(ends_new)
    for i in range(len(points)):
        num = binary_search(starts_new,0,n,points[i])
        for j in range(num+1):
            if points[i] <= ends_new[j]:
                cnt[i] += 1

    # for i in range(len(points)):
    #     for j in range(len(starts)):
    #         if starts[j] <= points[i] <= ends[j]:
    #             cnt[i] += 1    
    return cnt

def fast_count_segments2(starts, ends, points):
    m = len(points)
    cnt = [0] * m
    points_new = [0] * m
    n = len(starts)
    points_new[:] = points[:]

    for i in range(n):
        starts[i] = (starts[i],'a')
        ends[i] = (ends[i],'c')
    for i in range(m):
        points[i] = (points[i],'b')

    t = starts + ends + points

    t.sort(key=itemgetter(0,1))

    indexl = sorted(range(m),key = points_new.__getitem__)
    
    count = 0
    nump = 0
    # print('total:',t)
    # print('starts:',starts)
    # print('ends:',ends)
    # print('points:',points)
    for i in range(2*n+m):
        # print('current:',t[i][0])
        if t[i][1] == 'a': 
            count += 1
            # print(t[i],count)
        elif t[i][1] == 'c': 
            count -= 1
            # print(t[i],count)
        elif t[i][1] == 'b':
            # current = points_new.index(t[i][0])
            cnt[indexl[nump]] = count
            # points_new[current] = 0.1
            nump += 1
            if nump == m: return cnt

def binary_search(a,left,right,point):
    # print(a[left:right])
    if right - left == 1:
        if point < a[left]: return -1
        # print('end:',left)
        return left 

    mid = (left+right) // 2
    if point < a[mid]:
        return(binary_search(a,left,mid,point))
        # print(num,'left')
    else:
        return(binary_search(a,mid,right,point))
        # print(num,'right')
    

# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = list(map(int, input().split()))

    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # print(starts)
    # print(ends)
    # print(points)

    # print(k)
    #use fast_count_segments
    cnt = fast_count_segments2(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

# a = [0,0,0,1,1,1,2,2,2,3,4,5]
# num = binary_search(a,0,len(a),2)
# print(num+1)
