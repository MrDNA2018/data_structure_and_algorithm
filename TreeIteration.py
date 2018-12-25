# -*- coding: utf-8 -*-
# 首先需要定义结点
class BinTNode:
    def __init__(self,data=None,left =None,right =None):
        self.data =data
        self.left =left
        self.right =right
        
        
# 迭代的方式处理树，就必须清楚你将要访问的顺序，对应的就是指针怎么走，你必须很清楚
        
# 树的宽度优先搜索，他是一层一层的访问，就搞不清楚怎么划分子问题了，但是你访问的顺序
# 你很清楚，那么就使用迭代的方式实现，你的指针应该可以按照一层一层的走
# 怎么走？在线性结构里，我们处理的是数组，可以直接一个一个的走
# 在树里，按照层次访问，每一层结点之间是跳跃的，那我们该怎么实现指针的连续走动？
# 很容易的思路，把每一层的结点放在一个数组里，然后指针就可以连续走动了
# 把每一层的结点放在一个数组里，也需要注意放入和取出顺序，我们需要实现每一层从左到
# 右的层次访问，先左后右放入数组的话，取出的时候，也必须是先左后右取出
# 很明显我们需要先进先出的数据结构，FIFO

# 从这个代码结构可以看出和分支限界法队列实现方式很像，
# 分支限界就是把解定义成树，在树里搜索结果
def levelorder(root):
    # 初始化，把根结点放入队列
    queue = [root,]   
    # 当队列为空时代表，所有结点都遍历了
    while queue:
        # 弹出先放出的元素
        node = queue.pop(0)
        # 弹出的过程也是处理数据的过程
        print(node.data,end=' ')
        # 叶子结点不需要把左右的None添加到队列
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# 实现迭代方式的先根遍历，不管怎么遍历，首先你必须知道你是如何扫描的，然后再考虑如何遍历
# 所有的遍历扫描方式都是，一直往左走，到底回溯，往右走一步，一直往左走，到底回溯，往右走一步。。。
# 在这种扫描方式下，如何实现：回溯，往右走一步？就是提前把往右走的步骤放在一个数组里，回溯的时候
# 直接从数组取出要回溯到哪里，首先我们知道要回溯的结点都是右结点，那我们按照顺序扫描的过程中，
# 把右结点都放入一个数组，我们到底之后，回溯的是最近的右结点，很明显这个是LILO，后进先出
# 这个明显是栈，所以我们需要借助于栈实现。
            
# 还有一种思路，直接针对递归的实现方式，想办法通过栈来实现递归，得到的还是和上面一样
# 
def preorder(root):
    pointer = root
    stack =[]
    
    while pointer:
        # 这个叫做下行循环，一直向左走，直到走到空树
        while pointer:
            print(pointer.data,end=' ')
            if pointer.right:
                stack.append(pointer.right)
            pointer = pointer.left 
        if stack:
            # 遇到空树了，也就是走到底了，回溯
            pointer = stack.pop()
            
# 这里看见2个while,看起来应该可以简化，一个while的话下行循环就需要和下行循环一起
# 什么时候弹出了，当前指针为空时弹出，出口了就是没有元素弹出时为出口
def preorder2(root):
    pointer = root
    stack =[]
    
    while pointer:
        # 这个叫做下行循环，一直向左走，直到走到空树
        print(pointer.data,end=' ')
        
        if pointer.right:
            stack.append(pointer.right)
            
        pointer = pointer.left
        
        if not pointer and stack:
            pointer = stack.pop()

# 还有一种方案，就是把之前所说的模拟递归的操作，这里是把左结点和右结点均放入stack
# 这个思路计较简单，放入时先右后左，弹出时一直都是左
def preorder3(root):
    stack =[root,]
    
    while stack:
        pointer = stack.pop()
        print(pointer.data,end=' ')
        if pointer.right:
            stack.append(pointer.right)
        if pointer.left:
            stack.append(pointer.left)
