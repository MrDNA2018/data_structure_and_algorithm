# -*- coding: utf-8 -*-
import numpy as np
# 任意点到第一个点的和
def sum_(arr,n):    
    b = [0]*(n+1)    
    for i in range(1,n+1):
        b[i] = b[i-1] + arr[i-1]        
    return b
# 任意两点之间的数组和
def weight_i_j(b,i,j):
    return b[j+1]-b[i]
    
#  m[i,j] = min{m[i,k-1] + m[k,j] } + w[i,j]  i<k<=j,0<i<j<n+1
# i ==j ,m[i,j] =0

    
def DynamicProgramming(arr):
    n = len(arr)
    b = sum_(arr,n)
    print(b)
    
    # 初始化，这个问题初始化为i==j时为0，也就是对角线上均为0
    m = np.zeros((n,n),int)
    solution = np.full((n,n),0)
    
    # 扫描的时候注意了，这种类型的问题，扫描顺序不是从左到右，从上到下
    # 扫描的基准是j-i的间距，沿着对角线往右上扫描，这里的i就是为j-i的长度,扫描的最后就是
    # m[0,n-1],这个就是最后的解
    # i <j 所以间距为从1 到 n-1
    for r in range(1,n):
        # 沿着对角线往下走
        for i in range(n-r):
            j = i + r        
            # 首先取第一个k = i+1
            m[i][j] = m[i][i] + m[i+1][j]
            # 用于解的追踪
            solution[i][j] = i
            
            # 比较求最小的
            for k in range(i+2,j+1):
                temp = m[i][k-1] + m[k][j]
                
                if temp < m[i][j]:
                    m[i][j] = temp
                    solution[i][j] = k-1
            # min{m[i,k-1] + m[k,j] } + w[i,j]       
            m[i][j] += weight_i_j(b,i,j)
    
    return m,solution
                
def DynamicProgrammingSpeed(arr):
    n = len(arr)
    b = sum_(arr,n)
    print(b)
    
    # 初始化，这个问题初始化为i==j时为0，也就是对角线上均为0
    m = np.zeros((n,n),int)
    solution = np.full((n,n),0)

    
    # 扫描的时候注意了，这种类型的问题，扫描顺序不是从左到右，从上到下
    # 扫描的基准是j-i的间距，沿着对角线往右上扫描，这里的i就是为j-i的长度,扫描的最后就是
    # m[0,n-1],这个就是最后的解
    # i <j 所以间距为从1 到 n-1
    for r in range(1,n):
        # 沿着对角线往下走
        for i in range(n-r):
            j = i + r        
            
            # 利用四边形不等式，把范围缩小为s[i][j-1]到s[i+1][j]
            i1 = solution[i][j-1]
            j1 = solution[i+1][j]
            # 首先取第一个k = i1
            m[i][j] = m[i][i1-1] + m[i1][j]
            # 用于解的追踪
            solution[i][j] = i1-1
            
            # 比较求最小的
            for k in range(i1+1,j1+1):
                temp = m[i][k-1] + m[k][j]
                
                if temp < m[i][j]:
                    m[i][j] = temp
                    solution[i][j] = k-1
            # min{m[i,k-1] + m[k,j] } + w[i,j]       
            m[i][j] += weight_i_j(b,i,j)
    
    return m,solution    
    
    

#arr = [5,3,4,1,3,2,3,4]
arr = [1000, 22, 13, 4, 5000, 86, 57, 18]
print(arr)
m,s = DynamicProgrammingSpeed(arr)
m1,s1 = DynamicProgramming(arr)
print(m)
print(end='\n')
print(m1)
print(end='\n')
print(s)
print(end='\n')
print(s1)
#%%