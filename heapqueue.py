# -*- coding: utf-8 -*-

# 最大堆

# 很显然这是一个双针模型,指着一对父子，父亲小于儿子，则儿子上位
def siftUp(arr,insert_index,insert_value):
    child_pointer = insert_index
    parent_pointer = (child_pointer-1)//2
    pivot = insert_value
    
    #儿子不断的挑战父亲
    while parent_pointer >=0 and arr[parent_pointer] < pivot:
        arr[child_pointer] = arr[parent_pointer]
        child_pointer = parent_pointer
        parent_pointer = (child_pointer-1)//2
    
    arr[child_pointer] = pivot

def siftDown(arr,insert_index,insert_value):
    end_index = len(arr)-1
    # 下沉也是双针模型，父亲每次和儿子里面最大的交换，逐步下沉
    parent_pointer = insert_index
    child_pointer = 2*parent_pointer + 1
    pivot = insert_value
    
    while child_pointer <= end_index:
        # child_pointer指针总是指向儿子里面最大的那个
        if child_pointer + 1 <= end_index and arr[child_pointer + 1] >arr[child_pointer]:
            child_pointer +=1
        # 假如父亲还是大于两个儿子，就没必要执行下沉操作
        if pivot >= arr[child_pointer]:
            break
        # 否则的话，和最大的儿子交换，逐步下沉，下沉时逐步更新父子指针
        else:
            arr[parent_pointer] = arr[child_pointer]
            parent_pointer = child_pointer
            child_pointer = 2*parent_pointer + 1
    # 把最后空出来的位置进去 ，最后肯定parent_pointer为空，child_pointer越界       
    arr[parent_pointer] = pivot
           

# 上浮构造的时候，就需要从头到尾上浮，每个元素浮一遍    
def buildHeapBySiftUp(arr):
    for i in range(len(arr)):
        siftUp(arr,i,arr[i])
# 下沉构造时，需要从尾到头构造，每个元素沉一遍，实际上至多需要沉一半，因为后面一半
# 元素都是叶子
def buildHeapBySiftDown(arr):
    for i in range((len(arr)-1)//2 -1,-1,-1):
        siftDown(arr,i,arr[i])
    
arr =[1,2,3,4,5,6]
buildHeapBySiftUp(arr)
print(arr)
siftDown(arr,0,0)
print(arr)
arr3=[0,1,2,3,4,5,6]
print(arr3)
buildHeapBySiftDown(arr3)
print(arr3)
