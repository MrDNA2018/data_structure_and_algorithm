# -*- coding: utf-8 -*-

# 注意递归的返回值，递归的要返回的话，要前后一致，或者直接基于某一层考虑，把递归看成结果
def binary_Serach_recursive(arr,left,right,target):
        
    middle = (left + right) // 2
    # 递归出口
    if left > right :
        return(-1)
    
    if arr[middle] == target:
        return(middle)
            
    elif arr[middle] < target:
        # 这里没有return的话，结果就没法return出来
        return binary_Serach_recursive(arr,middle+1,right,target)
        
    else:
        return binary_Serach_recursive(arr,left,middle-1,target)

# 递归转换为迭代实现：可以看出上述的递归就是，left,right对应一个子问题，left,right两个指针相互逼近的过程
# 迭代实现时，也不断逼近两个指针，即可迭代实现递归
def binary_Serach_iterative(arr,target):
    left = 0
    right = len(arr)-1
    
    # 循环体条件
    while left <= right:
        
        middle = (left + right) // 2
        
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle +1
        else:
            right = middle -1
            
    return -1


def lowestCommonAncestor(self, root, p, q):
    
    if root.data < p and root.data < q:
        return self.lowestCommonAncestor(root.right, p, q)
    
    elif root.data > p and root.data > q:
        return self.lowestCommonAncestor(root.left, p, q)

    else:
        return root        

# 树形结构，是使用一个指针就可以描述一个子问题，指针对应的是子问题的选择，迭代时更新
# 树形指针就行了，出口就是找到了祖先，或者树形指针指向None
        
# 这里是树形指针的一种用方法，是把递归转化为迭代的一种常用方法
def lowestCommonAncestorRecursion(self, root, p, q):
    
    pointer = root
    while pointer:
        if pointer.data < p and pointer.data < q:
            pointer = pointer.right
    
        elif pointer.data > p and pointer.data > q:
            pointer = pointer.left        
        else:
            return pointer 