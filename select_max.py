# -*- coding: utf-8 -*-

# 这个已经是最优的算法了，比较n-1次
def findMax(arr):
    max_pivot = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] > max_pivot:
            max_pivot = arr[i]
    
    return max_pivot

def findMin(arr):
    min_pivot = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] < min_pivot:
            min_pivot = arr[i]
    
    return min_pivot

# 两两比较得到最大的一半数组
def partition_max(arr):
    
    pointer = 0
    max_arr =[]
    
    while pointer <= len(arr)-2:
        max_arr += [max(arr[pointer],arr[pointer+1])]
        pointer +=2
    # 假如是奇数，加上最后一个数，偶数的话加的为空   
    max_arr +=arr[pointer:]
    
    return max_arr

# 找最大分治的写法，也是最优的为比较n-1次
def findmax_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    
    max_arr = partition_max(arr)
    return findmax_recursive(max_arr)

# 找最大和最小，得到最大一半分组和最小的一半分组
def partition_max_min(arr):
    
    pointer = 0
    max_arr =[]
    min_arr =[]
    
    while pointer <= len(arr)-2:
        if arr[pointer] >=arr[pointer+1]:
            max_arr.append(arr[pointer])
            min_arr.append(arr[pointer+1])
        else:
            max_arr.append(arr[pointer+1])
            min_arr.append(arr[pointer])
            
        pointer +=2
        
    max_arr +=arr[pointer:]
    min_arr +=arr[pointer:]
    
    return max_arr,min_arr

# 这个也是最优的算法了
def findMaxMin(arr):
    max_arr,min_arr = partition_max_min(arr)
    min = findMin(min_arr)
    max = findMax(max_arr)
    
    return max,min

#%%
class node:
    def __init__(self,value=None,miss=None):
        self.value = value
        self.miss =miss
    
def partition_max_with_nodes(arr):
    
    pointer = 0
    max_arr =[]
    
    while pointer <= len(arr)-2:
        if arr[pointer].value >=arr[pointer+1].value:
            
            arr[pointer].miss.append(arr[pointer+1].value)
            max_arr.append(arr[pointer])
        else:
            arr[pointer+1].miss.append(arr[pointer].value)
            max_arr.append(arr[pointer+1])
            
        pointer +=2
    # 假如是奇数，加上最后一个数，偶数的话加的为空   
    max_arr +=arr[pointer:]
    
    return max_arr
    
def findMaxSecondmax(arr):
    arr_node =[]
    for i in range(len(arr)):
        arr_node.append(node(arr[i],[]))
        
    def findmax_recursive(arr):
        if len(arr) == 1:
            return arr[0]
        
        max_arr = partition_max_with_nodes(arr)
        return findmax_recursive(max_arr)
    
    pair = findmax_recursive(arr_node)
    
    first_max = pair.value
    second_max_arr = pair.miss
    
    second_max = findMax(second_max_arr)
    return first_max,second_max
        

arr = [4,44,5,77,8,32,18,99,377,55,33,11,12,999,678]
print(arr)
##print(findMax(arr))
##print(partition_max(arr))
##print(findmax_recursive(arr))
#print(partition_max_min(arr))
#print(findMaxMin(arr))
print(findMaxSecondmax(arr))
#%%

