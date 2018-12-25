# -*- coding: utf-8 -*-

# 用于右括号和左括号匹配
def left(a):
    if a == '}':
        return '{'
    if a == ']':
        return '['
    if a == ')':
        return '('
# 验证括号    
def checkNotation(arr):
    num = len(arr)
    # 特殊case处理
    if num == 0:
        return False
    # 用于存放左括号
    stack =[]
    # 遍历所有的元素
    for pos in range(num):
        # 遇到左括号，就直接放入栈里
        if arr[pos] =='{' or arr[pos] =='[' or arr[pos] =='(':
            stack.append(arr[pos])
        # 遇到右括号，考虑是否匹配    
        else :
            # 把栈顶的元素和当前的是否匹配，匹配的话，弹出栈顶元素，消除
            # 判断stack是否为空为特殊case处理
            if stack and stack[-1] == left(arr[pos]):
                stack.pop()
            else:
                return False
    # 特殊case处理
#    if stack: 
#        return False
#    else:
#        return True
    # 上述4行可以简化成如下
    return not stack
                
specialCase = []
print(checkNotation(specialCase))
tureCase = ['{','[',']','(',')','}']
flaseCase = ['{','[',']','(',']','}']
print(checkNotation(tureCase))
print(checkNotation(flaseCase))
    
    
    
    
