# -*- coding: utf-8 -*-
# fib
        
def fib_sequence(n):
    def fib_rec(n):
        if n == 0 or n ==1:
            return n
        return fib_rec(n-1) + fib_rec(n-2)

    list = []
    for i in range(n):
        list += [fib_rec(i)]
        
    return list

#%%
def fib_top_down_(n):
    list = [-1]*(n)
    list[0] = 0
    list[1] = 1
    def fib_top_down(n):
        if list[n] == -1:
            list[n] = fib_top_down(n-1)+fib_top_down(n-2)
        return list[n]
    fib_top_down(n-1)
    return list

#%%        
def fib_botton_up_(n):
    list = [0,1]
    for i in range(2,n):
        list.append(list[i-1] + list[i-2])
        
    return list

    

    
#%%
print fib_sequence(20)
#%%
print fib_top_down_(20)
#%%
print fib_botton_up_(20)

#%%
# house gold
def house_gold_Rec(gold,n):
    if n == 0:
        return gold[0]
    if n == 1:
        return gold[gold[0]<gold[1]]
    first = gold[n]+house_gold_Rec(gold,n-2)
    second = house_gold_Rec(gold,n-1)
    return (first,second)[first<second]

def house_gold_Top_down_(gold):
    n = len(gold)
    list = [-1]*(n)
    list[0] = gold[0]
    list[1] = gold[gold[0]<gold[1]]
    
    def house_gold_Top_down(gold,n):
        if list[n] == -1:
            first = gold[n]+house_gold_Top_down(gold,n-2)
            second = house_gold_Top_down(gold,n-1)
            list[n] = (first,second)[first<second]
        return list[n]
    
    return house_gold_Top_down(gold,n-1)

def house_gold_Bottom_up(gold):
    n =len(gold)
    list= [gold[0],gold[gold[0]<gold[1]]]
    
    for i in range(2,n):
        first = gold[i]+list[i-2]
        second = list[i-1]
        list.append((first,second)[first<second])
            
    return list[n-1]
#%%    

gold = [10,28,5,77,5,10,99,88,67]
#%%
print house_gold_Rec(gold,len(gold)-1)
#%%
print house_gold_Top_down_(gold)
#%%
print house_gold_Bottom_up(gold)
#%%
#coin change
def coins_change_Rec(money,coins):
    if money == 0:
        return 0

    result = 1000
    for i in range(len(coins)):
        if money >= coins[i]:
            first = coins_change_Rec(money-coins[i],coins)
            result = (first,result)[first>result]        
    result += 1
    
        
    return result

def coins_change_Top_down_(money,coins):
    list = [-1]*(money+1)
    list[0] =0
    
    def coins_change_Top_down(money,coins):
        result = 10000
        for i in range(len(coins)):
            if money >= coins[i]:
                if list[money-coins[i]] == -1:
                    list[money-coins[i]] = coins_change_Top_down(money-coins[i],coins)
                result = (list[money-coins[i]],result)[list[money-coins[i]]>result]
        list[money] = result + 1
        return list[money]
    
    coins_change_Top_down(money,coins)    
#    print list
    return list[money]
    

def coins_change_bottom_up(money,coins):
    list = [0,]
    
    min_ = min(coins)
    for x in range(1,min_):
        list.append(10000)
        
    list.append(1)
    
        
    for j in range(min_+1,money+1):
        result = 10000
        for i  in range(len(coins)):
            if j >= coins[i]:
                result = (list[j-coins[i]],result)[list[j-coins[i]]>result]
        list.append(result +1)
#    print list
    return list[money]
#%%
coins = [13,11,19,23,29,66,46,90]
money = 101
print coins_change_Rec(money,coins)

print coins_change_Top_down_(money,coins)
print coins_change_bottom_up(money,coins)
#%%
def pack_0_1_Rec(N,V,C,W):
    if N == 0 or V < min(C) :
        return 0
    else:
        A = pack_0_1_Rec(N-1,V,C,W)       
        if V < C[N-1]: return A
        else: return max(A,pack_0_1_Rec(N-1,V-C[N-1],C,W) + W[N-1])
        
