def abc():
    s='([])'
    if len(s) % 2 == 1:#这一步真的机智，我只会想到输入一个的状况。。。
        return False
    d = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for i in s:
        # in stack
        if i in d:
            print(i)
            stack.append(i)
        else:
            if stack==[] or d[stack.pop()] != i:
                return False
    return stack == []
abc()