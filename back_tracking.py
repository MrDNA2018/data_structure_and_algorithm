# -*- coding: utf-8 -*-
def pack_01_back(N,V,C,W):
    BestResult = [False]*N
    Selected = [False]*N
    BestValue = [0]
    CurCost = [0]
    CurValue = [0]
    
    def pack_01_back_tracking(depth):
        
        if depth > N-1:
            if CurValue[0] > BestValue[0]:
                BestValue[0] = CurValue[0]                
                BestResult[:] = Selected[:]

        else:
            if CurCost[0] + C[depth] <= V:
                Selected[depth] = True
                
                CurCost[0] += C[depth]
                CurValue[0]  += W[depth]
                # next
                pack_01_back_tracking(depth+1)
                # undo
                CurCost[0] -= C[depth]
                CurValue[0]  -= W[depth]
        

            Selected[depth] = False
            pack_01_back_tracking(depth+1)
        
        
    pack_01_back_tracking(0)
    
    return BestResult,BestValue
#%%                
def pack_01_back_iteration2(N,V,C,W):
    depth = 0
    BestResult = [False]*N
    Selected = [False]*(N)
    BestValue = 0
    CurCost = 0
    CurValue = 0    
    
    while True:
        if depth < N:
            if CurCost + C[depth] <= V:
                Selected[depth] = True
                CurCost += C[depth]
                CurValue  += W[depth]
            else:
                Selected[depth] = False
                
        else:
            if CurValue > BestValue:
                BestValue = CurValue                
                BestResult[:] = Selected[:]
            
            depth -=1
            while depth >= 0 and not Selected[depth]:
                depth -=1
            
            if depth < 0:
                break
            
            else:
                Selected[depth] =False
                CurCost -= C[depth]
                CurValue  -= W[depth]
        
        depth +=1
    
    return BestResult,BestValue
                
#%%
def pack_01_back_iteration3(N,V,C,W):
    depth = 0
    BestResult = [False]*N
    Selected = [False]*(N)
    BestValue = 0
    CurCost = 0
    CurValue = 0   
    rest = 0
    for i in range(N):
        rest += W[i]
    
    while True:
        while depth < N and CurCost + C[depth] <= V:
            rest -=W[depth]
            Selected[depth] = True
            CurCost += C[depth]
            CurValue  += W[depth]
            depth +=1
            
        if depth >= N:
            BestValue = CurValue                
            BestResult[:] = Selected[:]
        else:
            rest -=W[depth]
            Selected[depth] =False
            depth +=1
            
        while CurValue + rest <= BestValue:
            depth -=1
            while depth >=0 and not Selected[depth]:
                rest +=W[depth]
                depth -=1
        
            if depth < 0:
                return BestResult,BestValue
            
            else:
                Selected[depth] =False
                CurCost -= C[depth]
                CurValue  -= W[depth]
                depth +=1
    
    

N = 8
V = 30
C = [11,2,3,9,13,6,15,7,19]
W = [5.0,2.0,5.0,7.0,5.0,11.0,6.0,14.0]

print pack_01_back_iteration3(N,V,C,W)

#%%
def pack_01_back_iteration(N,V,C,W):

    depth = 0
    BestResult = [False]*N
    Selected = [False]*(N)
    BestValue = 0
    CurCost = 0
    CurValue = 0
    
    while depth >= 0:
        
        while depth < N: 
            if CurCost + C[depth] <= V:
                Selected[depth] = True
                CurCost += C[depth]
                CurValue  += W[depth]
                depth +=1
            else:
                Selected[depth] = False
                depth +=1
        
        if CurValue > BestValue:
            BestValue = CurValue                
            BestResult[:] = Selected[:N]

        depth -=1
        
        while depth > 0 and Selected[depth] == 0:
            depth -=1
        if Selected[depth] ==1:
            Selected[depth] =False
            CurCost -= C[depth]
            CurValue  -= W[depth]
            depth +=1
            
        if depth == 0:
            break
            
    return BestResult,BestValue

#%%
def pack_01_back_prune(N,V,C,W):
    BestResult = [False]*N
    Selected = [False]*(N)
    BestValue = [0]
    CurCost = [0]
    CurValue = [0]
    
    order = [i for i in range(N)]
    perp = [0]*N
    
    # sorted by value per weight
    def sort_group(C,W,O):
   
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
                    
        return perp,C,W,O
