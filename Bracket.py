def solution(angles):
    # Type your solution here
    if (len(angles) == 0):
        return ""
    stack =[]
    for c in angles:
        if c == '<':
            stack.append(c)
        elif (len(stack)==0 or stack[-1]=='<'):
            stack.pop(-1)
        else:
            stack.append(c)
    
    ans = angles
    while (len(stack)>0):
        if (stack[-1] == '<'):
            ans+='>'
            stack.pop(-1)
        else:
            ans = '<'+ans
            stack.pop(-1)
    
    return ans