def pack_0_1_Rec2(N,V,C,W):
    if N == 0 :
        return 0
    if V < C[N-1]:
        return pack_0_1_Rec(N-1,V,C,W)
    return max(pack_0_1_Rec(N-1,V,C,W),pack_0_1_Rec(N-1,V-C[N-1],C,W) + W[N-1])

def pack_0_1_Top_down(N,V,C,W):
    list = [[-1]*(V+1) for i in range(N+1)]
    mins = min(C)
    for i in range(N+1):
        for j in range(V+1):
            if i == 0 or j< mins:
                list[i][j] =0

    
    def pack_0_1_Top_down_(N,V):
        if list[N][V] == -1 and N >=1 and V >=mins:
            A = pack_0_1_Top_down_(N-1,V)      
            if V < C[N-1]: return A
            else:
                list[N][V] = max(A,pack_0_1_Top_down_(N-1,V-C[N-1])+W[N-1])
                
            
        return list[N][V]
    
    return pack_0_1_Top_down_(N,V)

def pack_0_1_bottom_up(N,V,C,W):
    list = [[-1]*(V+1) for i in range(N+1)]
    mins = min(C)
    for i in range(N+1):
        for j in range(V+1):
            if i == 0 or j< mins:
                list[i][j] =0

    for i in range(1,N+1):
        for j in range(mins,V+1):
            A = list[i-1][j]  
            if j < C[i-1]: list[i][j] = A  
            else:
                list[i][j] = max(A,list[i-1][j-C[i-1]]+W[i-1])
#    print list      
    return list[N][V]

def pack_0_1_first(N,V,C,W):
    def ZeroOnePack(F,ci,wi):
        for v in range(V,ci-1,-1):
            F[v] = max(F[v],F[v-ci] + wi)
        return F
    F =[0]*(V+1)
    
    for i in range(1,N+1):
        ZeroOnePack(F,C[i-1],W[i-1])
    return F[V]

def pack_0_1_yes_or_no(N,V,C):
    def ZeroOnePack(F,ci):
        for v in range(V,ci-1,-1):
            F[v] = F[v-ci] or F[v]
        return F
    
    F =[-1]*(V+1)
    F[0] = True
    
    for i in range(1,N+1):
        ZeroOnePack(F,C[i-1])
        
    return F[V]
#%%
#%%
N = 6
V = 24
C = [1,3,9,19,13,6]
W = [2,9,7,5,11,4]
#%%
print pack_0_1_Rec(N,V,C,W)
print pack_0_1_first(N,V,C,W)
print pack_0_1_Top_down(N,V,C,W)
print pack_0_1_bottom_up(N,V,C,W)
print pack_0_1_Rec2(N,V,C,W)
print pack_0_1_yes_or_no(N,V,C)  

#%%
# another way: F [i, v] = max {F [i − 1, v − kC i ] + kW i | 0 ≤ kC i ≤ v}
def pack_complete_Rec2(N,V,C,W):
    if N ==0:
        return 0    
    k = V // C[N-1]
    result = -1
    for i in range(k+1):
        A = pack_complete_Rec2(N-1,V-i*C[N-1],C,W) + i*W[N-1]
        if A > result:
            result = A
    return result
import numpy as np
# 注意if list[N,V] == -1 的未知，因为它确定了剪枝；
def pack_complete_Top_down2(N,V,C,W):
    list = np.zeros((N+1,V+1),dtype=int)
    list[1:,:] = -1
    
    def complete_Top_down(N,V):
        t = V // C[N-1] 
        if list[N,V] == -1 :
            result = -1000
            for k in range(t+1):
                if N >=1:
                    A = complete_Top_down(N-1,V-k*C[N-1]) + k*W[N-1]
                    if A >= result:
                        result = A
            list[N,V] = result 
        return list[N,V]
    
    return complete_Top_down(N,V)
