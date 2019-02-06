x=100.0
def cal(x):
    if x == 0:
        return 0
    elif x < 0:
        return 'error'
    else:
        i = 1
        while True:
            if (i+1)**2 > x >= i**2:
                return i
            i+=1

if __name__ == '__main__':
    print(cal(100))
