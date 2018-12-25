# -*- coding: utf-8 -*-
# =============================================================================
# 分支限界法，dijkstra算法
# 首先解空间[起点0，顶点1，当点2，...,顶点n-1]看成[起点，剩余n-1个顶点的排列树]
# 下界函数bound()是什么了?
#  可以参考货郎问题：下届为 已走过的路+未走过的路（未走过的结点的最小出边和）
# 同时我们可以优化下界函数，我们知道起点到最后一个顶点的最短距离，那么他途径得的顶点
# 都是最短距离，那么我们可以把顶点到起点的最短距离当作下界
# =============================================================================

import heapq
def dijkstra(graph,start):
    # 解空间的长度
    vnum = len(graph)
    # 优先级队列
    pqueue = []
    # 把起点放入队列，[顶点到起点的距离，前驱结点，当前结点]
    heapq.heappush(pqueue,(0.0,None,start))
    # 有两个用途：一是用来标记那些顶点已经访问了，二是用于存储前驱结点，用于解的追踪
    paths = {vertex : None for vertex in graph}
    # depth可以放在活结点里
    depth = 0
    # 循环体出口时是解满了
    while depth < vnum :
        # 弹出结点
        pair = heapq.heappop(pqueue)
        distance = pair[0]
        parent = pair[1]
        vertex = pair[2]
        # 加入结点已经访问过了，就直接弹出下一个结点
        if paths[vertex]:
            continue
        # 把该节点到起点的最短距离和前驱结点保存起来，并记录该节点已经访问过了
        paths[vertex] = (parent,distance)
        # 把该节点的子节点放入优先级队列，这里进行了剪枝，只放入和当前结点相连的结点
        # 不相连的结点，认为距离为无穷，没有必要放入到优先级队列
        # 以下是相连的边的终点顶点，把他们放入优先级队列
        edges = graph[vertex]
        for v in edges:
            # 加入终结点已经访问过，就没有必要加入，这是一个排列树
            if paths[v] is None:
                # 把这个顶点到起点的距离，这个结点，前驱结点加入队列，
                # 这个顶点到起点的距离：源节点的最短距离+他们的边的长度
                heapq.heappush(pqueue,(distance + graph[vertex][v],vertex,v))
        # 进入下一层，这个策略由于上面的continue保证了，每次到这儿可以进入下一层了，
        # 也可以把depth放到活结点里，放到活结点，就必须要注意循环体的退出
        depth += 1
    return paths


g = {'A':{'B':1,'C':2},
     'B':{'A':1,'C':3,'D':4},
     'C':{'A':2,'B':3,'D':5,'E':6},
     'D':{'B':4,'C':5,'E':7,'F':8},
     'E':{'C':6,'D':7,'G':9},
     'F':{'D':8},
     'G':{'E':9}
    }

t=dijkstra(g,'A')
print(t)