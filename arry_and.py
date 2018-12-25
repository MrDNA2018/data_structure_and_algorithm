# -*- coding: utf-8 -*-

def sortTwoSortedArry(a,b):
    b_num = len(b)
    a_num = len(a)-b_num
    
    li = []
    i ,j =0,0
    # 双针模型从左往右扫描，终止条件是，只要任意一个数组走完了，
    # 走完了没有完的那个数组直接接上就行了
    while i<a_num and j <b_num:
        if a[i] <= b[j]:
            li.append(a[i])
            i +=1
        if b[j] < a[i]:
            li.append(b[j])
            j +=1
    # 没走完的直接把尾巴接上去
    li += a[i:a_num]
    li += b[j:b_num]    
    return li

def sortTwoSortedArry_in_place(a,b):
    b_num = len(b)
    total_num = len(a)
    a_num = total_num-b_num
    
    # 原地方式，就需要倒着放，这个也是比较一般的思路
    # 原地操作一般想法，一是，取出一个元素放在空中，留出一个空
    # 二是纯粹通过交换来实现
    # 三是，哪里有空位就往哪里放，倒着放是一种思路
    
    # 指向数组a的数组
    i = a_num-1
    # 指向数组b
    j = b_num-1
    # 最终结果的指针
    k = total_num-1
    
    while i >=0 and j>=0:
        if a[i] >= b[j]:
            a[k] = a[i]
            i -=1
            k -=1
            
        if b[j] > a[i]:
            a[k] = b[j]
            j -=1
            k -=1 
    # 把尾巴接上
#    a[:i+1] = a[:i+1]
    a[:j+1] = b[:j+1]
    
a = [4,5,6,9,0,0,0]
b = [1,2,3]
print(sortTwoSortedArry(a,b))
print(a)
sortTwoSortedArry_in_place(a,b)
print(a)

