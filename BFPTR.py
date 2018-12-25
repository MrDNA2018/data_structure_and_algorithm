# -*- coding: utf-8 -*-

# 简单的插入排序
def insert_sort(arr,low,high):
    # 指针i,代表第几次插入，第0次，就默认首元素放入有序列表
    # 从第1次开始，拿一个元素放入有序列表，或者理解为拿原数组里面
    # 第i个元素放入有序数组，在这里是原地操作的，要么使用交换，要么
    # 先拿出一个元素在空中，数组里面就流出了一个空位
    for i in range(low+1,high+1):
        # 把第i个元素拿起，暂时放在空中
        temp = arr[i]
        # 指针j是从尾部扫描已排列的有序数组，注意有序列表是从小到大排列的
        # j一直都是指在空闲的位置的
        j = i
        
        # 遇到比空中的元素大的元素，大的元素后移一位，移到空出来的那个位置
        # 此时就又空出来一个位置，更新空闲的位置j,...直到碰到比空中的元素小的元素
        # 空中元素的位置就找到了，就是现在j指的空闲位置
        while arr[j-1] > temp and j >low:
            arr[j] = arr[j-1]
            j -=1
        # 把空中元素放入空闲位置
        arr[j] = temp

# 这个一个可以准确找到中位数的算法？显然不是的这个只是大概找中位数的方法，而且还有一个
# 致命的问题，只是找到中位数了，标号还要搜索
# 然后此时的数组是有结构规律的，划分数组的时候使用的是快排的划分，没有用到这里面
# insert_sort排序产生的局部有序的特征，改进优化方法：在找中位数组中位数的过程中
# 想办法记录下来，哪些数据必定小于中位数的在左上方，那些数据必定大于中位数在右下方，
# 以及不确定的那一块
def findMid(arr,low,high):
###############################################################################
# Divide
###############################################################################    
    # 这里的两个指针为每个小分组的头和尾，也可以只用一个指针
    left = low
    right = low+4
    # count指的是中位数数组的指针
    count = 0
    
    # 当小数组的尾指针小于等于右边界限时，对每个小组排序，得到每个小组的中位数
    
    while right <= high:
        insert_sort(arr,left,right)
        # 因为中位数是分散的步长为5，对于我来说不好处理，所以此时处理时把中位都放在数组的
        # 前面，这样下一轮时就比较好处理了，但是这样处理，就破坏了数组有序的规律，让最后
        # 无法利用数组的有序规律来划分数据，这里可以优化
        arr[low + count],arr[left +2] = arr[left +2],arr[low + count]
        # 处理下一组
        left +=5
        right +=5
        # 记得更新中位数数组的指针
        count +=1
    
    # 当跳出循坏时，就需要处理余数，或者没有进入循环，也要处理余数
    # 把余数排序，获取中位数，加入到中位数列表
    if left <=high:
        insert_sort(arr,left,high)
        arr[low + count],arr[left+(high-left)//2] = arr[left+(high-left)//2],arr[low + count]
        count +=1
        
    # 以上过程是这个问题划分子问题的过程，也就是partion的过程，也就是把问题规模n变成
    # n//5的过程。
###############################################################################
# Conquer
###############################################################################
    #获取到中位数数组，得到了子问题，下面就考虑治conquer了
    # 第一种情况，数组没有经过5分组，排序后直接到这里，直接返回在首位的中位数，这种情况下count=1
    # 当进入了5分组没有进入余数处理，这时count=1，也应该是返回首元素
    # 其他情况count>=0时，这两个元素还没有排序，所以要进入下一轮排序一下，变成count=1输出首元素
    # count就是low>high的情况，直接返回空
    if count ==0:
        return
    if count ==1:
        return arr[low]
    else:
        # 注意count是指中位数元素的数量，对应数组上的指针需要-1
        return findMid(arr,low,low+count-1)

#标号需要通过检索得到
def findIndex(arr,mid):
    for i in range(len(arr)):
        if arr[i] == mid:
            return i
        
def partion_with_index(arr,low,high,index):
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
    
    arr[low],arr[index] = arr[index],arr[low]
    return partition(arr,low,high)


def BFPTR(arr,low,high,k):
########################################################################
    # divide
########################################################################
    # 首先获取mid
    mid = findMid(arr,low,high)
    # 获取此时mid的index
    mid_index = findIndex(arr,mid)
    # 根据mid来划分数据，返回的是中间的index（就是排序后最终的位置）
    index =partion_with_index(arr,low,high,mid_index)
#######################################################################
    # Conquer
########################################################################    
    #根据index做出子问题的处理
    if index == k:
        return arr[index]
    elif index > k:
        return BFPTR(arr,low,index-1,k)
    else:
        return BFPTR(arr,index+1,high,k)
        
    
    
arr3 = [7,3,66,33,22,66,9,0,1,11,14,17,9,10,13,99,44,33,77,88,99,101,404,87,44,22,11,99,43,22]
print(sorted(arr3))
print(BFPTR(arr3,0,len(arr3)-1,(len(arr3)-1)//2-1))