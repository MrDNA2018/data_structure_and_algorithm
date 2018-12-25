# -*- coding: utf-8 -*-

class pack_01_back_test:        
    def __init__(self,N,V,C,W):
        self.num =N
        self.V = V
        self.C = C
        self.W = W
        self.BestResult = [False]*N
        self.Selected = [False]*N
        self.BestValue = 0
        self.CurCost = 0
        self.CurValue = 0
    
    def pack_01_back_tracking(self,depth):
        
        if depth > self.num-1:
            if self.CurValue > self.BestValue:
                self.BestValue = self.CurValue               
                self.BestResult[:] = self.Selected[:]

        else:
            if self.CurCost + self.C[depth] <= self.V:
                self.Selected[depth] = True
                
                self.CurCost += self.C[depth]
                self.CurValue  += self.W[depth]
                # next
                self.pack_01_back_tracking(depth+1)
                # undo
                self.CurCost -= self.C[depth]
                self.CurValue  -= self.W[depth]

            self.Selected[depth] = False
            self.pack_01_back_tracking(depth+1)
        
    def print_Result(self):
        self.pack_01_back_tracking(0)
        print(self.BestResult)
        print(self.BestValue)


#%%
class FIFO_01_Pack:
    def __init__(self,N,V,C,W):
        self.num =N
        self.Volume = V
        self.Cost = C
        self.Value = W
        # 追踪解，广度优先搜索，同一个纬度，假如不加指标判断的话，根本不知道最优解
        # 是选择的哪一个，所以需要同一个纬度的每一个结点，记住他之前的路径，才能在最优解的
        # 时候之前是怎么走过来的，这样实现的得不偿失，加入限界函数
#        self.BestResult = [False]*N
#        self.Path = [0]*N
        self.BestValue = 0
        
        #用于存放活结点，便于理解，把根结点，以及第0层结束标志-1放进去
        # 结点包括2个属性：当前空间大小，当前的价值大小
        self.queue = [[0,0],[-1,-1],]  

    # 实现时叶子结点不加入到活结点列表，当属于叶子结点时，增加对结果的处理
    def enQueen(self,pair,depth):
        if depth == self.num -1:
            CurValue = pair[1]
            if CurValue > self.BestValue:
                self.BestValue = CurValue
        else:
            self.queue.append(pair)
            
    def pack_01(self):
#        selected = [0]*self.num      
        # 首先取出根结点
        depth = 0
        pair = self.queue.pop(0)
        CurCost = pair[0]
        CurValue = pair[1]
        



        while True:
            # 判断左结点能否加入到队列，能的话，把当前空间和当前价值放入队列
            if CurCost + self.Cost[depth] < self.Volume:
                self.enQueen([CurCost + self.Cost[depth],CurValue + self.Value[depth]],depth)
            # 右结点总是可以加入队列的，因为没有约束条件的限制
            self.enQueen([CurCost,CurValue],depth)
            
            # 然后弹出下一个结点
            pair = self.queue.pop(0)
            CurCost = pair[0]
            CurValue = pair[1]
            
            # 当同一层处理完毕时，先判断是否能够输出结果，判断的标准是队列是否为空，
            # 这时下一层的所有结点已经加入了队列，这时需要把下一层
            # 增加一个结尾-1便于判断，然后进入下一层，弹出下一个结点
            if CurCost == -1:
                if not self.queue:
                    return self.BestValue
                self.enQueen([-1,-1],depth)
                depth += 1
                pair = self.queue.pop(0)
                CurCost = pair[0]
                CurValue = pair[1]
    
    def print_Result(self):
        print(self.pack_01())
        
#%%
class FIFO_01_Pack_prune:
    def __init__(self,N,V,C,W):
        self.num =N
        self.Volume = V
        self.Cost = C
        self.Value = W
        # 追踪解，广度优先搜索，同一个纬度，假如不加指标判断的话，根本不知道最优解
        # 是选择的哪一个，所以需要同一个纬度的每一个结点，记住他之前的路径，才能在最优解的
        # 时候之前是怎么走过来的，这样实现的得不偿失，加入限界函数
#        self.BestResult = [False]*N
#        self.Path = [0]*N
        self.BestValue = 0
        
        #用于存放活结点，便于理解，把根结点，以及第0层结束标志-1放进去
        # 结点包括2个属性：当前空间大小，当前的价值大小
        self.queue = [[0,0],[-1,-1],]  
        # 当前剩余价值和,bound()限界函数
        self.rest = 0
        for i in range(1,N):
            self.rest += W[i]
        

    # 实现时叶子结点不加入到活结点列表
    def enQueen(self,pair,depth):
        if depth < self.num -1:
            self.queue.append(pair)
            
    def pack_01(self):