import random        
def randomizedPartition(arr,low,high):
    def partition(arr,low,high):
        # 这时另外一种考虑方式，而且他是不需要额外空间的，他只使用一个指针来区分小于基准和大于基准的
        # pointer_less_than代表这个指针的左边全部都是小于基准的（包括自己，不包括首元素）
        # 然后从左往右扫描，遇到小于基准的元素，就把小于基准元素区域的后面紧接着的一个元素和他交换
        # 那么小于基准元素区域就多了一个元素，。。。就这样小于基准的元素就连在了一起
        # 首元素是基准元素，小于基准元素区域块，大于基准元素区域块，现在分成了三个部分
        # 把首元素和小于基准元素区域块最后一个元素交换，那三部分就变成，小于的，基准，大于的
        
        # 刚开始小于基准的元素为0，暂且指向首位值
        pointer_less_than = low
        # 然后一次扫描后面所有元素
        for i in range(pointer_less_than +1,high+1):
            # 遇到小于基准的，就把小于基准元素区域的后面紧接着的一个元素和他交换，小于的块相当于也更新了
            if arr[i] < arr[low] :
                pointer_less_than +=1
                arr[pointer_less_than],arr[i]=arr[i],arr[pointer_less_than]
        #  把首元素和小于基准元素区域块最后一个元素交换，那三部分就变成，小于的，基准，大于的       
        arr[low],arr[pointer_less_than] = arr[pointer_less_than],arr[low]
        
        return pointer_less_than
    
    index = random.randint(low,high)
    arr[low],arr[index]=arr[index],arr[low]
    return partition(arr,low,high)

def randomizedQuicksort_for_medium(arr,low,high,k):
     
    if low <= high:
        index = randomizedPartition(arr,low,high)
        if k == index:
            return arr[index]
        elif k < index :            
            return randomizedQuicksort_for_medium(arr,low,index-1,k)
        else:
            return randomizedQuicksort_for_medium(arr,index+1,high,k)


arr3 = [7,3,66,33,22,66,99,0,1]
print(arr3)
print(sorted(arr3))
print(randomizedQuicksort_for_medium(arr3,0,len(arr3)-1,4))


#%%

# 简单的插入排序
def insert_sort(arr,low,high):
    
    for i in range(low+1,high+1):
        temp = arr[i]
        j = i
        
        while arr[j-1] > temp and j >low:
            arr[j] = arr[j-1]
            j -=1
        arr[j] = temp

# 针对已分组的数据块排序
def insert_sort_node(arr,low,high):
    
    for i in range(low+1,high+1):
        temp = arr[i]
        j = i
        
        while arr[j-1][0] > temp[0] and j >low:
            arr[j] = arr[j-1]
            j -=1
        arr[j] = temp

