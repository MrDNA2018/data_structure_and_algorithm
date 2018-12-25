# -*- coding: utf-8 -*-

# 简单的插入排序
def insert_sort(arr,low,high):
    
    for i in range(low+1,high+1):
        temp = arr[i]
        j = i
        
        while arr[j-1] > temp and j >low:
            arr[j] = arr[j-1]
            j -=1
        arr[j] = temp
        
        
def group_sort_size_5(arr):
    
    # 我们是在arr上原地操作的
    # 下面是每5个一组
    low =0
    high = 4
    
    # 保存一下中位数数组，便于求中位数组的中位数
    # 此法相对于快排的规约，选择首元素或者随机选择，这个pivot是通过计算得出
    # 每5个分成一组，最后5的余数，特殊处理
    medium =[]
    while high < len(arr):
        insert_sort(arr,low,high)
        medium.append(arr[low+2])
        low +=5
        high +=5 
        
    insert_sort(arr,low,len(arr)-1)
    
    return arr,medium

def partion(arr,m_star,medium_num):
    
    # 因为没有足够的空位，所以临时放在list里，然后最后复制回去
    list = [-1]*(len(arr))
    # 小于pivot的指针，大于pivot的指针
    i =0
    j =len(arr)-1
    
    if medium_num == 0:
        left = arr[:len(arr)//2-1]
        right =arr[len(arr)//2:]
        return len(arr)//2-1,left,right
        
    
    # 先处理左边的数据，处理左上角
    for k in range(medium_num):
        #左上角可以直接放进左边
        # 理论上是直接把左上角放在head,右下角放在end,然后再处理左下角和右上角，以及最后的余数
        # 这样可以尽量保证有序，减少插入排序的工作量
        if arr[5*k + 2] < m_star:
            list[i]=arr[5*k + 2-2]
            i +=1
            list[i]=arr[5*k + 2-1]
            i +=1
            list[i]=arr[5*k + 2]
            i +=1

    # 处理中位数后面的分组，处理右下角
        # 从最后面开始处理，因为这里的数都比较大
        elif  arr[5*k + 2] > m_star:
            list[j]=arr[5*k + 2+2]
            j -=1
            list[j]=arr[5*k + 2+1]
            j -=1
            list[j]=arr[5*k + 2]
            j -=1
            
        else:
            # 处理中位数那一组上边，上面的放左边
            list[i]=arr[5*k + 2-2]
            i +=1
            list[i]=arr[5*k + 2-1]    
            i +=1

            # 处理中位数那一组，下面的放右边，为什么在这里了，因为他在大于pivot里面算是较小的，
            # 为了保证划分之后的子问题尽量有序，先下后上
            list[j] = arr[5*k + 2 +2]
            j -=1
            list[j] = arr[5*k + 2 +1]
            j -=1  
    
    # arr[medium[medium_num][1] 位置还不清楚最后添加
    
    # 处理左下角
    for k in range(medium_num):        
        # 左下角需要比较之后才能决定放左边还是右边，先上后下，上面的比较小
        if arr[5*k + 2] < m_star:
            if arr[5*k + 2 + 1] > m_star:
                list[j] = arr[5*k + 2 +1]
                j -=1
            else:
                list[i]=arr[5*k + 2 +1]
                i +=1
                
            if arr[5*k + 2 + 2] > m_star:
                list[j] = arr[5*k + 2 +2]
                j -=1
            else:
                list[i]=arr[5*k + 2 +2]
                i +=1            
        
        if arr[5*k + 2] > m_star:
            if arr[5*k + 2 - 1] > m_star:
                list[j] = arr[5*k + 2 -1]
                j -=1
            else:
                list[i]=arr[5*k + 2 -1]
                i +=1 
                
            if arr[5*k + 2 - 2] > m_star:
                list[j] = arr[5*k + 2 -2]
                j -=1
            else:
                list[i]=arr[5*k + 2 -2]
                i +=1 

    # 处理最后的余数
    for k in range(5*medium_num,len(arr)):

        if arr[k] > m_star:
            list[j] = arr[k]
            j -=1
        else:
            list[i]=arr[k]
            i +=1
            
    # 把最后的中位数放入       
    list[i] = m_star
    # 把临时结果放回原来的数组
    arr[:] = list[:]
    left = arr[:i]
    right =arr[i+1:]
    return i,left,right
    
    
def select_recursive(arr,k):
    if len(arr) == 1:
        return arr[0]
    
    if len(arr) >1:                    
        arr,medium = group_sort_size_5(arr)
        medium_num = len(medium)
#        print(medium_num)
        m_star = select_recursive(medium,medium_num/2-1)
        print("m_star",m_star)
        
        index,left,right = partion(arr,m_star,medium_num)
        print(arr[index],left,right)
        
        if k == index:
            return arr[index]
        
        elif k < index:
            return select_recursive(left,k)
        else:
            return select_recursive(right,k-index-1)
    
arr = [7,3,66,33,22,66,9,0,1,11,14,17,9,10,13,99,44,33,77,88,99,101,404,87,44,22,11,99,43,22]
print(arr)
a= sorted(arr)
print(a)
print(a[len(a)//2-1])
print(select_recursive(arr,len(arr)/2-1))
        
    
    