#        selected = [0]*self.num      
        # 首先取出根结点
        depth = 0
        pair = self.queue.pop(0)
        CurCost = pair[0]
        CurValue = pair[1]
        
        while True:
            # 判断左结点能否加入到队列，能的话，把当前空间和当前价值放入队列,满足约束条件
            if CurCost + self.Cost[depth] < self.Volume:
                # 满足限界函数
                if CurValue + self.Value[depth] + self.rest > self.BestValue:
                    # 在进入左子树时，更新bestvalue
                    self.BestValue = CurValue + self.Value[depth]                   
                self.enQueen([CurCost + self.Cost[depth],CurValue + self.Value[depth]],depth)
            
            # 右满足限界函数
            if CurValue + self.Value[depth] + self.rest > self.BestValue:
                self.enQueen([CurCost,CurValue],depth)
            
            # 然后弹出下一个结点
            pair = self.queue.pop(0)
            CurCost = pair[0]
            CurValue = pair[1]
            
            # 当同一层处理完毕时，先判断是否能够输出结果，判断的标准是队列是否为空，
            # 这时下一层的所有结点已经加入了队列，这时需要把下一层
            # 增加一个结尾-1便于判断，然后进入下一层，弹出下一个结点
            if CurCost == -1:
                if not self.queue:
                    return self.BestValue
                self.enQueen([-1,-1],depth)
                depth += 1
                # 在刚进入下一层时，更新rest
                self.rest -= self.Value[depth]
                # 弹出下一个结点
                pair = self.queue.pop(0)
                CurCost = pair[0]
                CurValue = pair[1]
    
    def print_Result(self):
        print(self.pack_01())                
    
#%%
N = 8
V = 30
C = [11,2,3,9,13,6,15,7,19]
W = [5.0,2.0,5.0,7.0,5.0,11.0,6.0,14.0]

#pack_01_back_test(N,V,C,W).print_Result()
FIFO_01_Pack_prune(N,V,C,W).print_Result()

#%%
# 这种解法注意回溯函数一致性，思路比较清晰：满足剪枝条件就回溯：CurValue + rest <= BestValue
# 这是基于深度优先搜索的回溯法剪枝,以下是迭代实现方法
def pack_01_back_prune_iteration_test(N,V,C,W):
    depth = 0
    BestResult = [False]*N
    Selected = [False]*(N)
    BestValue = 0
    CurCost = 0
    CurValue = 0   
    # bound()限界函数
    rest = 0
    for i in range(N):
        rest += W[i]
    
    while True:
        # 尽量向左走直到不满足约束条件
        while depth < N and CurCost + C[depth] <= V:
            rest -=W[depth]
            Selected[depth] = True
            CurCost += C[depth]
            CurValue  += W[depth]
            depth +=1
        # 走到底，结果处理
        if depth >= N:
            BestValue = CurValue                
            BestResult[:] = Selected[:]
        # 不能往左走，就向右走，注意这里只是走一步而已
        else:
            rest -=W[depth]
            Selected[depth] =False
            depth +=1
        
        # 当不满足限界函数的时候，就需要回溯，注意底部也满足这个条件
        while CurValue + rest <= BestValue:
            # 回溯的处理，之所有需要depth -=1，上面走的时候都depth++了，底部也是这样
            depth -=1
            while depth >=0 and not Selected[depth]:
                rest +=W[depth]
                depth -=1
            # 当回溯到root的之后，无法回溯了，输出结果
            if depth < 0:
                return BestResult,BestValue
            # 回溯恢复现场
            else:
                Selected[depth] =False
                CurCost -= C[depth]
                CurValue  -= W[depth]
                depth +=1
    
#%%
class pack_01_back_prune_test:        
    def __init__(self,N,V,C,W):
        self.num =N
        self.V = V
        self.C = C
        self.W = W
        self.BestResult = [False]*N
        self.Selected = [False]*N
        self.BestValue = 0
        self.CurCost = 0
        self.CurValue = 0
        # bound()限界函数
        self.rest = 0
        for i in range(N):
            self.rest += W[i]
        
    
    def pack_01_back_tracking(self,depth):
        
        if depth > self.num-1:
            if self.CurValue > self.BestValue:
                self.BestValue = self.CurValue               
                self.BestResult[:] = self.Selected[:]

        else:
            # 满足约束条件和限界函数的处理
            if self.CurCost + self.C[depth] <= self.V and self.CurValue + self.rest > self.BestValue:
                self.Selected[depth] = True
                
                self.CurCost += self.C[depth]
                self.CurValue  += self.W[depth]
                self.rest -= self.W[depth]
                # next
                self.pack_01_back_tracking(depth+1)
                # undo
                self.CurCost -= self.C[depth]
                self.CurValue  -= self.W[depth]
                self.rest += self.W[depth]
            # 满足限界函数   
            if self.CurValue + self.rest > self.BestValue:
                self.Selected[depth] = False
                self.pack_01_back_tracking(depth+1)
        
    def print_Result(self):
        self.pack_01_back_tracking(0)
        print(self.BestResult)
        print(self.BestValue)                
                

