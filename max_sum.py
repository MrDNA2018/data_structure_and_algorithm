# -*- coding: utf-8 -*-
# 以下算法时间复杂度O(n^2)
def maxSum(arr):
    num = len(arr)
    # 记录最好的结果，这个结果是一个不断逼近的过程
    best_result_start =0
    best_result_end=0
    best_result =0
    # i为起始的指针，j为终止的指针，基于简单计算，起始位置不可能为负的，因为假如
    # 为负的，后移一位就会使结果变大
    for i in range(num):
        if arr[i] <0:
            continue
        else:
            cur_sum = arr[i]
            # j指针后移更新当前的求和
            for j in range(i+1,num):
                cur_sum +=arr[j]    
                # 假如当前求和大于当前的最好结果，就更新当前的最好结果
                if cur_sum > best_result:
                    best_result = cur_sum
                    best_result_start =i
                    best_result_end = j
                    
    return best_result,best_result_start,best_result_end

#%%
# 基于分治的做法，把数组分成两个部分，最优解出现的情况：要么在左半边，要么在右半边，
# 左边的尾部+右边头部       

# 针对起始为left,求最长字段和并返回，终止的标号        
def start_max(arr,left,right):
    cur_sum =0
    best_result =0
    best_result_end =0
    for i in range(left,right+1):
        cur_sum += arr[i]        
        if cur_sum > best_result:
            best_result = cur_sum
            best_result_end = i
    return best_result,best_result_end

# 针对起始为right,求最长字段和并返回，终止的标号 
def end_max(arr,left,right):
    cur_sum =0
    best_result =0
    best_result_end =0
    for i in range(right,left-1,-1):
        cur_sum += arr[i]        
        if cur_sum > best_result:
            best_result = cur_sum
            best_result_end = i
    return best_result,best_result_end          

# 递归的理解，一种直接看成递归到最底层，然后在最底层的处理，一种直接看成某一层直接把递归函数看成
# 你要用的变量
# 关于return和不return的理解，当你需要返回结果的时候就需要返回，在原来数组上操作的情况就可以不返回    
def maxSumSub(arr,left,right):
    # 递归的出口，也就是最小子问题的解
    if left == right:
        best_sum = max(0,arr[left])
        best_i = left
        best_j = right
    else:
        # 划分子问题的过程，一层层进入递归，子问题不断划分，divide
        mid = left + (right-left)//2

        # 针对子问题处理，此时三个子问题
        # 最优解在左边
        left_max,left_i,left_j = maxSumSub(arr,left,mid)
        # 最优解在右边
        right_max,right_i,right_j = maxSumSub(arr,mid+1,right)
        # 最优解出现在左边的尾部+右边头部，最优解和起止位置
        best_left,best_i = end_max(arr,left,mid)
        best_right,best_j =start_max(arr,mid+1,right)
        best_sum =  best_left+ best_right
        
        # 最优解取三者中的最大值
        if best_sum < left_max:
            best_sum = left_max
            best_i = left_i
            best_j = left_j            
        if best_sum < right_max:
            best_sum = right_max
            best_i = right_i
            best_j = right_j  
    
    return best_sum,best_i,best_j

#%%
# 动态规划的算法，状态方程，初始值 
# 如何划分子问题比较好了，看成选择问题，选与不选，从尾部开始，i选的话，最大值就是end_max前面
# n-1个元素的最大值+arr[i],不选的话就是前面n-1个元素求最小字段和
# 这个工作量好大，问题规模缩小了1，然后干了分治算法一层的工作量
# 所以这种规约子问题的方案不好？
# 最大字段结束在j,那么原问题的解就是j=0,1,2..len(arr)-1
# 这么多情况里面的最大值，
# 我们定义b[j]为结束在j字段和最大值，max{b[j]} 0<=j<=len(arr)-1
# 我们只要求出了每一个b[j],最大值就是可以从里面求出来了
# 那么b如何求解了,结束在j的最大字段和，假如前面j-1最大字段和小于0的话，那就是arr[j]
# 状态方程为：b[j] = max{b[j-1]+arr[j],arr[j]}
# 这里不需要考虑arr[j]是否大于0，因为我的子问题就是定义的是结束在j的最大字段和，至于
# 最终的解是结束在不同的j上的最大字段和的最大值。

# 这个方法可以知道结束位置j,没法知道起始位置i为多少啊    
def maxSumDynamicProgramming(arr):
    # 本来是需要一个数组来记录b的，然后找b[]里面的最大值
    # 但是我们得到一个b,就可以更显最优结果的，我只要记录当前最优解就行了，所以只需要当前的b
    # b的初值就是b[0-1]的值，也就是没有元素时最大字段和为多少，为0
    cur_b =0
    
    # 用于记录最优的结果
    best_result = 0
    best_j = -1
    # 根据状态方程自底向上完成
    for j in range(len(arr)):
        # b[j] = max{b[j-1]+arr[j],arr[j]}，当b[j-1]>0为左边，否则为右边，也可以直接用max
        if cur_b>0:
            cur_b += arr[j]
        else:
            cur_b = arr[j]
        
        # 每求出一个b,就更新一下当前最优解
        if cur_b >= best_result:
            best_result = cur_b
            best_j = j
    return best_result,best_j
         
