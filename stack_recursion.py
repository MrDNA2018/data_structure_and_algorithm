# -*- coding: utf-8 -*-


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

class guide:
    def __init__(self,left =None,right =None):
        self.left =left
        self.right =right
        
        
def quick_sort(arr):
    stack =[guide(0,len(arr)-1),]
    
    while stack:
        # 弹出子问题
        pointer = stack.pop()
        # 划分子问题，这个是必须操作，划分子问题操作，把对原问题的访问隐含在里面
        index = partition(arr,pointer.left,pointer.right)
        
        # 以下是操作的处理，快排在划分子问题之后，只有一个操作，访问子问题
        # 按照逆序放入栈
        if index+1 <= pointer.right:
            stack.append(guide(index+1,pointer.right))
        if pointer.left <= index-1:
            stack.append(guide(pointer.left,index-1))
            
# 如下是针对两个已排序的数组合并成一个有序数组的排列方法，为最基本的双针模型    
def MergeArry(arr,left,right):
    i =left
    middle = left + (right-left)//2
    j =middle +1
    result =[]
    while i <= middle and j <= right:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i +=1
        else:
            result.append(arr[j])
            j += 1
    
    result += arr[i:middle+1]
    result += arr[j:right+1]
    arr[left:right+1] = result[:]
    
def MergeSort(arr,left,right):
    # 递归出口，出口需要返回当前的那个数
    if left == right:
        return 
    
    # 以下当作某一层的处理
    middle = left + (right-left)//2
    # 获取待排序的两个已排序的数组
    MergeSort(arr,left,middle)
    MergeSort(arr,middle+1,right)
    MergeArry(arr,left,right)
        
    # 返回已排序的结果，用于上一层获取待排序的有序数组

class path:
    def __init__(self,left =None,right=None,opt =None):
        self.left =left
        self.right = right
        # True是处理子问题，False为合并
        self.opt =opt
        
def MergeSort2(arr):
    stack =[path(0,len(arr)-1,True),]
    
    while stack:
        # 弹出子问题
        pointer = stack.pop()
        # 子问题的划分，这个是必须的操作，首先是划分子问题
        middle = pointer.left + (pointer.right-pointer.left)//2
        
        # 归并排序有两个操作：一是访问子问题，二是合并原问题，为了操作方便，改写了函数原地操作
        # 如果操作是访问子问题
        if pointer.opt:
            # 对于一个问题,先解决左子问题，再解决右子问题，再把两个子问题合并，逆序放入
            if pointer.left<pointer.right:
                stack.append(path(pointer.left,pointer.right,False))                
                stack.append(path(middle+1,pointer.right,True))
                stack.append(path(pointer.left,middle,True))
        # 如何操作是合并，就执行合并操作
        else:
            MergeArry(arr,pointer.left,pointer.right)
            
arr = [1,9,11,12,4,5,6,7,99]
MergeSort2(arr)
print(arr)
        
        
        
    
    