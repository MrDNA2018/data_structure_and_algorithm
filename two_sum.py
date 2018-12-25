# -*- coding: utf-8 -*-

# 双针模型，蛮力算法，时间复杂度O(n^2)
def twoSum_two_pointer(arr,target):
    n = len(arr)
    # i为第一个数的位置，j为第二个数的位置
    for i in range(n-1):
        rest = target - arr[i]
        for j in range(i+1,n):
            if arr[j] == rest:
                return True,[arr[i],rest]
    
    return False

# 利用有序的数组，寻找第二个数时，可以使用二分查找法为logn,整个时间复杂度为O(nlogn)
def twoSum_sorted_binary_Serach(arr,target):
    n = len(arr)
    # 排序O(nlogn)
    arr = sorted(arr)
    
    # 二分查找，logn
    def binary_Serach_recursive(arr,left,right,target):
        
        middle = (left + right) // 2
        # 递归出口
        if left > right :
            return False
        
        if arr[middle] == target:
            return True
                
        elif arr[middle] < target:
            # 这里没有return的话，结果就没法return出来
            return binary_Serach_recursive(arr,middle+1,right,target)
            
        else:
            return binary_Serach_recursive(arr,left,middle-1,target)
    
    # 遍历第一个数，查询第二个数
    for i in range(n-1):
        rest = target - arr[i]
        if binary_Serach_recursive(arr,i+1,n-1,rest):
            return True,[arr[i],rest]
         
    return False
#%%
# python里面set使用的是哈希方式实现，查找时间复杂度O(1)，整体时间复杂度O(n)       
def twoSum_hash(arr,target):
    n = len(arr)
    # 哈希表
    visit = set()
    
    # 遍历第一个数，查询第二个数是否在哈希表里
    for i in range(n):
        rest = target - arr[i]
        if rest in visit:
            return True,[arr[i],rest]
        # 假如这个数不再哈希表里，就添加到哈希表里面，这种操作步骤，已经保证
        # 任意两个数都组合过
        # 当遇到ab比较，ba就没必要比较时，指针对应的就是i,j =i+1,而在哈希里，对应的
        # 就是逐步加入元素
        visit.add(arr[i])
    
    return False

arr = [16,7,8,44,2,4,5,97,5,3]
print(twoSum_hash(arr,100))
print(twoSum_two_pointer(arr,100))
print(twoSum_sorted_binary_Serach(arr,100))
#%%
import numpy as np
def kSum(arr,target,k):
    n = len(arr)
    
    dp = np.full((n+1,k+1,target+1),False)
    
    # 初始化,为可能性问题，也就是最后必须k和target都用完了，才是最后的解
    # 不能使用dp[:][0][0] = True,这两个的赋值不一样，这里是一个容易出错的地方
    for i in range(n+1):
        dp[i][0][0] = True
    
    for i in range(1,n+1):
        for j in range(1,k+1):
            # 这里是一个剪枝，假如k小于元素个数就没有必要考虑了
            if j <= i:
                for l in range(1,target+1):
                    # 注意边界，假如l-arr[i-1]<0，就没有意义了，只能取左边
                    if l-arr[i-1] >=0:
                        dp[i][j][l] = dp[i-1][j][l] or dp[i-1][j-1][l-arr[i-1]]
                    else:
                        dp[i][j][l] = dp[i-1][j][l]
                                        
    return dp[n][k][target]
                   
    
arr = [16,7,8,44,2,4,5,97,5,3]
print(kSum(arr,99,3))
print(kSum(arr,102,3))