N = 8
V = 30
C = [11,2,3,9,13,6,15,7,19]
W = [5.0,2.0,5.0,7.0,5.0,11.0,6.0,14.0]

print(pack_01_back_prune_iteration_test(N,V,C,W))

pack_01_back_prune_test(N,V,C,W).print_Result()

#%%
# 修改成结点，为了追踪解，新增两个变量，是否选择物品和前一个物品的结点
class Node:
    def __init__(self, CurCost=None,CurValue=None,Flag=None,parent=None):
        # 部分解所占体积
        self.CurCost = CurCost
        # 部分解所占价值
        self.CurValue = CurValue
        # 当前结点是否选择了物品
        self.isleft = Flag
        # 前一个结点是谁
        self.parent = parent

#%%        
class FIFO_01_Pack_with_solution_tracking:
    def __init__(self,N,V,C,W):
        self.num =N
        self.Volume = V
        self.Cost = C
        self.Value = W
        # 存放最优解
        self.BestResult = [False]*N
#       最优解结点，这里是叶子结点
        self.BestNode = Node(0,0,False,None)
        
        #用于存放活结点，便于理解，把根结点，以及第0层结束标志-1放进去
        # 结点包括2个属性：当前空间大小，当前的价值大小
        self.queue = [Node(0,0,False,None),Node(-1,-1,False,None),]  

    # 实现时叶子结点不加入到活结点列表，当属于叶子结点时，增加对结果的处理
    def enQueen(self,node,depth):
        if depth == self.num -1:
            CurValue = node.CurValue
            if CurValue > self.BestNode.CurValue:
                self.BestNode.CurValue = CurValue
                self.BestNode.isleft = node.isleft
                self.BestNode.parent = node.parent               
        else:
            self.queue.append(node)
            
    def pack_01(self):
#        selected = [0]*self.num      
        # 首先取出根结点
        depth = 0
        node = self.queue.pop(0)
        CurCost = node.CurCost
        CurValue = node.CurValue
        
        while True:
            # 判断左结点能否加入到队列，能的话，把当前空间和当前价值放入队列
            if CurCost + self.Cost[depth] < self.Volume:
                # 这时的父节点就是node
                self.enQueen(Node(CurCost + self.Cost[depth],CurValue + self.Value[depth],True,node),depth)
            # 右结点总是可以加入队列的，因为没有约束条件的限制
            self.enQueen(Node(CurCost,CurValue,False,node),depth)
            
            # 然后弹出下一个结点
            node = self.queue.pop(0)
            CurCost = node.CurCost
            CurValue = node.CurValue
            
            # 当同一层处理完毕时，先判断是否能够输出结果，判断的标准是队列是否为空，
            # 这时下一层的所有结点已经加入了队列，这时需要把下一层
            # 增加一个结尾-1便于判断，然后进入下一层，弹出下一个结点
            if CurCost == -1:
                if not self.queue:
                    return self.BestNode.CurValue
                self.enQueen(Node(-1,-1,False,None),depth)
                depth += 1
                node = self.queue.pop(0)
                CurCost = node.CurCost
                CurValue = node.CurValue
    
    def solution_Tracking(self):
        #追踪解从self.BestNode开始追踪
        for j in range(self.num-1,-1,-1):
            self.BestResult[j] = self.BestNode.isleft
            self.BestNode = self.BestNode.parent
        return self.BestResult
        
            
    def print_Result(self):
        print(self.pack_01())
        print(self.solution_Tracking())
        

N = 8
V = 30
C = [11,2,3,9,13,6,15,7]
W = [5.0,2.0,5.0,7.0,5.0,11.0,6.0,14.0]

FIFO_01_Pack_with_solution_tracking(N,V,C,W).print_Result()

#%%
import heapq

class Nodes:
    def __init__(self,CurValue=None,CurCost=None,depth =None,parent=None,Flag=None):
        
        # 部分解所占体积
        self.CurCost = CurCost
        # 部分解所占价值
        self.CurValue = CurValue
        # 处于那一层
        self.depth = depth
        # 当前结点是否选择了物品        
        self.isleft = Flag
        # 前一个结点是谁
        self.parent = parent