#%%
import numpy as np
# 处理矩阵，把arr[i1:i2+1,:]转换成一维数组，也就是把每一列的从i1到i2相加
def matrixSumByRow(arr,i1,i2,n):
    li = [0]*n
    for j in range(n):
        for i in range(i1,i2+1):
            li[j] +=arr[i][j]
    return li

def maxSumOrder2(arr):
    # 获取矩阵的行列
    row,column = arr.shape
    # 初始化左右结果，best_j1由于一维最大子段和没有实现，这里也没有
    best_result = 0
    best_i1 = -1
    best_i2 = -1
    best_j2 = -1
    # 原问题max{t(i1,i2)}，1<=i1<=i2<=m，遍历所有的t(i1,i2)
    for i1 in range(row):
        for i2 in range(i1,row):
            # matrixSumByRow(arr,i1,i2,column)把arr[i1:i2+1,:]转换成一维数组
            # 求出这个一维数组的最大字段和，这个是原问题的一个可行解
            t_i1_i2,j2 = maxSumDynamicProgramming(matrixSumByRow(arr,i1,i2,column))
            # 如果可行解优于当前的最优解，更新为当前最优解
            if t_i1_i2 > best_result:
                best_result = t_i1_i2
                best_i1 = i1
                best_i2 = i2
                best_j2 = j2
                
    return best_result,[best_i1,best_i2,-1,best_j2]
            
arr = np.full((5,5),-1)
arr[1][1] = 4
arr[1][3] = 4
arr[3][1] = 4
arr[3][3] = 4
print(arr)
print(maxSumOrder2(arr))

#%%
import numpy as np
def maxMSum(arr,m):
    n = len(arr)
    b = np.zeros((m+1,n+1),int)
    
    for i in range(1,m+1):
        # (i,n+1-m+i),本来是(i,n+1），可以发现有些没有必要计算，
        # 因为[i][j]总是取左边或者左上的数据     
        for j in range(i,n+1-m+i):
            # 最后刚好子段个数==元素个数时，就是相当于一个元素一个子段
            # 边界时，需要保证一个元素一个子段，不能直接取左边和左上角最大值
            if j == i:
                b[i][j] = b[i-1][j-1] + arr[j-1]       
            # 其他的情况需要按照状态方程比较
            else:
                # 第一种情况
                b[i][j] = b[i][j-1] + arr[j-1]
                # 第二种情况
                for k in range(i-1,j):
                    if b[i-1][k] + arr[j-1] > b[i][j]:
                        b[i][j] = b[i-1][k] + arr[j-1]
    # 最后一行都是可行解，取最大为最优解
    return b,max(b[m][:])


def maxMSum_opt(arr,m):
    n = len(arr)
    b = [0]*(n+1)
    # 数组c专门记录max{b(i-1,k)} ，c[j-1]代表k从i-1到j-1里面最大值，需要初始化
    # 参考b的第0行可以得到c的初始化如下
    c= [0]*(n+1)
    
    for i in range(1,m+1):
        # 先把第一个元素处理一下，也就是j == i，我们只使用一个一维的滚动数组
        b[i] = b[i-1] + arr[i-1]
        # 我们需要一个变量记录当前一行的到当前位置的最大值
        cur_max = b[i]
        
        # (i,n+1-m+i),本来是(i,n+1），可以发现有些没有必要计算，
        # 因为[i][j]总是取左边或者左上的数据     
        # 第一个元素上面已经处理了
        for j in range(i+1,n+1-m+i):
            # 获取b[j]当前的值
            b[j] = max(b[j-1],c[j-1]) + arr[j-1]
            # c[j-1] 使用了之后，就要更新c[j-1]留给下一层使用，值为还未更新的cur_max
            c[j-1] = cur_max
            # 更新后的cur_max要放在c[j]，但是旧的c[j]还没使用了，所以c[j]的更新是滞后一步的
            if cur_max <  b[j]:
                cur_max = b[j]
        # 我们会发现内存循环完了，最后的cur_max还没更新到c里面，因为c的更新是滞后一步
        # 得再次进入循环才能更新的，注意这里c的标号
        c[n-m+i] = cur_max
           

    # 最后一行都是可行解，取最大为最优解
    return b,max(b[:])


arr = [-2,11,-4,-4,13,-5,-2,1,1,5,8,-1]
print(maxMSum(arr,3))                
            
        
