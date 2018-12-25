# -*- coding: utf-8 -*-

# 简单的插入排序
def insert_sort(arr,low,high,step):
    
    for i in range(low+step,high+1,step):
        temp = arr[i]
        j = i
        
        while arr[j-step] > temp and j >low:
            arr[j] = arr[j-step]
            j -=step
        arr[j] = temp

def group_sort_size_5(arr,left,right,step):
    
    # 我们是在arr上原地操作的
    # 下面是每5个一组
    low =left
    high = left +4*step
    
    # 保存一下中位数数组，便于求中位数组的中位数
    # 此法相对于快排的规约，选择首元素或者随机选择，这个pivot是通过计算得出
    # 每5个分成一组，最后5的余数，特殊处理
    while high <= right:
        insert_sort(arr,low,high,step)
        low +=5*step
        high +=5*step
    
    insert_sort(arr,low,right,step)

#li = [9,6,4,3,2,77,66,1,44]
#print(li)
#group_sort_size_5(li,1,len(li)-2,3)
#print(li)

#%%
#  规约子问题的方法：
# 按照每5个一组，在每组中位数里取中位数，然后把小于中位数的元素放在左边，大于的放在右边
def partion(arr,left,right,m_star):
    
    medium_num = (right-left +1)//5
    # 现在中位数为medium[medium_num],把小于medium[medium_num]放到左边
    
    # 因为没有足够的空位，所以临时放在list里，然后最后复制回去
    list = [-1]*(right-left +1)
    # 小于pivot的指针，大于pivot的指针
    i =0
    j =right-left
    
    if medium_num == 0:
        return (right-left)//2
        
    
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
    for k in range(5*medium_num,right+1):

        if arr[k] > m_star:
            list[j] = arr[k]
            j -=1
        else:
            list[i]=arr[k]
            i +=1
            
    # 把最后的中位数放入       
    list[i] = m_star
    # 把临时结果放回原来的数组
    arr[left:right+1] = list[:]
    return i



def select_recursive(arr,low,high,k,step):
    
    if low == high:
        return arr[low]
    
    if low < high:                    
        group_sort_size_5(arr,low,high,step)
        
        m_star = select_recursive(arr,low+2,((high-low +1)//5-1) * 5 +2,k,5)
        
        index = partion(arr,low,high,m_star)
        
        if k == index:
            return arr[index]
        
        elif k < index:
            return select_recursive(arr,low,index-step,k,step)
        else:
            return select_recursive(arr,index+step,high,k,step)
        
        
    
arr3 = [7,3,66,33,22,66,9,0,1,11,14,17,15,22,88,91,10,5,11,77,88,45,990,1]
print(arr3)
print(select_recursive(arr3,0,len(arr3)-1,len(arr3)//2-1,1))

a =sorted(arr3)
print(a)
print(a[len(arr3)//2-1])  