# -*- coding: utf-8 -*-

# 寻找变化,要求返回arr第一个1的位置

def binarySearch(arr,left,right):
        
    if left < right:
        mid = left + (right - left ) //2
        
        if arr[mid] == 0:
            # 这个是递归的出口之一
            if arr[mid +1] == 1:
                return mid + 1
            else:
                return binarySearch(arr,mid +1,right)
            
        else:
            # 这个是递归的出口之一
            if arr[mid -1] == 0:
                return mid
            else:
                return binarySearch(arr,left,mid-1)

# 还有一种思路mid = left + (right - left ) //2
# arr[mid] =0是处理[mid-1:right]
# arr[mid] =1 时处理[left:mid+1]
# 这个的含义就是:剩下处理的数组里总是含有0和1，最后剩余2个时，就是01
def binarySearch2(arr,left,right):
    
    if left + 1 == right:
        index = right
        
    else:
        mid = left + (right - left ) //2
        
        if arr[mid] == 0:
            index = binarySearch(arr,mid,right)
            
        else:
            index = binarySearch(arr,left,mid)

    return index            

def binarySearchRecursive(arr):
    left =0
    right = len(arr) -1
    
    if arr[0] == 1 or arr[-1] == 0 or not arr:
        return -1
    
    # 不会出现left =right,因为在这之前，已经找到了，提前退出了
    # 循环体条件，有一种形式靠break退出循环
    while left < right:
        # 取中位数
        mid = left + (right - left ) //2
        # 中位数为0，判断一下，01直接退出，00的话处理右边
        if arr[mid] == 0:
            if arr[mid +1] == 1:
                index = mid + 1
                break
            else:
                left = mid +1   
        # 中位数为1，判断一下，01的话退出，11的话处理左边
        else:
            if arr[mid -1] == 0:
                index = mid
                break
            else:
                right = mid-1
                
    return index
        
                

arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]
left =0
right = len(arr)-1
print(binarySearch(arr,left,right))
print(binarySearchRecursive(arr))
print(binarySearch2(arr,left,right))

