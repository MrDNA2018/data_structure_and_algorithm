# -*- coding: utf-8 -*-

# 图的定义，邻接表，使用字典的方式，用于演示，比较直观

g = {'A':{'B':1,'C':2},
     'B':{'A':1,'C':3,'D':4},
     'C':{'A':2,'B':3,'D':5,'E':6},
     'D':{'B':4,'C':5,'E':7,'F':8},
     'E':{'C':6,'D':7,'G':9},
     'F':{'D':8},
     'G':{'E':9}
    }   


# 图的遍历，宽度优先，也就是从起点开始，一层一层扫描，需要使用队列数据结构
# 同时图的遍历，不同于树的遍历，树的结构确定了，而图点和点的相连情况无法提前确定
# 搜索时，需要标记已扫描的点，避免重复扫描

def BFS(graph,start_vertex):
    # 初始化队列，把起点放入队列
    queue =[start_vertex,]
    # 我们还需要定义一个数组记录已访问的顶点，一般使用哈希表，每次查找时间复杂度O(1)
    visited = set()
    # 记录遍历的结果
    result = []
    
    while queue:
        # 弹出一个顶点
        current_vertex = queue.pop(0)
        # 假如该节点没有访问过，就访问它，并标记已访问
        if current_vertex not in visited:
            result.append(current_vertex)
            visited.add(current_vertex)
            
        # 下面就需要访问这个结点的邻接顶点
            for neighbour_vertex in graph[current_vertex].keys():
                # 把邻接顶点放入队列，放入之前可以判断一下，是否已经访问过
#                if neighbour_vertex not in visited:
                queue.append(neighbour_vertex)
                    
    return result

# 这里面判断结点是否访问过，在弹出的时候判断，可以改进一下，也就是在入队的时候
# 就标记成已访问的顶点，也就是重复的结点不会入栈
def BFS2(graph,start_vertex):
    queue = [start_vertex,]
    # 入栈就标记已访问
    visited = set()
    visited.add(start_vertex)
    # 用于记录访问的结点顺序
    result =[]
    
    while queue:
        current_vertex = queue.pop(0)
        result.append(current_vertex)
        for neighbour_vertex in graph[current_vertex].keys():
            if neighbour_vertex not in visited:
                queue.append(neighbour_vertex)
                visited.add(neighbour_vertex)
    return result


# 这里面也需要注意标记的用法，我们在什么时候标记顶点已经被访问了
# 第一次访问顶点的时候，还是打印结点结束也就是最后一次访问结点的时候
# 一般情况下我们习惯在在一个结点确定访问完毕也就是最后访问结点的时候，标记结点已访问
# 实际操作的效率高的是，在我们第一次碰见顶点的时候就标记结点，因为第一次碰见他就代表
# 处理他已经开始了
# BFS在入队列的时候，标记已访问，这样重复的结点就不会入队列
# DFS在进入递归前，标记顶点已访问，这样重复结点就不会进入递归
# DFS的递归，把原问题看成：当前顶点+ 所有相邻顶点为起点子图的子问题
# 为什么不是当前顶点+ 一个相邻顶点为起点子图的子问题？想一下你要处理的是当前顶点+
# 剩余n-1个顶点构成的子图，这个子图可能是好几个分离的图。
def DFS(graph,start_vertex):    
    def DFSRecursion(graph,start_vertex,visited):        
        result.append(start_vertex) 
        # 遍历访问子图集，访问前先判断是否已访问，未访问标记已访问，然后进入子图处理
        for neighbour_vertex in graph[start_vertex].keys():
            if neighbour_vertex not in visited:
                visited.add(neighbour_vertex)
                DFSRecursion(graph,neighbour_vertex,visited)
    result =[]           
    visited = set()
    # 在进入递归前，把顶点标记为已访问
    visited.add(start_vertex)        
    DFSRecursion(graph,start_vertex,visited)
    return result
    
# 深度优先遍历，明显需要用到栈的数据结构
# 一个图的处理，分为两个大部分，当前顶点处理 + 所有子图的处理，
# 所以这个问题的结构是n叉树，
# 可以参考，回溯法处理（基于深度优先的回溯法，在那里使用迭代的方法比较少），
# 或者参考二叉树的处理，先序遍历，先访问顶点，再左子树，后访问右子树，逆序放入栈中
# 那么对应图的先序遍历，先访问顶点，在访问各个子图，只要把他们逆序放入栈中就行了
# 同理放入栈中前，先标记顶点已访问         
def DFS2(graph,start_vertex):
    
    visited = set()
    # 在入栈之前需要先看是否已标记，未标记标记之后放入栈中
    visited.add(start_vertex)
    stack =[start_vertex,]
    result = []
    
    while stack:
        current_vertex = stack.pop()
        # 处理当前结点
        result.append(current_vertex)
        
        # 处理子图子问题
        for neighbour_vertex in graph[current_vertex].keys(): 
            # 子问题入栈前需要判断是否已标记，未标记标记之后放入栈中
            if neighbour_vertex not in visited:
                visited.add(neighbour_vertex)
                stack.append(neighbour_vertex)
    
    return result
  

print(BFS(g,'A'))
print(BFS2(g,'A'))
print(DFS(g,'A'))
print(DFS2(g,'A'))
                    
                
            
        
        
        
    