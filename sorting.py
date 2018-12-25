# -*- coding: utf-8 -*-
#%%
class Sorting(object):
    def insertionSorting(self, arry):
        for i in range(1,len(arry)):
            x = arry[i]
            j = i-1
            while j >=0 and x < arry[j]:
                arry[j+1] = arry[j]
                j -=1
            arry[j+1] = x
            
        return arry
    
    def insertionSorting2(self, arry):        
        def insert_last_sorted_arrys(arry,n):
            x = arry[n]
            j = n-1
            while j >=0 and x < arry[j]:
                arry[j+1] = arry[j]
                j -=1
            arry[j+1] = x
            
        def insert_recursion_Sorting(arry,n):
            if n == 1:
                return
            insert_recursion_Sorting(arry,n-1)            
            insert_last_sorted_arrys(arry,n-1)
            
        insert_recursion_Sorting(arry,len(arry))
        
    
    def selectSorting(self, arry):
        for i in range(len(arry)):
            min_index = i
            for j in range(i+1,len(arry)):
                if arry[min_index] > arry[j]:
                    min_index = j
                    
            arry[min_index],arry[i] = arry[i],arry[min_index]
            
        return arry
    

    def bubbleSorting(self,arry):
        for i in range(len(arry)-1):
            swap = False
            for j in range(len(arry)-2-i):
                if arry[j] > arry[j+1]:
                    arry[i],arry[j+1] = arry[j+1],arry[j]
                    swap = True
            if not swap:
                break
        return arry
    
    def quickSorting(self,arry):
        def qsort_rec(arry,start,end):      
            if start >= end:
                return 
            i = start
            j = end
            pivot = arry[start]
            while i<j:
                while i<j and arry[j] >= pivot:
                    j -=1
                if i<j:
                    arry[i] = arry[j]
                    i +=1
                while i<j and arry[i] <= pivot:
                    i +=1
                if i<j:
                    arry[j] = arry[i]
                    j -=1
            arry[i] = pivot
            qsort_rec(arry,start,i-1)
            qsort_rec(arry,i+1,end)
            
        qsort_rec(arry,0,len(arry)-1)

    def quickSorting2(self,arry):
        def qsort_rec(arry,start,end):
            
            if start >= end:
                return
            
            i = start           
            for j in range(start+1,end+1):
                if arry[j] < arry[start]:
                    i +=1
                    arry[i],arry[j] = arry[j],arry[i]
            arry[i],arry[start] = arry[start],arry[i]
            qsort_rec(arry,start,i-1)
            qsort_rec(arry,i+1,end)
            
        qsort_rec(arry,0,len(arry)-1)
        
    def quickSorting3(self,arry):
        
        def partition(arry,start,end):
            i = start           
            for j in range(start+1,end+1):
                if arry[j] < arry[start]:
                    i +=1
                    arry[i],arry[j] = arry[j],arry[i]
            arry[i],arry[start] = arry[start],arry[i]
            return i
        
        stack =[0,len(arry)-1,]
        
        while stack:
            end = stack.pop()
            start = stack.pop()
            pivot = partition(arry,start,end)
            
            if start < pivot-1:
                stack += [start]
                stack += [pivot-1]
                
            if end > pivot +1:
                stack += [pivot+1]
                stack += [end]
    
    def mergeSorting(self,arry):
        
        def two_part_sort(left,right):
            result = []
            i,j = 0,0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result += [left[i]]
                    i += 1
                else:
                    result += [right[j]]
                    j +=1
            
            result += left[i:]
            result += right[j:]
            
            return result
                    
        
        def msort_rec(arry):      
            
            n = len(arry)
            mid = n // 2
            
            if mid < 1:
                return arry
            
            left = msort_rec(arry[:mid])
            right = msort_rec(arry[mid:])            
            result = two_part_sort(left,right)
            
            return result
        
        return msort_rec(arry)
        
    def mergeSorting2(self,arry):
        def two_part_sort(left,right):
            result = []
            i,j = 0,0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result += [left[i]]
                    i += 1
                else:
                    result += [right[j]]
                    j +=1
            
            result += left[i:]
            result += right[j:]
            
            return result
        
        def binary_function(arry):
            result = []
            i = 0
            while i <= len(arry)-2:
                result += [two_part_sort(arry[i],arry[i+1])]
                i +=2
            
            if i == len(arry)-1:
                result += [arry[i]]
