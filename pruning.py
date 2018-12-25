# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:38:02 2018
分支限界法
@author: geng
"""
import numpy as np
import heapq
class dijkstra:
    def __init__(self,graph,start):
        # 邻接表
        self.graph = graph
        # 顶点个数
        self.num = len(graph)
        #源点
        self.start = start
        # 已知最短路径，又叫当前最优值,并初始化
        self.dist = {vertex:np.Inf for vertex in graph}       
        self.dist[start] = 0.0
        # 初始化优先级队列
        self.queue = []
        heapq.heappush(self.queue,(0.0,start))
        #追踪解
        self.parent = {start:None}
        
    def shortest_Path(self):
             
        while self.queue:
             #取出根节点
            enode = heapq.heappop(self.queue)
            distance = enode[0]
            vertex = enode[1]
            # 取邻接的边，实际上过滤了不相邻的边
            # 这里可以写成 for j in range(self.num),
            # 看成完全n叉树，也可以看成随机叉树的处理
            for j in self.graph[vertex].keys():
                # 他们都叫这个为控制约束，两条到某同一点的路径，长的那一条后面就被剪掉了
                # 也就是贪心法里面的贪心策略
                if distance + self.graph[vertex][j] < self.dist[j] :
                    self.dist[j] = distance + self.graph[vertex][j]
                    self.parent[j] = vertex
                    
                    heapq.heappush(self.queue,(self.dist[j],j))
    
    def print_Result(self):
        print(self.parent)
        print(self.dist)
        

def dijkstra_test(graph,start):
    pqueue = []
    heapq.heappush(pqueue,(0.0,start))
    
    visit = set()
    parent = {start:None}
    distance = {vertex:np.Inf for vertex in graph}
    distance[start] = 0.0
    
    
    while pqueue:
        pair = heapq.heappop(pqueue)        
        dist = pair[0]
        vertex = pair[1]
        visit.add(vertex)
        
        edges = graph[vertex]
        for v in edges:
            if v not in visit:
                if dist + graph[vertex][v] < distance[v]:
                    heapq.heappush(pqueue,(dist + graph[vertex][v],v))
                    distance[v] = dist + graph[vertex][v]
                    parent[v] = vertex 
                    
    print(parent)
    print(distance)        

#%%
g = {'A':{'B':1,'C':2},
     'B':{'A':1,'C':3,'D':4},
     'C':{'A':2,'B':3,'D':5,'E':6},
     'D':{'B':4,'C':5,'E':7,'F':8},
     'E':{'C':6,'D':7,'F':9},
     'F':{'D':8,'E':9,'G':10},
     'G':{'F':10}
    }

dij = dijkstra(g,'D')
dij.shortest_Path()
dij.print_Result()

dijkstra_test(g,'D')
