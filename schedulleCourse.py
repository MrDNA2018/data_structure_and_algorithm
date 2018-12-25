# -*- coding: utf-8 -*-




class Soulution:
    def scheduleCourse(self,prerequests):
        num = len(prerequests)
        
        indegree = [[],[],[],[]]
        
        # prerequests为出度表，根据出度表构建入度表，删除某结点时，就可以删除，
        # 就知道哪些结点需要删除出度结点
        for from_id in range(num):
            for to_id in prerequests[from_id]:
                indegree[to_id].append(from_id)
        
        print(indegree)
        # 根据出度表，构建遍历的队列,遍历的策略是，那些出度为0的点
        queue =[]
        degree =[-1]*num
        for i in range(num):
            degree[i]= len(prerequests[i])
            if degree[i] == 0:
                queue.append(i)
        
        # 每次弹出一个出度为0的点，然后删除和这个点相邻的点的出度，这个地方只需要
        # 将出度的数量-1就行了
        
        # count表示已上了几门课
        count =0
        while queue:
            curid = queue.pop()
            count +=1
            
            # 下面是更新出度，更新待上课列表的操作
            for from_id in indegree[curid]:
                degree[from_id] -=1
                if degree[from_id] == 0:
                    queue.append(from_id)
        # 当上了的课程和总课程一致时代表上完了，否则代表有环，剩余课程相互约束无法先后上            
        return count == num
                    
        
prerequests = [[1],[2],[0]]
print(prerequests)
print(Soulution().scheduleCourse(prerequests))

prerequests1 = [[1],[3],[3],[]]
print(prerequests1)
print(Soulution().scheduleCourse(prerequests1))