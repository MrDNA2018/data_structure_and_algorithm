import numpy as np
import heapq
class Node:
    def __init__(self,curCost=None,depth=None,rcost = None,path = None,lbound =None):
        self.lbound = lbound
        self.curCost = curCost
        self.depth = depth
        self.path = path
        self.rcost = rcost
    
    def __lt__(self,other):

              return int(self.lbound) <int(other.lbound)

class prune_Traveling_saleman:
    def __init__(self,graph,start=0):
        self.num = len(graph)
        self.graph =  graph
        self.start = start
        
        self.bestNode = Node(np.inf,-1,-1,None,-1)
        
        self.minOut = [np.inf]*self.num
        self.minSum =0
        for i in range(self.num):
            for j in range(self.num):
                if i !=j and graph[i][j] < self.minOut[i]:
                    self.minOut[i] = graph[i][j]
            self.minSum += self.minOut[i]
            

    
       
    def traveling_Saleman(self):
        pqueue =[]
                 
        # 第1层，就是起点，也可以认为是第一层，这里为了处理数据方便成为第1层
        curNode = Node(0,0,self.minSum,[i for i in range(self.num)],self.minSum)
        pqueue = [curNode,]
        curNode = heapq.heappop(pqueue)
        curCost = curNode.curCost
        depth = curNode.depth
        rcost = curNode.rcost
        path = curNode.path

        
        while depth <= self.num-1:
            

                    
            if depth == self.num-1:

                lbound = curCost + self.graph[path[depth]][path[0]]
                if lbound < self.bestNode.curCost:
                    self.bestNode.curCost = lbound
                    self.bestNode.path = path
                  
                    node = Node(lbound,depth+1,lbound,path,lbound)
                    heapq.heappush(pqueue,node)
                    
            else:   
                temp_rcost = rcost - self.minOut[path[depth]]
                for i  in range(depth+1,self.num):
                    temp_cur = curCost + self.graph[path[depth]][path[i]]
                    lbound =  temp_cur + temp_rcost
                    if lbound < self.bestNode.curCost:#  should fix
                        temp_path = path[:]
                        temp_path[depth+1],temp_path[i] = temp_path[i],temp_path[depth+1]
                        node = Node(temp_cur,depth+1,temp_rcost,temp_path,lbound)
                        heapq.heappush(pqueue,node)
            
            curNode = heapq.heappop(pqueue)
            curCost = curNode.curCost
            depth = curNode.depth
            rcost = curNode.rcost
            path = curNode.path
                
    def print_Result(self):
        self.traveling_Saleman()
        print(self.bestNode.curCost)
        print(self.bestNode.path)
            

g =[[0,5,9,4],
    [5,0,13,2],
    [9,13,0,7],
    [4,2,7,0]]

#backtracking_Traveling_saleman(g,0).print_Result()
prune_Traveling_saleman(g,0).print_Result()

#%%
# 分支限界法求解旅行商问题
import math
from heapq import *
 
n=4
x = [1, 2, 3, 4]
# 定义图的字典形式
#G = {
#    '1': {'2': 30, '3': 6, '4': 4},
#    '2': {'1': 30, '3': 5, '4': 10},
#    '3': {'1': 6, '2': 5, '4': 20},
#    '4': {'1': 4, '2': 10, '3': 20}
#}

G = {
    '1': {'2': 5, '3': 9, '4': 4},
    '2': {'1': 5, '3': 13, '4': 2},
    '3': {'1': 9, '2': 13, '4': 7},
    '4': {'1': 4, '2': 2, '3': 7}
}

# 定义图的数组形式
graph = [
        [0,5,9,4],
        [5,0,13,2],
        [9,13,0,7],
        [4,2,7,0]
        ]
#graph = [
#    [0, 30, 6, 4],
#    [30, 0, 5, 10],
#    [6, 5, 0 , 20],
#    [4, 10, 20, 0]
#]
bestway = ''
# bestcost = 1<<32 # 这里只要是一个很大数就行了 无穷其实也可以
bestcost = math.inf # 好吧 干脆就无穷好了
nowcost = 0    # 全局变量，现在的花费
 
# 设置节点类
class Node:
    # 构造函数，现在的花费，到目前的路径
    def __init__(self, w=math.inf, route=[], cost=0):
        self.weight = w
        self.route = route
        self.cost = cost
        
    # 重载比较，用于堆的排序
    def __lt__(self,other):
        return int(self.weight) < int(other.weight)
    
    # 打印
    def __str__(self):
        return "节点的权重为"+str(self.weight)+" 节点的路径为"+str(self.route)+" 花费为"+str(self.cost)
        
 
def BBTSP(graph, n, s):
    global bestcost, bestroute
    heap = []
    
    start = Node(route=[str(s)])
    
    heap.append(start)
    
    # 当堆中有数的时候，循环继续
    while heap:
        nownode = heappop(heap)    # 取出权重最大的那个数
        # 生成权重最大的那个数的下结点，并且把下结点加入堆中
        for e in [r for r in graph if r not in nownode.route]:
            node = Node(w=graph[nownode.route[-1]][e], route=nownode.route+[e], cost=nownode.cost+graph[nownode.route[-1]][e])
            # 如果现在的值大于最优值，剪枝操作
            if node.cost >= bestcost:
                continue
            # 如果到了最后一个点，加上回去的路，并计算最小值
            if len(node.route)==4:
                wholecost = graph[node.route[-1]][s]+node.cost
                if wholecost < bestcost:
                    bestcost = wholecost
                    bestroute = node.route
                    print("最佳花费为:"+str(bestcost))
                    print("最佳路径为:"+str(bestroute))
                    
            heap.append(node)
 
        
    return bestcost
        
    
BBTSP(G, n, '1')
