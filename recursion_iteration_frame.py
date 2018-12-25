# -*- coding: utf-8 -*-

class BinTNode:
    def __init__(self,data=None,left =None,right =None):
        self.data =data
        self.left =left
        self.right =right
        
        
class guide:
    def __init__(self,operation =None,node =None,level =None):
        self.operation = operation
        self.node =node
        # 针对专门的问题可以专门设计需要的恢复的现场
        self.level =level



def preorder(root):
    # operation = 1 代表处理访问自己，operation = 0访问子树
    stack = []
    result =[]
    
    # 初始化
    # 原始问题：访问自己，访问左子树，访问右子树
    # 入栈顺序：访问右子树，访问左子树，访问自己
    stack.append(guide(0,root))
    
    # 这里把原问题看成一个对象，这个对象有三个部分：左子树，当前结点，右子树，
    # 这个对象可以有两种操作，一是处理当前结点，二是访问子树，访问子树可以看成子问题
    
    while stack:
        
        Current = stack.pop()
                
        if Current.operation == 1:
            result.append(Current.node.data)
        
        # 为1代表访问子树，访问子树就当作子问题处理
        else:
            # 入栈顺序：访问右子树，访问左子树，访问自己
            if Current.node.right:
                stack.append(guide(0,Current.node.right))
            if Current.node.left:
                stack.append(guide(0,Current.node.left))
            if Current.node:
                stack.append(guide(1,Current.node))
            
    return result


def inorder(root):
    # operation = 1 代表处理访问自己，operation = 0访问子树
    stack = []
    result =[]
    
    # 初始化
    # 原始问题：访问自己，访问左子树，访问右子树
    # 入栈顺序：访问右子树，访问左子树，访问自己
    stack.append(guide(0,root))
    
    # 这里把原问题看成一个对象，这个对象有三个部分：左子树，当前结点，右子树，
    # 这个对象可以有两种操作，一是处理当前结点，二是访问子树，访问子树可以看成子问题
    
    while stack:
        
        Current = stack.pop()
                
        if Current.operation == 1:
            result.append(Current.node.data)
        
        # 为1代表访问子树，访问子树就当作子问题处理
        else:
            # 入栈顺序：访问右子树，访问自己，访问左子树
            if Current.node.right:
                stack.append(guide(0,Current.node.right))

            if Current.node:
                stack.append(guide(1,Current.node))
                
            if Current.node.left:
                stack.append(guide(0,Current.node.left))
            
    return result


def postorder(root):
    # operation = 1 代表处理访问自己，operation = 0访问子树
    stack = []
    result =[]
    
    # 初始化
    # 原始问题：访问自己，访问左子树，访问右子树
    # 入栈顺序：访问右子树，访问左子树，访问自己
    stack.append(guide(0,root))
    
    # 这里把原问题看成一个对象，这个对象有三个部分：左子树，当前结点，右子树，
    # 这个对象可以有两种操作，一是处理当前结点，二是访问子树，访问子树可以看成子问题
    
    while stack:
        
        Current = stack.pop()
                
        if Current.operation == 1:
            result.append(Current.node.data)
        
        # 为1代表访问子树，访问子树就当作子问题处理
        else:
            # 入栈顺序：访问自己,访问右子树，访问左子树，
            if Current.node:
                stack.append(guide(1,Current.node))
            if Current.node.right:
                stack.append(guide(0,Current.node.right))
            if Current.node.left:
                stack.append(guide(0,Current.node.left))

            
    return result


def countTree(root):
    stack = []
    result = 0

    # 初始化树，把树看成待访问的一颗子树  
    stack = [guide(0,root),]
    
    while stack:
        
        pointer = stack.pop()
        
        if pointer.operation == 1:
            result +=1
            
        else:
            if pointer.node:
                stack.append(guide(1,pointer.node))
            if pointer.node.right:
                stack.append(guide(0,pointer.node.right))
            if pointer.node.left:
                stack.append(guide(0,pointer.node.left))            
            
    return result

def sumTree(root):
    stack = []
    result = 0

    # 初始化树，把树看成待访问的一颗子树  
    stack = [guide(0,root),]
    
    while stack:
        
        pointer = stack.pop()
        
        if pointer.operation == 1:
            result +=pointer.node.data
            
        else:
            if pointer.node:
                stack.append(guide(1,pointer.node))
            if pointer.node.right:
                stack.append(guide(0,pointer.node.right))
            if pointer.node.left:
                stack.append(guide(0,pointer.node.left))            
            
    return result    

def heightTree(root):
    stack = []
    MAX = 0

    # 初始化树，把树看成待访问的一颗子树  
    stack = [guide(0,root,0)]
    
    while stack:
        
        pointer = stack.pop()
        
        if pointer.operation == 1:
            if not pointer.node.left and not pointer.node.left:
                if pointer.level > MAX:
                    MAX = pointer.level
                
        else:
            if pointer.node:
                stack.append(guide(1,pointer.node,pointer.level))
            if pointer.node.right:
                stack.append(guide(0,pointer.node.right,pointer.level+1))
            if pointer.node.left:
                stack.append(guide(0,pointer.node.left,pointer.level+1))            
            
    return MAX + 1 


root = BinTNode(1,BinTNode(2,BinTNode(4),BinTNode(5)),BinTNode(3,BinTNode(6),BinTNode(7)))

print('preorder:',end='')
print(preorder(root))
print(end='\n')
print('inorder:',end='')
print(inorder(root))
print(end='\n')
print('postorder:',end='')
print(postorder(root))
print(end='\n')          
print('countTree:',end='')
print(countTree(root))
print(end='\n')          
print('sumTree:',end='')
print(sumTree(root))
print(end='\n') 
print('heightTree:',end='')
print(heightTree(root))
print(end='\n')                          
            