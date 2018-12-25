# -*- coding: utf-8 -*-
import numpy as np

class backtracking_Traveling_saleman:
    # 初始化，明确起点
    def __init__(self,graph,start=0):
        # 顶点的个数
        self.vertex_num = len(graph)
        self.graph = graph
        self.start = start
        # 当前解，当前解为顶点的集合[起点，顶点1，...顶点n-1],初始时，第0个为起点
        # 从第一个到n-1个为排列树
        # 解为[起点，顶点1，...顶点n-1]
        # 解的目标函数为：起点到顶点1距离（depth =1）+顶点1到顶点2的+...+顶点depth-1到depth的距离
        # 顶点n-2到顶点n-1(depth=n-1)距离，最后还要构成环路+顶点n-1到起点的距离，求上述和的最小值。
        self.curSolution = [i for i in range(self.vertex_num)]
        # 用于存最好的解
        self.bestSolution = [-1] *self.vertex_num
        # 当前花费初始距离为0
        self.curCost = 0
        # 界初始为很大，得到一个解之后更新，也可以提前更新
        self.bestCost = np.inf
        
    def backtracking(self,depth):
        # 当到达最后一个顶点，为递归出口
        if depth == self.vertex_num-1:
            # 最后一层时，目前函数应该为：当前的距离和+前一个顶点到最后顶点距离+最后顶点到起点的距离
            temp_cost = self.curCost + self.graph[self.curSolution[depth-1]][self.curSolution[depth]] + self.graph[self.curSolution[depth]][self.curSolution[self.start]]
            # 当前解优于最优解的话，更新最优解，假如求可行解的话，就需要把可行解保存起来
            if temp_cost < self.bestCost:
                self.bestCost = temp_cost
                self.bestSolution[:] = self.curSolution[:]
                
        else:
            # 下面就是排列树的处理，我们需要求除了起点之外的[顶点1，...顶点n-1]n-1个起点的全排列
            #  我们处理的是标号，也就是self.curSolution = [i for i in range(self.vertex_num)]
            # 所以我们全排列都是self.curSolution里面的数
            for i in range(depth,self.vertex_num):
#                self.curSolution[depth],self.curSolution[i] = self.curSolution[i],self.curSolution[depth]

                # 当满足我们定义的界时，才可以进入下一层，也就是走过的长度<最优值的话（注意我们这儿要求的是最小值），我们才继续搜索，否则剪掉
                # 有没有人注意到这里是depth-1到i,而不是depth-1 到 depth?
                # 实际上我们学习到模板应该是，先交换，然后满足constraint() && bound() 回溯，最后再交换
                # 编码时先交换的话，这个地方就应该写成depth-1 到 depth，还没交换的话就是depth-1到i
                # 这里是做了优化处理，不满足条件的话，交换都没有必要执行
                if self.curCost + self.graph[self.curSolution[depth-1]][self.curSolution[i]] < self.bestCost:
                    # 全排列，把 当前 和第一位交换，除第一位以外剩下的的进行全排列
                    self.curSolution[depth],self.curSolution[i] = self.curSolution[i],self.curSolution[depth]
                    # 同理这里为什么是depth-1 到 depth，为不是depth-1到i，也是一样的道理
                    self.curCost += self.graph[self.curSolution[depth-1]][self.curSolution[depth]]
                    # 进入下一层
                    self.backtracking(depth+1)
                    # 回溯处理，恢复现场
                    self.curCost -= self.graph[self.curSolution[depth-1]][self.curSolution[depth]]
                    self.curSolution[depth],self.curSolution[i] = self.curSolution[i],self.curSolution[depth]
#                self.curSolution[depth],self.curSolution[i] = self.curSolution[i],self.curSolution[depth]
                    
    def print_Result(self):
        # 我们需要求除了起点之外的[顶点1，...顶点n-1]n-1个起点的全排列
        self.backtracking(1)
        print(self.bestCost)   
        print(self.bestSolution)        

#%%
import numpy as np
import heapq
class Node:
    def __init__(self,curCost=None,depth=None,rcost = None,path = None,lbound =None):
        # 限界函数，我们定义限界函数为：当前走过的长度+未走过的结点最小出边的长度和
        # 这个用于优先级队列排序
        self.lbound = lbound
        # 当前走过的距离
        self.curCost = curCost
        # 当前的解的深度
        self.depth = depth
        # 路径，从0到depth为已走过的，depth+1到n-1为未走过的结点
        self.path = path
        # depth到n-1为未走过的结点的最小出边的和
        self.rcost = rcost
    
    # 这个用于结点比较大小，之前的（weights,node)方式有时会出问题，是有时候，
    # 现在使用这种方式，lt means less than
    def __lt__(self,other):

              return int(self.lbound) <int(other.lbound)

