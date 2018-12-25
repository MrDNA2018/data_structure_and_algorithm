# -*- coding: utf-8 -*-

# 构造一棵树
# 首先需要定义结点
class BinTNode:
    def __init__(self,data=None,left =None,right =None):
        self.data =data
        self.left =left
        self.right =right
# =============================================================================
# 结合这几个例子，体会一下树形结构
# 树本来就是一个天然的递归结构，每一个递归都对应着一个递归树
# 就二叉树而言，每一个二叉树对应着一个左子树，一个右子树
# 都不用我们思考怎么划分子问题，现在两个子问题就已经划分好了
# 那么每一棵树对应三部分：当前结点，左子树，右子树
# 那么我们处理原问题，只需要对应处理这三部分就可以了        
# 递归实现的出口是什么，出口就是叶子结点的左右子树，也就是空树，出口就是空树return
# =============================================================================

# 我们统计树的结点，当前结点1个+左子树的结点和+右子树的结点和
def count_TreeNodes(root):
    if not root:
        return 0
    else:
        return 1 + count_TreeNodes(root.left) + count_TreeNodes(root.right)
  
# 我们统计树的权值和，当前结点权值+左子树的权值和+右子树的权值和    
def sum_TreeValues(root):
    if not root:
        return 0
    else:
        return root.data + sum_TreeValues(root.left) + sum_TreeValues(root.right)    
# 同样的道理，获取树的高度   
def height_Tree(root):
    if not root:
        return 0
    else:
        return 1 + max(height_Tree(root.left),height_Tree(root.right))
    
# 我们讨论树的遍历，对于一棵树：
# 先根遍历：遍历当前结点-->遍历左子树-->遍历右子树
# 中根遍历：遍历左子树-->遍历当前结点-->遍历右子树
# 后跟遍历：遍历左子树-->遍历右子树-->遍历当前结点
# 这是从整个问题来考虑
# 还有一个思考为什么这3种遍历成了深度优先搜索了？
# 只要是递归必然是深度优先，因为只要是递归就必须一直探到底部，然后逐步返回
# 整个看起来，先处理左边，再处理右边，很像宽度优先是吧，其实所有的递归都是深度优先
# 处理时应该从整体分解子问题的角度来分析
def preorder(root):
    if not root:
        return
    else:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)
        
def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
        
def postorder(root):
    if not root:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')

    
root = BinTNode(1,BinTNode(2,BinTNode(4),BinTNode(5)),BinTNode(3,BinTNode(6),BinTNode(7)))
print(count_TreeNodes(root))
print(sum_TreeValues(root))
print('preorder:',end='')
preorder(root)
print(end='\n')
print('inorder:',end='')
inorder(root)
print(end='\n')
print('postorder:',end='')
postorder(root)
print(end='\n')
print('Height:',end='')
print(height_Tree(root))
print(end='\n')
