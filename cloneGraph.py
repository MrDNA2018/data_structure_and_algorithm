# -*- coding: utf-8 -*-

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# 克隆图是图的遍历的应用，就是我们在遍历图时需要进行一些操作
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        # visited是一个字典：node.label:新复制的结点，node.label可以定位原来的结点
        visited = {}
        root = UndirectedGraphNode(node.label)
        visited[node.label] = root
        
        # 实际上是图的遍历，所以指针是指向原图的
        stack = [node,]
        
        while stack:
            curNode = stack.pop()            
            for neighborNode in curNode.neighbors:
                if neighborNode.label not in visited:
                    # 这个步骤做了2个操作，相当于标记了原图中这个结点已经访问了
                    # 二是复制了这个结点，邻居还有待添加进去
                    visited[neighborNode.label] = UndirectedGraphNode(neighborNode.label)
                    # 标记了结点之后，结点入栈
                    stack.append(neighborNode)
                # 既然新图邻居结点都复制了，那么就可以更新新图的邻居列表了
                visited[curNode.label].neighbors.append(visited[neighborNode.label])
                
        return root
    
class Solution2:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        #visited是一个字典：原图的node:新复制的结点，这样使用更加简洁，速度更快
        visited = {}
        root = UndirectedGraphNode(node.label)
        visited[node] = root       
        stack = [node,]
        
        while stack:
            curNode = stack.pop()            
            for neighborNode in curNode.neighbors:
                if neighborNode not in visited:
                    visited[neighborNode] = UndirectedGraphNode(neighborNode.label)
                    stack.append(neighborNode)
                visited[curNode].neighbors.append(visited[neighborNode])
                
        return root
    
    
    
# =============================================================================
# 下面来总结一下克隆图的思路，首先图形的遍历很清楚了，我们所要做的是：在遍历每一个结点
# 时，复制该结点以及他的邻接结点，但是有一个问题，这时新图的邻接结点还没有新建，就没有
# 办法，更新新图这个结点的邻接结点表，但是我们在遍历原图的时候，会把原图的邻接结点都
# 一个一个的放入到栈中或者队列中，在放入前我们就可以把新图的结点复制了，这样新图结点
# 邻接结点都存在了，就可以直接添加了，这里面需要注意，原图遍历的时候结点入栈时会去重
# 但是新图需要把所有的邻接结点都添加进去，只要确认他的列表里面的结点都创建了，就行了
# 这就是为什么visited[curNode].neighbors.append(visited[neighborNode])在if语句的
# 外面。然后，我们还是没有讲到为什么会想到使用{原结点：新结点}的字典，这是因为对一个结点
# 操作有3个，一是新建结点（未更新邻接表），二是更新自己邻接表，三是被用作更新其他结点的
# 邻接表。我们操作过程一直都是在原图上遍历，也就是指针是指向原图的结点，新图对应的在哪里
# 我们不知道，把原结点和新结点一一对应起来，就相当于一个指针同时指向了原图和新图。
# 类似的可以扩展，可以把任意的遍历看成最简单的数组遍历，就是指针按照一定方式走，假如两个数组
# 可以关联起来，可以使用一个指针同时遍历两个数组，简单化遍历之后，一般的问题都只是添加
# 遍历过程的处理。
# =============================================================================

# 这个的处理，是从图的深度遍历考虑，处理整个图，处理顶点，处理各个子图，处理顶点的过程
# 就是克隆顶点的过程，假如某个相邻的顶点已经克隆了，对应的子树就没必要遍历了。
class Solution3:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self,node):
        if not node:
            return node
        
        # 原问题初始化
        visited ={}
        root = UndirectedGraphNode(node.label)
        visited[node] = root       
        
        def Rec(node,visited):
            # 处理每一个子问题
            for neighborNode in node.neighbors:
                if neighborNode not in visited:
                    visited[neighborNode] = UndirectedGraphNode(neighborNode.label)
                    # 处理子问题
                    Rec(neighborNode,visited)
                visited[node].neighbors.append(visited[neighborNode])
                
        # 处理原问题
        Rec(node,visited)
        return root
        

# 还有一种思路：不是从子图来思考问题，而是从子图延申到子问题，这个问题是克隆子图，
# 克隆子图里面的每一个结点，并返回克隆的始顶点
class Solution4:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self,node):
        if not node:
            return node
        
        # 原问题初始化
        visited ={}       
        
        def cloneGraphRec(node,visited):
            if node in visited:
                return visited[node]
            
            visited[node] = UndirectedGraphNode(node.label)
            # 处理每一个子问题
            for neighborNode in node.neighbors:
                visited[node].neighbors.append(cloneGraphRec(neighborNode,visited))
            
            return visited[node]
                
        # 处理原问题
        return cloneGraphRec(node,visited)
