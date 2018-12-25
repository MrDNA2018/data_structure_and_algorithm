# -*- coding: utf-8 -*-

class BinTNode:
    def __init__(self,data=None,left =None,right =None):
        self.data =data
        self.left =left
        self.right =right

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

def buildTree1(arr,pointer,N):
    
    if pointer <=N:
        
        if arr[pointer] == -1:
            curNode = None
        else:
            curNode = BinTNode(arr[pointer])
        
        if 2*pointer+1<=N:
            curNode.left = buildTree(arr,2*pointer+1,N)
        if 2*pointer+2<=N:
            curNode.right = buildTree(arr,2*pointer+2,N)
            
        return curNode

# 如下是简化的版本，我们一般在循环里尽量少用判断语句    
def buildTree(arr,pointer,N):
    # 递归出口，当越界时就没有必要创建节点了直接return，开始回退
    # 当值为-1时，也没有必要创建结点
    if pointer > N or arr[pointer] == -1:
        return None

    curNode = BinTNode(arr[pointer])

    curNode.left = buildTree(arr,2*pointer+1,N)
    curNode.right = buildTree(arr,2*pointer+2,N)
            
    return curNode

# 寻找两个孩子的共同祖先：我们定义问题为找共同祖先，当一颗子树只含有child1时，
# 那么这颗子树的祖先就是child1，一颗子树只含有child2时，那么这颗子树的祖先就是child2，
# 当一颗子树同时含有child1和child2时，那么他的祖先就是child1和child2的共同祖先，然后
# 把问题缩小到一颗子树
def findAncestor(root,child1,child2):
    if not root:
        return -1
  
    # 把原问题分成三个部分，左子树，当前结点，右子树
    if root.data == child1 or root.data ==child2:
        # 不管下面还有没有要找的child,整颗树的祖先都是root
        return root.data
    
    # 如果root不是任何一个的祖先，就需要处理下面的2颗子树
    left_ancestor = findAncestor(root.left,child1,child2)
    right_ancestor = findAncestor(root.right,child1,child2)
    
    # 然后基于两颗子树得到的结果处理,分为六种情况:
    # 左0右0，-1，                  left_ancestor + right_ancestor + 1
    # 左1右1，root.data,            root.data
    # 左1右0，left_ancestor         left_ancestor + right_ancestor + 1
    # 左0右1，right_ancestor        left_ancestor + right_ancestor + 1
    # 左2右0，left_ancestor         left_ancestor + right_ancestor + 1
    # 左0右2，right_ancestor        left_ancestor + right_ancestor + 1
    if left_ancestor !=-1 and right_ancestor !=-1:
        return root.data
    # 这个简化处理非常巧妙，一般写循环尽量少用判断，可以巧妙利用返回值-1构造通用结果
    # 看这个处理直接把其他的5种结果都处理成left_ancestor + right_ancestor + 1
    # 利用返回的结果为-1，+1之后可以消除可能出现的那个结果
    return left_ancestor + right_ancestor + 1
    
# 这种方案存在问题，当一颗子树只含有child1时，
# 那么这颗子树的祖先就是child1，一颗子树只含有child2时，那么这颗子树的祖先就是child2，
# 但是最终方案是求共同祖先，如果输入一个孩子不存在，那返回结果不久变成了两外一个孩子

def findAncestor2(root,child1,child2):

    # 把原问题分成三个部分，左子树，当前结点，右子树
    if (not root) or root.data == child1 or root.data ==child2:
        # 不管下面还有没有要找的child,整颗树的祖先都是root        
        return root
    
    # 如果root不是任何一个的祖先，就需要处理下面的2颗子树
#    left_ancestor =None
#    right_ancestor =None
    left_ancestor = findAncestor2(root.left,child1,child2)
    right_ancestor = findAncestor2(root.right,child1,child2)
    
    # 然后基于两颗子树得到的结果处理,分为六种情况:
    # 左0右0，none，                [left_ancestor , right_ancestor]
    # 左1右1，root,                 root
    # 左1右0，left_ancestor         [left_ancestor , right_ancestor]
    # 左0右1，right_ancestor        [left_ancestor , right_ancestor ]
    # 左2右0，left_ancestor         [left_ancestor , right_ancestor]
    # 左0右2，right_ancestor        [left_ancestor , right_ancestor]
    if left_ancestor and right_ancestor:
        return root
    # 这个简化处理非常巧妙，一般写循环尽量少用判断，可以巧妙利用返回值-1构造通用结果
    # 看这个处理直接把其他的5种结果都处理成left_ancestor + right_ancestor + 1
    # 利用返回的结果为-1，+1之后可以消除可能出现的那个结果
    return (left_ancestor,right_ancestor)[not left_ancestor]

# leetcode 236
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (not root) or root.data == p or root.data ==q:   
            return root

        left_ancestor = self.lowestCommonAncestor(root.left,p,q)
        right_ancestor = self.lowestCommonAncestor(root.right,p,q)
    
        if left_ancestor and right_ancestor:
            return root

        return left_ancestor if left_ancestor else right_ancestor     
        
arr =[1,2,3,4,5,6,7,-1,-1,8,9,-1,-1,10,11]
root = buildTree(arr,0,len(arr)-1)
print(findAncestor(root,9,5))
print(findAncestor2(root,9,5).data)
print(Solution().lowestCommonAncestor(root,9,5).data)