#   计算上界函数，功能为剪枝
#  判断当前背包的总价值cp＋剩余容量可容纳的最大价值<=当前最优价值
    def bound(depth):
        left_weight = V - CurCost[0]
        b = CurValue[0] 
        
        while depth < N and C[depth] <= left_weight:
            left_weight -=C[depth]
            b += W[depth]
            depth +=1
            
        if depth < N:
            b += perp[depth] * left_weight
            
        return b

    
    def backtracking(depth):
        
        if depth > N-1:
            if CurValue[0] > BestValue[0]:
                BestValue[0] = CurValue[0]                
                BestResult[:] = Selected[:]

        else:
#    如若左子节点可行，则直接搜索左子树;
#    对于右子树，先计算上界函数，以判断是否将其减去
            if CurCost[0] + C[depth] <= V :# and bound(depth+1) > BestValue[0]:
                Selected[depth] = True
                
                CurCost[0] += C[depth]
                CurValue[0]  += W[depth]
                # next
                backtracking(depth+1)
                # undo
                CurCost[0] -= C[depth]
                CurValue[0]  -= W[depth]
#           如若符合条件则搜索右子树     
            if bound(depth+1) > BestValue[0]:
                Selected[depth] = False
                backtracking(depth+1)
         
    
    perp,C,W,order = sort_group(C,W,order)
    backtracking(0)
    
    decode_BestResult =[False]*N
    for i in range(N):
        if BestResult[i]:
            decode_BestResult[order[i]] = True
            
    return decode_BestResult,BestValue
    
#%%
    
def pack_01_back_prune_iteration(N,V,C,W):
    BestResult = [False]*N
    Selected = [False]*(N)
    BestValue = [0]
    CurCost = [0]
    CurValue = [0]
    
    order = [i for i in range(N)]
    perp = [0]*N
    
    # sorted by value per weight
    def sort_group(C,W,O):
   
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
                    
        return perp,C,W,O
#   计算上界函数，功能为剪枝
#  判断当前背包的总价值cp＋剩余容量可容纳的最大价值<=当前最优价值
    def bound(depth):
        left_weight = V - CurCost[0]
        b = CurValue[0] 
        
        while depth < N and C[depth] <= left_weight:
            left_weight -=C[depth]
            b += W[depth]
            depth +=1
            
        if depth < N:
            b += perp[depth] * left_weight
            
        return b

    
    def backtracking_iteration(depth):
        
        while True:
            if depth < N:
                if CurCost[0] + C[depth] <= V and bound(depth+1) > BestValue[0]:
                    Selected[depth] = True
                    CurCost[0] += C[depth]
                    CurValue[0]  += W[depth]
                    
                elif bound(depth+1) > BestValue[0]:
                    Selected[depth] = False
                    
                else:
                    while depth >= 0 and not Selected[depth]:
                        depth -=1
                        
                    if depth < 0:
                        break
                    else:
                        Selected[depth] =False
                        CurCost[0] -= C[depth]
                        CurValue[0]  -= W[depth]                     
                    
            else:
                if CurValue[0] > BestValue[0]:
                    BestValue[0] = CurValue[0]                
                    BestResult[:] = Selected[:]
                
                depth -=1
                while depth >= 0 and not Selected[depth]:
                    depth -=1
                
                if depth < 0:
                    break
                
                else:
                    Selected[depth] =False
                    CurCost[0] -= C[depth]
                    CurValue[0]  -= W[depth]        
            depth +=1
        
        
        
    perp,C,W,order = sort_group(C,W,order)
    backtracking_iteration(0)
    
    decode_BestResult =[False]*N
    for i in range(N):
        if BestResult[i]:
            decode_BestResult[order[i]] = True
            
    return decode_BestResult,BestValue    
    
    
    
    
    
    
#%%
N = 8
V = 30
C = [11,2,3,9,13,6,15,7,19]
W = [5.0,2.0,5.0,7.0,5.0,11.0,6.0,14.0]

#print pack_01_back(N,V,C,W)
#print pack_01_back_iteration(N,V,C,W)
#print pack_01_back_iteration2(N,V,C,W)
print pack_01_back_prune(N,V,C,W)
print pack_01_back_prune_iteration(N,V,C,W)


    