class prune_Traveling_saleman:
    def __init__(self,graph,start=0):
        self.num = len(graph)
        self.graph =  graph
        self.start = start
        
        # 用于存储最优的结果
        self.bestNode = Node(np.inf,-1,-1,None,-1)
        
        # 用于存储每个顶点的最小出边
        self.minOut = [np.inf]*self.num
        # 所有的最小出边之和
        self.minSum =0
        for i in range(self.num):
            for j in range(self.num):
                if i !=j and graph[i][j] < self.minOut[i]:
                    self.minOut[i] = graph[i][j]
            self.minSum += self.minOut[i]
            

    
       
    def traveling_Saleman(self):
        pqueue =[]
                 
        # 第0层，就是起点，也可以认为是第一层，这里为了处理数据方便成为第0层
        # [i for i in range(self.num)]为开始的路径[0,1,2,3],path[0]是已经确定为0
        # 最开始curCost =0，depth=0，rcost =self.minSum，lbound=  self.minSum
        curNode = Node(0,0,self.minSum,[i for i in range(self.num)],self.minSum)
        # 把第一个结点放入
        pqueue = [curNode,]
        depth =0

        
        while depth <= self.num-2:
            # 弹出结点
            curNode = heapq.heappop(pqueue)
            curCost = curNode.curCost
            depth = curNode.depth
            rcost = curNode.rcost
            path = curNode.path
            # 当处于倒数第2层时，就可以处理最后结果了，可以考虑结束了
            if depth == self.num-2:
                # 处于当处于倒数第2层时，lbound就是当前走过的距离+当前结点到最后一个结点的距离
                # + 最后一个结点到起点的距离；实际上也可以考虑self.num-1层，那就只需要加上
                # 当前结点到起点的距离
                lbound = curCost + self.graph[path[depth]][path[depth+1]] + self.graph[path[depth+1]][path[0]]
                # 如果下界小于当前最优的结果，就可以考虑输出结果了
                if lbound < self.bestNode.curCost:
                    # 把当前值和当前路径输出
                    self.bestNode.curCost = lbound
                    self.bestNode.path = path
                    
                    # 以下只是方便退出，当depth == self.num-1时退出
                    node = Node(lbound,depth+1,lbound,path,lbound)
                    heapq.heappush(pqueue,node)
                    
            else:
                # 一般情况下首先更新下一层，也就是未走过结点最小出边和，
                # 需要减去当前结点的最小出边，
                temp_rcost = rcost - self.minOut[path[depth]]
                for i  in range(depth+1,self.num):
                    # 当前走过的距离，需要更新为加上当前结点到下一个结点的距离
                    temp_cur = curCost + self.graph[path[depth]][path[i]]
                    # 当前结点的下界为，当前走过的距离+未走过结点最小出边和
                    lbound =  temp_cur + temp_rcost
                    # 只有当下界小于self.bestNode.curCost才有放入优先级队列的必要
                    if lbound < self.bestNode.curCost:#  
                        # 放入前需要更新path里面这一层depth加入的结点号
                        # 只要把path[depth]记录为当前选择的结点就行了，同时path[depth]位置
                        # 之前放置的那个结点放到刚刚空的那个地方就行了
                        # 这一层还有其他的分支，所有不能直接在path上操作，因为这样下一个分支也
                        # 用这个path就乱了。也可以可以先换了，压入之后再换回来
                        temp_path = path[:]
                        temp_path[depth+1],temp_path[i] = temp_path[i],temp_path[depth+1]
                        # 把这个分支压入优先级队列
                        node = Node(temp_cur,depth+1,temp_rcost,temp_path,lbound)
                        heapq.heappush(pqueue,node)

            
    def print_Result(self):
        self.traveling_Saleman()
        print(self.bestNode.curCost)
        print(self.bestNode.path)
            

g =[[0,5,9,4],
    [5,0,13,2],
    [9,13,0,7],
    [4,2,7,0]]

backtracking_Traveling_saleman(g,0).print_Result()
prune_Traveling_saleman(g,0).print_Result()


#%%
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
            

            # 处于解的最后一层，lbound就为当前的距离+当前点到起点的距离
            # 在这种情况下需要注意，需要把结点弹出放在循环体的最后，到达self.num就
            # 退出循环了，不会再进入判断体，否者进入判断，else就会报越界
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