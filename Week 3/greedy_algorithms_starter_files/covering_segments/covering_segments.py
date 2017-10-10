# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def getend(tuple):
    return tuple.end

def optimal_points(segments):
    points = []
    key = -1
    #write your code here
    segments = sorted(segments,key=getend)
    # return segments
    for s in segments:
    #     points.append(s.start)
        if s.start > key:
            key = s.end
            points.append(key)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # n, *data = map(int, input().split())

    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # print(data)
    # print(segments)
    # print(optimal_points(segments))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
