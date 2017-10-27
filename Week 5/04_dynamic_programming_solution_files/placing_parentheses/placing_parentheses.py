# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def MaxandMin (i,j):
    for k in range(i,j):
        a = evalt(MaxandMin(i,k),MaxandMin(k+1,j),op[k])
        
def get_maximum_value(dataset):
    #write your code here
    num = list(map(int,dataset[::2]))
    op = list(dataset[1::2])

    return num,op



if __name__ == "__main__":
    print(get_maximum_value(input()))