#  规约子问题的方法：
# 按照每5个一组，在每组中位数里取中位数，然后把小于中位数的元素放在左边，大于的放在右边
def partion_group_sort_size_5(arr,left,right):
    
    # 我们是在arr上原地操作的
    # 下面是每5个一组
    low =left
    high = left +4
    
    # 保存一下中位数数组，便于求中位数组的中位数
    # 此法相对于快排的规约，选择首元素或者随机选择，这个pivot是通过计算得出
    # 每5个分成一组，最后5的余数，特殊处理
    medium =[]
    if right -left > 4:
        while high <= right:
            insert_sort(arr,low,high)
            medium.append((arr[low+2],low+2))
            low +=5
            high +=5
    
    # 假如输入刚好为5个或者少于5个，直接插入排序，返回最中间的index
    # 插入排序对已有序大的序列，效率高，在次情况下，比较次数很少
    # 这种情况下直接返回中位数的标号
    else:
        insert_sort(arr,low,high)
        return (low+high)//2 -1
    

    # 对中位数数组排序，取得中位数，也就是分解子问题的pivot
    insert_sort_node(medium,0,len(medium)-1)

    # 把小于pivot的数据放左边，把大于pivot数据放右边
    # 分组里面的左上角可以直接放在前后和右下角的数据可以直接放在后面
    # 左下角和右上角，以及最后的余数需要比较之后，再决定放左边还是右边
    medium_num = (len(medium) -1)//2
    # 现在中位数为medium[medium_num],把小于medium[medium_num]放到左边
    
    # 因为没有足够的空位，所以临时放在list里，然后最后复制回去
    list = [-1]*(right-left +1)
    # 小于pivot的指针，大于pivot的指针
    i =0
    j =right-left
    
    # 先处理左边的数据，处理左上角
    for k in range(medium_num):
        #左上角可以直接放进左边
        # 理论上是直接把左上角放在head,右下角放在end,然后再处理左下角和右上角，以及最后的余数
        # 这样可以尽量保证有序，减少插入排序的工作量
        list[i]=arr[medium[k][1]-2]
        i +=1
        list[i]=arr[medium[k][1]-1]
        i +=1
        list[i]=arr[medium[k][1]]
        i +=1

    # 处理中位数后面的分组，处理右下角
    for k in range(len(medium)-1,medium_num,-1):
        # 从最后面开始处理，因为这里的数都比较大
        list[j]=arr[medium[k][1]+2]
        j -=1
        list[j]=arr[medium[k][1]+1]
        j -=1
        list[j]=arr[medium[k][1]]
        j -=1

    # 处理中位数那一组上边，上面的放左边
    list[i]=arr[medium[medium_num][1]-2]
    i +=1
    list[i]=arr[medium[medium_num][1]-1]    
    i +=1

    # 处理中位数那一组，下面的放右边，为什么在这里了，因为他在大于pivot里面算是较小的，
    # 为了保证划分之后的子问题尽量有序，先下后上
    list[j] = arr[medium[medium_num][1] +2]
    j -=1
    list[j] = arr[medium[medium_num][1] +1]
    j -=1  
    
    # arr[medium[medium_num][1] 位置还不清楚最后添加
    
    # 处理左下角
    for k in range(medium_num):        
        # 左下角需要比较之后才能决定放左边还是右边，先上后下，上面的比较小
        if arr[medium[k][1] + 1] > medium[medium_num][0]:
            list[j] = arr[medium[k][1] +1]
            j -=1
        else:
            list[i]=arr[medium[k][1] +1]
            i +=1
            
        if arr[medium[k][1] + 2] > medium[medium_num][0]:
            list[j] = arr[medium[k][1] +2]
            j -=1
        else:
            list[i]=arr[medium[k][1] +2]
            i +=1            
        
    # 处理右上角        
    for k in range(len(medium)-1,medium_num,-1):        
        if arr[medium[k][1] - 1] > medium[medium_num][0]:
            list[j] = arr[medium[k][1] -1]
            j -=1
        else:
            list[i]=arr[medium[k][1] -1]
            i +=1 
            
        if arr[medium[k][1] - 2] > medium[medium_num][0]:
            list[j] = arr[medium[k][1] -2]
            j -=1
        else:
            list[i]=arr[medium[k][1] -2]
            i +=1 

    # 处理最后的余数
    for k in range(low,right+1):

        if arr[k] > medium[medium_num][0]:
            list[j] = arr[k]
            j -=1
        else:
            list[i]=arr[k]
            i +=1
            
    # 把最后的中位数放入       
    list[i] = medium[medium_num][0]
    # 把临时结果放回原来的数组
    arr[left:right+1] = list[:]
    # 返回中位数的index
    return(left+i)

# 使用分治获取中位数
def partion_group_sort_size_5_for_medium(arr,low,high,k):
        
    # 递归出口，当左右指针重合时，便是找到了第k小的数组
    if low <= high:
        # 取经过计算的pivot分组，这个pivot 的index应该接近中位数的index，这样就可以很快的收敛
        index = partion_group_sort_size_5(arr,low,high)
        # 这个index恰好为中位数的index时，就可以直接返回中位数大小
        if k == index:
            return arr[index]
        # 当index>k时，代表在左半部分
        elif k < index :            
            return partion_group_sort_size_5_for_medium(arr,low,index-1,k)
        # 否则就在右半部分
        else:
            return partion_group_sort_size_5_for_medium(arr,index+1,high,k)        
    
            
    
arr3 = [7,3,66,33,22,66,9,0,1,11,14,17,15,22,88,91,10,5,11,77,88,45,990,1]
print(arr3)
print(partion_group_sort_size_5_for_medium(arr3,0,len(arr3)-1,len(arr3)//2-1))

a =sorted(arr3)
print(a)
print(a[len(arr3)//2-1])  
        