#                print result
                
            return result
        
        i =len(arry) +1
        result = [[val] for _,val in enumerate(arry)]

        while i >= 1:
            result = binary_function(result)
            i //= 2         
        return result[0]  
          
    def mergeSorting3(self,arry):
        def two_sorted_arrys_sorting_in_place(arry,left,mid,right):
            result =[]
            i,j = left,mid+1
            while i <=mid and j <=right:
                if arry[i] <= arry[j]:
                    result += [arry[i]]
                    i += 1
                else:
                    result += [arry[j]]
                    j +=1
            
            result += arry[i:mid+1]
            result += arry[j:right+1]
            
            arry[left:right+1] = result[0:right-left+1]

        cur_size =1
        while cur_size<len(arry) -1:
            left =0 
            while left < len(arry) -1:
                mid = left + cur_size-1
                right = ((left+2*cur_size-1,len(arry)-1)[left+2*cur_size-1>len(arry)-1])
                two_sorted_arrys_sorting_in_place(arry,left,mid,right)
                left = left + cur_size*2
            
            cur_size =2*cur_size

    def heapSorting(self,arry):
#        for maxheap
        def siftDown(arry,start,end):
            i = start
            j = 2*i + 1
            temp = arry[i]
            while j <= end:
                if arry[j] < arry[j+1] and j <end:
                    j +=1
                if arry[j] > temp:
                    arry[i] = arry[j]
                    i = j
                    j = 2*i + 1
                else:
                    break
            arry[i] = temp
            
#        for maxheap                
        def siftUp(arry,end):
            i = end
            j = (i-1)/2
            temp =arry[i]
            while j > 0:
                if arry[j] < temp:
                    arry[i] = arry[j]
                    i = j
                    j = (i-1)/2
                else:
                    break
            arry[i] = temp
        
        def buildheapMax(arry,end):
            i = (end-1)/2
            while i>=0:
                siftDown(arry,i,end)
                i -=1

#'''only need one step of siftdown and no need build heapmax         
#        for i in range(len(arry)-1,0,-1):
#            buildheapMax(arry,i)
##            print arry
#            arry[0],arry[i] = arry[i],arry[0]
#'''                
        n = len(arry) -1
        buildheapMax(arry,n)
        arry[0],arry[n] = arry[n],arry[0]
        for i in range(n-1,-1,-1):            
            siftDown(arry,0,i)
            arry[0],arry[i] = arry[i],arry[0]
            
    def heapSorting2(self,arry):
        def heapify(arry, start, end): 
            largest =start
            l = 2*start+1
            r = 2*start+2
            if l <= end and arry[largest] < arry[l]:
                largest = l
            if r <= end and arry[largest] < arry[r]:
                largest = r
            if largest != start:
                arry[start],arry[largest] = arry[largest],arry[start] # swap                 
                
                heapify(arry,largest,end)
                
        for i in range(len(arry)-1,0,-1):
            heapify(arry,0,i)
            print arry
            arry[0],arry[i] = arry[i],arry[0]       
                
                
            
            
            
#%%
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90,11,32,90,55,44,13,15,16,22,55,33,22,77,88,1,3,9,0,87,66]     
##%%
#    print Sorting().insertionSorting(arr)
#    print Sorting().selectSorting(arr)
#    print Sorting().bubbleSorting(arr)
#    #%%
#    print arr
#    Sorting().quickSorting3(arr)
#    print arr
#%%
    print arr
    Sorting().heapSorting(arr)
    print arr