def pack_complete_Bottom_up2(N,V,C,W):
    list = np.zeros((N+1,V+1),dtype=int)
#    list[1:,:] = -1

    for i in range(1,N+1):
        for j in range(0,V+1):
            t = j // C[i-1]
            result = -1000
            for k in range(t+1):
                A = list[i-1,j-k*C[i-1]] + k*W[i-1]
                if A > result:
                    result = A
            list[i,j] = result         
     
    return list[N,V]
# change complete to 01
def change_complete_to_01(N,V,C,W):
    C_ =[]
    W_ =[]
    
    for i in range(N):
        t = V // C[i]
        for k in range(1,t+1):
            C_.append(C[i])
            W_.append(W[i])

    def pack_0_1_first(N,V,C,W):    
        F =[0]*(V+1)    
        for i in range(1,N+1):
            for v in range(V,C[i-1]-1,-1):
                F[v] = max(F[v],F[v-C[i-1]] + W[i-1])
        return F[V]
            
    N_ = len(C_)
    return pack_0_1_first(N_,V,C_,W_)

def pack_complete_Rec(N,V,C,W):
    if N ==0:
        return 0
    if V < C[N-1]:
        return pack_complete_Rec(N-1,V,C,W)
    return max(pack_complete_Rec(N-1,V,C,W),pack_complete_Rec(N,V-C[N-1],C,W) + W[N-1])  

import numpy as np
def pack_complete_Top_down(N,V,C,W):
    list = np.zeros((N+1,V+1),dtype=int)
    list[1:,:] = -1
    
    def complete_Top_down(N,V):
        if list[N,V] == -1 and N >=1:
            A = complete_Top_down(N-1,V)
            if V < C[N-1]: 
                return A
            else:
                list[N,V] = max(A,complete_Top_down(N,V-C[N-1])+W[N-1])
                
            
        return list[N,V]
    
    return complete_Top_down(N,V)

def pack_complete_Bottom_up(N,V,C,W):
    list = np.zeros((N+1,V+1),dtype=int)
    list[1:,:] = -1

    for i in range(1,N+1):
        for j in range(0,V+1):
            A = list[i-1,j]  
            if j < C[i-1]: 
                list[i,j] = A  
            else:
                list[i,j] = max(A,list[i,j-C[i-1]]+W[i-1])
     
    return list[N,V]
def pack_complete_first(N,V,C,W):
    def CompletePack(F,ci,wi):
        for v in range(ci,V+1):
            F[v] = max(F[v],F[v-ci] + wi)
        return F
    
    F =[0]*(V+1)
    
    for i in range(1,N+1):
        CompletePack(F,C[i-1],W[i-1])
    return F[V]
def pack_complete_first_yes_or_no(N,V,C):
    def CompletePack_or(F,ci,wi):
        for v in range(ci,V+1):
            F[v] = F[v] or F[v-ci]
        return F
    
    F =[False]*(V+1)
    F[0] = True
    
    for i in range(1,N+1):
        CompletePack_or(F,C[i-1],W[i-1])
    return F[V]

def pack_complete_Bottom_up_yes_or_no(N,V,C):
    list = np.zeros((N+1,V+1),dtype=bool)
    list[0,0] = True

    for i in range(1,N+1):
        for j in range(0,V+1):
            A = list[i-1,j]  
            if j < C[i-1]: 
                list[i,j] = A  
            else:
                list[i,j] = A or list[i,j-C[i-1]]
     
    return list[N,V]
