# -*- coding: utf-8 -*-

class BinTNode:
    def __init__(self,data=None,left =None,right =None):
        self.data =data
        self.left =left
        self.right =right
        
        
        
def buildTree(arr,pointer,N):
    # 递归出口，当越界时就没有必要创建节点了直接return，开始回退
    # 当值为-1时，也没有必要创建结点
    if pointer > N or arr[pointer] == -1:
        return None

    curNode = BinTNode(arr[pointer])

    curNode.left = buildTree(arr,2*pointer+1,N)
    curNode.right = buildTree(arr,2*pointer+2,N)
            
    return curNode


def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
        
def searchInBinaryTree(root,node_key):
    if not root:
        return False
    if root.data == node_key:
        return True
    elif root.data < node_key:
        return searchInBinaryTree(root.right,node_key)    
    else:
        return searchInBinaryTree(root.left,node_key)



class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode data
        :type q: TreeNode data
        :rtype: TreeNode
        """
#        if not root or root.data == p or root.data == q:
#            return root
        
        if root.data < p and root.data < q:
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif root.data > p and root.data > q:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # 实际上这个包含多种请款：
        # not root or root.data == p or root.data == q 和 root.data在p,q之间
        else:
            return root        
    
    
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
        
            
            
        
        
arr = [6,2,8,0,4,7,9,-1,-1,3,5]
root = buildTree(arr,0,len(arr)-1)
inorder(root)
print(searchInBinaryTree(root,9))
t = Solution().lowestCommonAncestorRecursion(root,3,5)
print(t.data if t else t)


#%%
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        x = m -1
        y = n -1
        z = m + n -1
        
        while x >=0 and y >=0:
            
            if nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -=1
                z -=1
            else:
                nums1[z] = nums2[y]
                y -=1
                z -=1
                
        nums1[:y+1] = nums2[:y+1]

nums1 =[1,2,3,0,0,0]
m=3
nums2 =[2,5,6]
n= 3
Solution().merge(nums1,m,nums2,n)  
print(nums1) 


#%%
# 注意python复制数组注意使用切片
# 基于回溯法考虑
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[]
        num = len(nums)
        
        def backtracking(depth,nums):
            if depth == num-1:
                result.append(nums[:])
            
            else:
                for i in range(depth,num):
                    nums[i],nums[depth] = nums[depth],nums[i]
                    backtracking(depth+1,nums)
                    nums[i],nums[depth] = nums[depth],nums[i]
                    
            return result
                    
                    
        return backtracking(0,nums)
 
# 基于动态规划，状态方程考虑,f[n] = 首位为所有元素 + f[n-1]，这个动态规划没有重复
# 子问题，每一种情况都需要遍历
class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[]
        end = len(nums)
        def permute_recursion(nums,start):
            # 递归的出口，就是只剩一个元素时
            if start == end-1:
                result.append(nums[:])
            
            # 把每一个元素放在首位，其他的做全排列
            for i in range(start,end):
                nums[i],nums[start] = nums[start],nums[i]
                permute_recursion(nums,start+1)
                nums[i],nums[start] = nums[start],nums[i]
                
            return result
        
        return permute_recursion(nums,0)


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_result = nums[0]
        num = len(nums)
        b = [0] *(num +1)
        
        for i in range(1,num+1):
            if b[i-1] > 0:
                b[i] = b[i-1] + nums[i-1]
            else:
                b[i] = nums[i-1]
                
            if b[i] > max_result:
                max_result = b[i]
                
        return max_result
    
    
lst = [1,2,3]
Solution().permute(lst)
Solution2().permute(lst)
