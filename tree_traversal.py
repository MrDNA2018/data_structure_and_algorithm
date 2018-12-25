# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import tree
#%%
class Solution1(object):
    def postorderTraversal(self, root):
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
        print output      
        return output[::-1]
    
    def preorderTraversal(self, root):
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
            if root.right is not None:
                stack.append(root.right)

            if root.left is not None:
                stack.append(root.left) 
        return output
#%%
class guide(object):
    def __init__(self, opt,node):
        self.opt = opt
        self.node = node
         
class Solution2(object):
 
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        ans = []
        path = [guide(0,root),]
        while path:
            current = path.pop()
            if not current.node:
                continue
            if current.opt == 1:
                ans += [current.node.item]
            else:
                path += [guide(0,current.node.right)]
                path += [guide(0,current.node.left)]
                path += [guide(1,current.node)]
                            
        return ans

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        ans = []
        path = [guide(0,root),]
        while path:
            current = path.pop()
            if not current.node:
                continue
            if current.opt == 1:
                ans += [current.node.item]
            else:
                path += [guide(0,current.node.right)]
                path += [guide(1,current.node)]
                path += [guide(0,current.node.left)]
                            
        return ans
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        ans = []
        path = [guide(0,root),]
        while path:
            current = path.pop()
            if not current.node:
                continue
            if current.opt == 1:
                ans += [current.node.item]
            else:
                path += [guide(1,current.node)]
                path += [guide(0,current.node.right)]
                path += [guide(0,current.node.left)]
                            
        return ans

#%%
class Solution3(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        t = root
        while t is not None or s:
            while t is not None:
                s.append(t)
                t = t.left if t.left is not None else t.right
            
            t = s.pop()
            ans += [t.item]
#            print ans
         
            if s and s[-1].left == t:
                t = s[-1].right
            else:
                t = None
                
        return ans
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        t = root
        while t is not None or s:
            while t is not None:
                ans += [t.item]
                s.append(t.right)
                t = t.left            
            t = s.pop()                        
        return ans
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        t = root
        while t is not None or s:
            while t is not None:
                s.append(t)
                t = t.left
            
            t = s.pop()
            ans += [t.item]
            t = t.right                
        return ans
#%%               
if __name__ =="__main__":
    tree =tree.Node()
    tree._add(0)
    tree._add(1)
    tree._add(2)
    tree._add(3)
    tree._add(4)
    tree._add(5)
    tree._add(6)
    tree._add(7)
    tree._add(8)
    tree._add(9)
    tree._add(10)
#%%  
#    ans1 = Solution1().postorderTraversal(tree)
#    print ans1
#%%
    ans = Solution2().preorderTraversal(tree)
    print ans

    ans = Solution2().inorderTraversal(tree)
    print ans

    ans = Solution2().postorderTraversal(tree)
    print ans    
    
#%%
    ans = Solution3().preorderTraversal(tree)
    print ans

    ans = Solution3().inorderTraversal(tree)
    print ans

    ans = Solution3().postorderTraversal(tree)
    print ans  