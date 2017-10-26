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


def get_maximum_value(dataset):
    #write your code here
    num = list(map(int,dataset[::2]))
    op = list(dataset[1::2])
    return num,op



if __name__ == "__main__":
    print(get_maximum_value(input()))