#%%
#%%
N = 7
V = 77
C = [1,2,3,9,13,6,7,5]
W = [1,2,9,7,5,11,6,14]
#%%
print pack_complete_first(N,V,C,W)
print pack_complete_Rec(N,V,C,W)
print pack_complete_Top_down(N,V,C,W)
print pack_complete_Bottom_up(N,V,C,W)
print pack_complete_first_yes_or_no(N,V,C)
print pack_complete_Bottom_up_yes_or_no(N,V,C)
print pack_complete_Rec2(N,V,C,W)
print pack_complete_Top_down2(N,V,C,W)
print pack_complete_Bottom_up2(N,V,C,W)
print change_complete_to_01(N,V,C,W)
#%%
# F [i , v] = max {F [i − 1, v − k ∗ C i ] + k ∗ W i | 0 ≤ k ≤ M i }
import numpy as np
def pack_multiple_Bottom_up(N,V,C,W,M):
    list = np.zeros((N+1,V+1),dtype=int)

    for i in range(1,N+1):
        for j in range(0,V+1):
            t = min(j // C[i-1],M[i-1])
            result = -1000
            for k in range(t+1):
                A = list[i-1,j-k*C[i-1]] + k*W[i-1]
                if A > result:
                    result = A
            list[i,j] = result         
     
    return list[N,V]

def change_multiple_to_01(N,V,C,W,M):
    C_ =[]
    W_ =[]
    
    for i in range(N):
        t = min(V // C[i],M[i])
        k = 1
        j = t
        while 2*k <= t:
            C_.append(k*C[i])
            W_.append(k*W[i]) 
            j -= k
            k *= 2
        C_.append(j*C[i])
        W_.append(j*W[i])

    def pack_0_1_first(N,V,C,W):    
        F =[0]*(V+1)    
        for i in range(1,N+1):
            for v in range(V,C[i-1]-1,-1):
                F[v] = max(F[v],F[v-C[i-1]] + W[i-1])
        return F[V]
            
    N_ = len(C_)
    return pack_0_1_first(N_,V,C_,W_)

import numpy as np
def change_multiple_to_01_yes_or_no(N,V,C,M):
    C_ =[]
    
    for i in range(N):
        t = min(V // C[i],M[i])
        k = 1
        j = t
        while 2*k <= t:
            C_.append(k*C[i])
            j -= k
            k *= 2
        C_.append(j*C[i])

    def pack_0_1_first(N,V,C):    
        F =[False]*(V+1)
        F[0] = True   
        
        for i in range(1,N+1):
            for v in range(V,C[i-1]-1,-1):
                F[v] = F[v] or F[v-C[i-1]]
        return F[V]
            
    N_ = len(C_)
    return pack_0_1_first(N_,V,C_)

def pack_multiple_yes_or_no(N,V,C,M):
    list = np.zeros((N+1,V+1),dtype=int)
    list[:,:] = -1
    list[0,0] = 0
    for i in range(1,N+1):
        
        for j in range(V+1):
            if list[i-1,j] >=0:
                list[i,j] = M[i-1]
            else:
                list[i,j] = -1
        
        for j in range(V-C[i-1]+1):
            if list[i,j] >0:
                list[i,j+C[i-1]] = max(list[i,j+C[i-1]],list[i,j]-1) #list[i,j]-1 #
                
    return list[N,V]
                
    
    
 


def pack_01_and_complete_Bottom_up(N,V,C,W,M):
    list =[0]*(V+1)
    for i in range(1,N+1):
        if M[i-1] == 1:
            for v in range(V,C[i-1]-1,-1):
                list[v] = max(list[v],list[v-C[i-1]] + W[i-1])
        if M[i-1] == 1000:
            for v in range(C[i-1],V+1):
                list[v] = max(list[v],list[v-C[i-1]] + W[i-1])      
    return list[V]

def pack_01_and_complete_and_multiple_Bottom_up(N,V,C,W,M):
    list = np.zeros((N+1,V+1),dtype=int)

    for i in range(1,N+1):
        for j in range(0,V+1):
            t = min(j // C[i-1],M[i-1])
            result = -1000
            for k in range(t+1):
                A = list[i-1,j-k*C[i-1]] + k*W[i-1]
                if A > result:
                    result = A
            list[i,j] = result         
     
    return list[N,V]
#%%
N = 7
V = 100
C = [11,2,3,9,13,6,7,5]
W = [1,2,9,7,5,11,6,14]
M = [1000,1,1000,1,1000,1,1,1]

print pack_multiple_Bottom_up(N,V,C,W,M)
print change_multiple_to_01(N,V,C,W,M)
print pack_01_and_complete_Bottom_up(N,V,C,W,M)
print pack_01_and_complete_and_multiple_Bottom_up(N,V,C,W,M)

print change_multiple_to_01_yes_or_no(N,V,C,M)
print pack_multiple_yes_or_no(N,V,C,M)
#%%
def pack_01_and_complete_and_multiple_Bottom_up(N,V,C,W,M):
    list = np.zeros((N+1,V+1),dtype=int)
    G = np.zeros((N+1,V+1),dtype=int)

    for i in range(1,N+1):
        for j in range(0,V+1):
            t = min(j // C[i-1],M[i-1])
            result = -1000
            for k in range(t+1):
                A = list[i-1,j-k*C[i-1]] + k*W[i-1]
                if A > result:
                    result = A
                    G[i,j] = k
            list[i,j] = result         
     
    return list[N,V] ,G

def decode_G(G,N,V,W,C):
    i = N
    v = V
    while i > 0:
        print("Choose value {} : cost {}: how many {}".format(W[i-1],C[i-1],G[i,v]))
        v -= G[i,v]*C[i-1]
        i -= 1
    

#%%
N = 8
V = 20
C = [11,2,3,9,13,6,7,5]
W = [1,2,5,7,5,11,6,14]
M = [10,2,9,1,19,3,4,1]

value,path = pack_01_and_complete_and_multiple_Bottom_up(N,V,C,W,M)   
print value
decode_G(path,N,V,W,C)
#%%
import numpy as np
def pack_01_Bottom_up(N,V,C,W,K):           
    list = np.zeros((K,V+1),dtype = int)
    A =[0]*(K+1)
    B =[0]*(K+1)
    for i in range(1,N+1):
        for v in range(V,C[i-1]-1,-1):
            for k in range(K):
                A[k] = list[k,v]
                B[k] = list[k,v-C[i-1]] + W[i-1]   
            A[K],B[K] = -1,-1    
            x,y,k =0,0,0
            while k < K and (A[k] !=-1 or B[k] !=-1):
                if A[x] > B[y]:
                    list[k,v]= A[x]
                    x +=1
                else:
                    list[k,v] = B[y]
                    y +=1
                    
                if list[k,v] != list[k-1,v]:
                    k +=1
 
    return list[:,V]

#%%
N = 8
V = 20
K = 3
C = [11,2,3,9,13,6,7,5]
W = [1,2,5,7,5,11,6,14]

print pack_01_Bottom_up(N,V,C,W,K)
#%%
import numpy as np
def pack_01_track_solution_Bottom_up(N,V,C,W):
    track_solution = np.zeros((N+1,V+1),dtype = int)
    list =[0]*(V+1)
    for i in range(1,N+1):
        for v in range(V,C[i-1]-1,-1):
            if list[v] < list[v-C[i-1]] + W[i-1]:
                list[v] = list[v-C[i-1]] + W[i-1]
                track_solution[i,v] = 1
#            else:
#                track_solution[i,v] = 0  
    return list[V],track_solution

def pack_complete_track_solution_Bottom_up(N,V,C,W):
    track_solution = np.zeros((N+1,V+1),dtype = int)
    track_solution[1:,1:] =-1
    list =[0]*(V+1)
    for i in range(1,N+1):
        for v in range(C[i-1],V+1):
            if list[v] <= list[v-C[i-1]] + W[i-1]:
                list[v] = list[v-C[i-1]] + W[i-1]
                track_solution[i,v] = i
            else:
                track_solution[i,v] = track_solution[i-1,v]
                
    return list[V],track_solution

def track_solution(G,N,V,W,C):
    i = N
    v = V
    while i > 0:
        print("Choose value {} : cost {}: how many {}".format(W[i-1],C[i-1],G[i,v]))
        v -= G[i,v]*C[i-1]
        i -= 1
        
def track_solution_standard(G,N,V,W,C):
    i = N
    v = V
    while G[i,v] !=0:    
        
        i = G[i,v]
        m = 0
        while G[i,v] == i:
            m +=1
            v -=C[i-1]            
        print("Choose value {} : cost {}: how many {}".format(W[i-1],C[i-1],m))
        
        while  G[i,v] == -1:
            i -=1

#%%
N = 8
V = 30
C = [11,2,3,9,13,6,15,7,19]
W = [1,2,5,7,5,11,6,14]
value,path = pack_complete_track_solution_Bottom_up(N,V,C,W)   
print value
print path
track_solution_standard(path,N,V,W,C)        


#%%

# LCS F[i,v] = (max{F[i-1,v],F[i,v-1]},F[i-1,v-1] +1)[i == v]
# X = 'conservatives'
# Y = 'breather'
import numpy as np
def LCS(X,Y,N,V):
#    L = [[None]*(n+1) for i in xrange(m+1)] 
    list = np.zeros((N+1,V+1),dtype = int)
    list[1:,1:] =-1
    G = np.full((N+1,V+1),'0')
    
    for i in range(1,N+1):
        for v in range(1,V+1):
            if X[i-1] == Y[v-1]:
                list[i][v] = list[i-1,v-1] +1
                G[i][v] = '7'
            else:
                if list[i-1,v] > list[i,v-1]:
                    list[i][v] = list[i-1,v]
                    G[i][v] = '^'
                else:
                    list[i][v] =list[i,v-1]
                    G[i][v] = '<'
    return list,G

def print_LCS_Rec(X,Y,G,N,V):

    if N == 0 or V == 0:
        return 
    elif G[N,V] == '7':
        print_LCS_Rec(X,Y,G,N-1,V-1) 
        print X[N-1]
    elif G[N,V] == '<':
        print_LCS_Rec(X,Y,G,N,V-1)
    else :
        print_LCS_Rec(X,Y,G,N-1,V)
    return 
    
def print_LCS(X,Y,list,N,V):
    
    i = N
    v = V
    result = []
    
    while i > 0 and v > 0:
        if X[i-1] == Y[v-1]:
            result += X[i-1]
            i -=1
            v -=1
            
        elif list[i-1,v] > list[i,v-1]:
            i -=1
        else:
            v -=1           
    return result[::-1]
#
def print_LCS_(X,Y,G,N,V):
    
    i = N
    v = V
    result = []
    
    while i > 0 and v > 0:
        if G[i,v] == '7':
            result += X[i-1]
            i -=1
            v -=1
            
        elif G[i,v] == '^':
            i -=1
        else:
            v -=1           
    return result[::-1]   
    
#%%
X = 'breather'
Y = 'conservatives'

N = len(X)
V = len(Y)

value,path = LCS(X,Y,N,V)
print value
print path

print_LCS_Rec(X,Y,path,N,V)                

print print_LCS(X,Y,value,N,V)
print print_LCS_(X,Y,path,N,V)


#%%
#floyd DP
# d[k][i][j] = min(d[k-1][i][j], d[k-1][i][k]+d[k-1][k][j])（k,i,j∈[1,n]）
import numpy as np
def floyd_original(graph):
    vertex_num = len(graph)
    
    list = np.full((vertex_num+1,vertex_num+1,vertex_num+1),np.inf)
    list[:,0,:] = 0
    list[:,:,0] = 0
    
    for i in range(1,vertex_num+1):
        for j in range(1,vertex_num+1):
            list[0,i,j] = graph[i-1,j-1]
    
    for k in range(1,vertex_num+1):
        for i in range(1,vertex_num+1):
            for j in range(1,vertex_num+1):
                list[k,i,j] = min(list[k-1,i,j],list[k-1,i,k]+list[k-1,k,j])
                
    return list[vertex_num,1:,1:]

import numpy as np
def floyd(graph):
    vertex_num = len(graph)   
    list = np.zeros((vertex_num+1,vertex_num+1))
    
    for i in range(1,vertex_num+1):
        for j in range(1,vertex_num+1):
            list[i,j] = graph[i-1,j-1]
    
    for k in range(1,vertex_num+1):
        for i in range(1,vertex_num+1):
            for j in range(1,vertex_num+1):
                list[i,j] = min(list[i,j],list[i,k]+list[k,j])
                
    return list[1:,1:]

#%%
graph = np.full((7,7),np.inf)
graph[0,:3] = [0,1,2]
graph[1,:4] = [1,0,3,4]
graph[2,:4] = [2,3,0,6]
graph[3,1:5] = [4,6,0,7]
graph[4,3:6] = [7,0,9]
graph[5,4:7] = [9,0,10]
graph[6,5:7] = [10,0]

    

print floyd_original(graph)

print floyd(graph)


#%%
# dist[k][u] = min{ dist[k-1][u] ,min{dist[k-1][j]+Edge[j][u]} },j = 0,1,...,n-1；j!=u

import numpy as np
def Bellman_Ford_original(graph,start):
    vertex_num = len(graph)
    edge_num_ = vertex_num-1
    list = np.full((edge_num_+1,vertex_num+1),np.inf)
#    for i in range(1,vertex_num+1):
#        list[1,i] = graph[start,i-1]
    list[:,start+1] =0
    
    for k in range(1,edge_num_+1):
        for u in range(1,vertex_num+1):
            result = list[k-1,u]
            for j in range(1,vertex_num+1):
                if  graph[j-1,u-1]>0 and graph[j-1,u-1]<10000 and result > list[k-1,j] + graph[j-1,u-1]:
                    result = list[k-1,j] + graph[j-1,u-1]
            list[k,u] =result                     
    return list[k,1:]
            



def Bellman_Ford(graph,start):
    vertex_num = len(graph)
    edge_num_ = vertex_num-1
    list = np.full((vertex_num+1),np.inf)
    list[start+1] = 0
    
    path =[-1] * vertex_num    
    for i in range(vertex_num):
        if graph[start,i] < 10000:
            path[i] = start    
    path[start] = None
    
    
#    for i in range(1,vertex_num+1):
#        list[i] = graph[start,i-1]
                    

    
    for k in range(1,edge_num_+1):
        flag = True
        for u in range(1,vertex_num+1):
            for j in range(1,vertex_num+1):
                w = graph[j-1,u-1]
                if w>0 and w <10000 and list[u] > list[j] + w :
                    list[u] = list[j] + w
                    path[u-1] = j-1
                    flag = False
         # 提前退出，并检查是否有负回路              
        if flag == True:
            for u in range(1,vertex_num+1):
                for j in range(1,vertex_num+1):
                    if list[u] > list[j] + graph[j-1,u-1] :
                        print "there is a - cycle"
                        break
            break

        
    return list[1:],path
#%%    

graph = np.full((7,7),np.inf)
graph[0,:3] = [0,-1,2]
graph[1,:4] = [-1,0,3,4]
graph[2,:5] = [2,3,0,5,6]
graph[3,1:6] = [4,5,0,7,8]
graph[4,2:6] = [6,7,0,9]
graph[5,3:7] = [8,9,0,10]
graph[6,5:7] = [10,0]

print Bellman_Ford_original(graph,3)
value,path = Bellman_Ford(graph,3)
print value
print path


#%%

import heapq
import numpy as np

def dijkstra(graph,start):
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
                    
    return parent,distance

    #%%
    g = {'A':{'B':1,'C':2},
         'B':{'A':1,'C':3,'D':4},
         'C':{'A':2,'B':3,'D':5,'E':6},
         'D':{'B':4,'C':5,'E':7,'F':8},
         'E':{'C':6,'D':7,'G':9},
         'F':{'D':8},
         'G':{'E':9}
        }
    i,j=dijkstra(g,'A')
    print i
    print j