# 后根还有一种实现方式，后根是左右中，先根处理时：右左中的到结果倒叙输出就是后根处理结果            
def postorderBypreorder(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    stack, output = [root, ], []
    while stack:
        root = stack.pop()
        output.append(root.item)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
    return output[::-1]

# 这里迭代分为2个部分，一是一直往左走，走到空树，弹出结点
# 弹出结点时，一直弹出，直到弹出的结点的右子树存在，对右子树做相同的操作
def inorder(root):
    stack =[root,]
    pointer = root
    
    while stack:
        
        # 下行循环走到底，并把结点都存入进来
        while pointer:
            if pointer.left:
                stack.append(pointer.left)
            pointer = pointer.left
                         
       # 一直往上打印结点，直到当前结点的右子树存在 
        while stack:
            pointer = stack.pop()
            print(pointer.data,end=' ')
            if pointer.right:
                pointer = pointer.right        
                stack.append(pointer)
                break
            
            
def inorder3(root):
    stack =[]
    pointer = root
    
    while True:
        
        # 下行循环走到底，并把结点都存入进来
        while pointer:
            stack.append(pointer)
            pointer = pointer.left
            

                         
       # 一直往上打印结点，直到当前结点的右子树存在 
        while stack:
            pointer = stack.pop()
            print(pointer.data,end=' ')
            
            if pointer.right:
                pointer = pointer.right        
                break
            # 思考一下退出为什么要放在这里，没有右结点需要加入而且栈已空的情况下循环退出
            if not stack:
                return
            

            
def inorder2(root):
    stack =[]
    pointer = root
    
    while stack or pointer:
        
        # 下行循环走到底，并把结点都存入进来
        while pointer:
            stack.append(pointer)
            pointer = pointer.left
        
                         
       # 一直往上打印结点，直到当前结点的右子树存在 ,代码可以简化如下
       # 右边为空时也是会一直弹出元素
        pointer = stack.pop()
        print(pointer.data,end=' ')
        pointer = pointer.right

def postorder(root):
    stack =[root,]
    pointer = root
    
    while stack:
        
        # 下行循环走到底，并把结点都存入进来,加入左结点为空，右结点非空，就往右走
        while pointer:
            if pointer.left:
                stack.append(pointer.left)
                pointer = pointer.left
            elif pointer.right:
                stack.append(pointer.right)
                pointer = pointer.right
            else:
                pointer = None
                         
       # 一直往上打印结点，栈顶 的元素的左儿子是当前结点，把栈顶的元素的右儿子
       # 问题的关键是何时放入右结点
        while stack:
            pointer = stack.pop()
            print(pointer.data,end=' ')
            if stack and stack[-1].left == pointer and stack[-1].right:
                pointer = stack[-1].right      
                stack.append(pointer)
                break     
            
def postorder2(root):
    stack =[]
    pointer = root
    
    # 这个循环体设计得很巧妙
    while stack or pointer:
        
        # 下行循环走到底，并把结点都存入进来
        while pointer:
            stack.append(pointer)
            pointer = pointer.left if pointer.left else pointer.right
        
                         
       # 一直往上打印结点，直到当前结点的右子树存在 ,代码可以简化如下
       # 右边为空时也是会一直弹出元素
        pointer = stack.pop()
        print(pointer.data,end=' ')
        if stack and stack[-1].left == pointer:
            pointer = stack[-1].right
        # 当stack[-1].left ！= pointer时，即右子树遍历完毕，我们现在需要遍历stack[-1]
        # 直接设置pointer = None就可以直接遍历了，这里是一个点
        else:
            pointer = None

            
        
           
root = BinTNode(1,BinTNode(2,BinTNode(4),BinTNode(5)),BinTNode(3,BinTNode(6),BinTNode(7)))
print('levelorder:',end='')
levelorder(root)
print(end='\n')
print('preorder:',end='')
preorder(root)
print(end='\n')
print('preorder2:',end='')
preorder2(root)
print(end='\n')
print('preorder3:',end='')
preorder3(root)
print(end='\n')
print('inorder:',end='')
inorder(root)
print(end='\n')
print('inorder2:',end='')
inorder2(root)
print(end='\n')
print('inorder3:',end='')
inorder3(root)
print(end='\n')
print('postorder:',end='')
postorder(root)
print(end='\n')
print('postorder2:',end='')
postorder2(root)
print(end='\n')