class PQ_pack_01_with_solution_tracking:
    def __init__(self,N,V,C,W):
        self.num = N
        self.volume = V
        self.cost = C
        self.value = W
                    
        #(0当前的价值，1,当前体积，2当前的深度，3父节点，4是否选择了该物品)
        self.bestnode = Nodes(0,0,0,None,False)
        # 保存最后的方案
        self.bestsolution = [False]*N
        # 数据预处理，为什么需要预处理数据了，这里使用的是优先级队列，这个优先级的选区非常重要，也非常重要
        # 之前的策略curValue+rest就不行了，因为在这种策略下，无法保证最优，这时需要精心挑选优先级，就像
        # 思考贪心策略那样，实际上就是思考贪心策略，贪心就是配合优先级队列使用的
        # 这里首先把数据安装单位体积价值降序排列，self.order记录与之前排列的标号，用于恢复最后结果
        self._cost,self._value,self.order = self.sort_group(N,C,W)

    # 把数据安装单位体积价值降序排列
    def sort_group(self,N,C,W):
        # 原来数据的标号
        O = [i for i in range(N)]
        
        perp = [0]*N
        
        for i in range(N):
            perp[i] = W[i]/C[i]
            
        for i in range(N-1):
            for j in range(i+1,N):
                if  perp[i] < perp[j]:                    
                    temp = perp[i]
                    perp[i] = perp[j]
                    perp[j] = temp
                    
                    temp = O[i]
                    O[i] = O[j]
                    O[j] = temp
                    
                    temp = C[i]
                    C[i] = C[j]
                    C[j] = temp
                    
                    temp = W[i]
                    W[i] = W[j]
                    W[j] = temp                    
                    
        return C,W,O
    
    
    # 限界函数，这个限界函数就非常精确，确保了每一次往下都是最优的策略
    def bound(self,depth,CurCost,CurValue):
        left_weight = self.volume - CurCost
        b = CurValue
        
        while depth < self.num and self._cost[depth] <= left_weight:
            left_weight -=self._cost[depth]
            b += self._value[depth]
            depth +=1
            
        if depth < N:
            b += (self._value[depth]/self._cost[depth]) * left_weight
            
        return b
    
    def PQ_pack_01(self):
        
        pqueue = []   
        # 初始化，从root开始
        current_node = None
        current_value = 0
        current_cost = 0
        depth = 0
        
                
        # 终止条件，优先级队列里面存的是(0当前的价值，1,当前体积，2当前的深度，3父节点，4是否选择了该物品)
        # 只要取第self.num层最优的current_value就可以了，只要到self.num层终止就行了
        while depth != self.num:
            # 满足约束条件，存入左结点
            if current_cost + self._cost[depth] <= self.volume:
                # 每次进入左结点更新最优质，这样方便剪枝，让没有必要的点不放进优先级队列
                if current_value + self._value[depth] > self.bestnode.CurValue:
                    self.bestnode.CurValue =current_value + self._value[depth]
                    # 确定待放入结点的上界
                    temp = self.bound(depth+1,current_cost+self._cost[depth],current_value+self._value[depth])
                    # 把待放入结点的上界，当前价值，当前花费，当前层次，父亲，是左是右放入优先级队列
                    # 因为是要求最大堆，随意优先级取了-，heapq默认是取最小堆，直接求最大堆的包还不知道怎么用
                    heapq.heappush(pqueue,(-temp,Nodes(current_value + self.value[depth],current_cost+self._cost[depth],depth+1,current_node,True)))
        
            # 对于右结点计算上界
            up = self.bound(depth+1,current_cost,current_value)
            # 加入上界小于当前最优质，就没有必要放入优先级队列，免得给优先级队列增加负担
            # 等于的情况需要放进去，因为这时路径必须的，没有等于0，就没法深入了
            if up >= self.bestnode.CurValue:
                heapq.heappush(pqueue,(-up,Nodes(current_value,current_cost,depth+1,current_node,False)))
            
            # 弹出下一个最优的结点，0代表上界，1包含了所需要的信息
            current_node = heapq.heappop(pqueue)[1]
                        
            current_value = current_node.CurValue
            current_cost = current_node.CurCost
            depth = current_node.depth
            print(depth,current_value)

            
        self.bestnode = current_node
        print(self.bestnode.CurValue)
        
     # 追踪解   
    def solution_tracking(self):
        # 追踪解，获取最优方案
        BestResult =[False]*N
        for i in range(self.num -1,-1,-1):
            BestResult[i] = self.bestnode.isleft
            self.bestnode = self.bestnode.parent
        # 将最优方案翻译成原来的排序    
        for i in range(N):
            if BestResult[i]:
                self.bestsolution[self.order[i]] = True
                
        print(self.bestsolution)
            
        
        
N = 8
V = 30
C = [11,2,3,9,13,6,15,7]
W = [5.0,2.0,5.0,7.0,5.0,11.0,6.0,14.0]
            
tt =PQ_pack_01_with_solution_tracking(N,V,C,W)
tt.PQ_pack_01()     
tt.solution_tracking()
        
        
    