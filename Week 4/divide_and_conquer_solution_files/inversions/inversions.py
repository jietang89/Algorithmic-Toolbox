# Uses python3
import sys



def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here

    # leftside = a[left:ave]
    # rightside = a[ave:right]
    i = left
    j = ave
    k = 0

    while i < ave and j < right:
        if a[i] > a[j]:
            b[k] = a[j]
            j += 1
            k += 1
            number_of_inversions += (ave - i)
        else:
            b[k] = a[i]
            i += 1
            k += 1

    while i < ave:
        b[k] = a[i]
        i += 1
        k += 1

    while j < right:
        b[k] = a[j]
        j += 1
        k += 1

    a[left:right] = b[:k]

    # print(a , number_of_inversions)
    # print(left,ave,right)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, *a = list(map(int, input().split()))

    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
