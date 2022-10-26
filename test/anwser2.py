src = input().strip()
expr = ''
stack = []
def sharp(stack=stack):
    y = stack.pop()
    _sharp = stack.pop()
    x = stack.pop()
    return '4*' + x +  + '3*' + y + '+ 2'
for index, i in enumerate(src):
    if i.isdigit():
        stack.append(i)
    elif i == '#':
        stack.append(i)
        stack.append(src[i + 1])
        index += 1
        expr += sharp()
    elif i == '$':
