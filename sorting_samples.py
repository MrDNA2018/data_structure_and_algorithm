## -*- coding: utf-8 -*-
#
## Python program for implementation of Insertion Sort 
#
## Function to do insertion sort 
#def insertionSort(arr): 
#
#	# Traverse through 1 to len(arr) 
#	for i in range(1, len(arr)): 
#
#		key = arr[i] 
#
#		# Move elements of arr[0..i-1], that are 
#		# greater than key, to one position ahead 
#		# of their current position 
#		j = i-1
#		while j >=0 and key < arr[j] : 
#				arr[j+1] = arr[j] 
#				j -= 1
#		arr[j+1] = key 
#
#
## Driver code to test above 
#arr = [12, 11, 13, 5, 6] 
#insertionSort(arr) 
#for i in range(len(arr)): 
#	print ("%d" %arr[i]) 
#
## This code is contributed by Mohit Kumra 
##%%
#    # Python program for implementation of Selection 
## Sort 
#A = [64, 25, 12, 22, 11] 
#
## Traverse through all array elements 
#for i in range(len(A)): 
#	
#	# Find the minimum element in remaining 
#	# unsorted array 
#	min_idx = i 
#	for j in range(i+1, len(A)): 
#		if A[min_idx] > A[j]: 
#			min_idx = j 
#			
#	# Swap the found minimum element with 
#	# the first element		 
#	A[i], A[min_idx] = A[min_idx], A[i] 
#
## Driver code to test above 
#print ("Sorted array") 
#for i in range(len(A)): 
#	print("%d" %A[i]), 
##%%
## Python program for implementation of Bubble Sort 
#
#def bubbleSort(arr): 
#	n = len(arr) 
#
#	# Traverse through all array elements 
#	for i in range(n): 
#
#		# Last i elements are already in place 
#		for j in range(0, n-i-1): 
#
#			# traverse the array from 0 to n-i-1 
#			# Swap if the element found is greater 
#			# than the next element 
#			if arr[j] > arr[j+1] : 
#				arr[j], arr[j+1] = arr[j+1], arr[j] 
#
## Driver code to test above 
#arr = [64, 34, 25, 12, 22, 11, 90] 
#
#bubbleSort(arr) 
#
#print ("Sorted array is:") 
#for i in range(len(arr)): 
#	print ("%d" %arr[i]), 
##%%
## Python program for implementation of Quicksort Sort 
#
## This function takes last element as pivot, places 
## the pivot element at its correct position in sorted 
## array, and places all smaller (smaller than pivot) 
## to left of pivot and all greater elements to right 
## of pivot 
#def partition(arr,low,high): 
#	i = ( low-1 )		 # index of smaller element 
#	pivot = arr[high]	 # pivot 
#
#	for j in range(low , high): 
#
#		# If current element is smaller than or 
#		# equal to pivot 
#		if arr[j] <= pivot: 
#		
#			# increment index of smaller element 
#			i = i+1
#			arr[i],arr[j] = arr[j],arr[i] 
#
#	arr[i+1],arr[high] = arr[high],arr[i+1] 
#	return ( i+1 ) 
#
## The main function that implements QuickSort 
## arr[] --> Array to be sorted, 
## low --> Starting index, 
## high --> Ending index 
#
## Function to do Quick sort 
#def quickSort(arr,low,high): 
#	if low < high: 
#
#		# pi is partitioning index, arr[p] is now 
#		# at right place 
#		pi = partition(arr,low,high) 
#
#		# Separately sort elements before 
#		# partition and after partition 
#		quickSort(arr, low, pi-1) 
#		quickSort(arr, pi+1, high) 
#
## Driver code to test above 
#arr = [10, 7, 8, 9, 1, 5] 
#n = len(arr) 
#quickSort(arr,0,n-1) 
#print ("Sorted array is:") 
#for i in range(n): 
#	print ("%d" %arr[i]), 
#
## This code is contributed by Mohit Kumra 
##%%
#def qsort_rec(arry,start,end):      
#    if start >= end:
#        return 
#    i = start
#    j = end
#    pivot = arry[start]
#    while i<j:
#        while i<j and arry[j] >= pivot:
#            j -=1
#        if i<j:
#            arry[i] = arry[j]
#            i +=1
#        while i<j and arry[i] <= pivot:
#            i +=1
#        if i<j:
#            arry[j] = arry[i]
#            j -=1
#    arry[i] = pivot
#    qsort_rec(arry,start,i-1)
#    qsort_rec(arry,i+1,end)
#
#arr = [10, 7, 8, 9, 1, 5] 
#n = len(arr) 
#print ("Sorted array is:") 
#qsort_rec(arr,0,n-1)
#
#print arr
#
##%%
## Python program for implementation of Quicksort 
#
## This function is same in both iterative and recursive 
#def partition(arr,l,h): 
#	i = ( l - 1 ) 
#	x = arr[h] 
#
#	for j in range(l , h): 
#		if arr[j] <= x: 
#
#			# increment index of smaller element 
#			i = i+1
#			arr[i],arr[j] = arr[j],arr[i] 
#
#	arr[i+1],arr[h] = arr[h],arr[i+1] 
#	return (i+1) 
#
## Function to do Quick sort 
## arr[] --> Array to be sorted, 
## l --> Starting index, 
## h --> Ending index 
#def quickSortIterative(arr,l,h): 
#
#	# Create an auxiliary stack 
#	size = h - l + 1
#	stack = [0] * (size) 
#
#	# initialize top of stack 
#	top = -1
#
#	# push initial values of l and h to stack 
#	top = top + 1
#	stack[top] = l 
#	top = top + 1
#	stack[top] = h 
#
#	# Keep popping from stack while is not empty 
#	while top >= 0: 
#
#		# Pop h and l 
#		h = stack[top] 
#		top = top - 1
#		l = stack[top] 
#		top = top - 1
#
#		# Set pivot element at its correct position in 
#		# sorted array 
#		p = partition( arr, l, h ) 
#
#
#		# If there are elements on right side of pivot, 
#		# then push right side to stack 
#		if p+1 < h: 
#			top = top + 1
#			stack[top] = p + 1
#			top = top + 1
#			stack[top] = h 
#        	# If there are elements on left side of pivot, 
#		# then push left side to stack 
#		if p-1 > l: 
#			top = top + 1
#			stack[top] = l 
#			top = top + 1
#			stack[top] = p - 1
#
#
## Driver code to test above 
#arr = [4, 3, 5, 2, 1, 3, 2, 3] 
#n = len(arr) 
#quickSortIterative(arr, 0, n-1) 
#print ("Sorted array is:") 
#for i in range(n): 
#	print ("%d" %arr[i]), 
#
## This code is contributed by Mohit Kumra 
##%%
#    
#    def mergeSorting(self,arry):
#        
#        def two_part_sort(left,right):
#            result = []
#            i,j = 0,0
#            while i < len(left) and j < len(right):
#                if left[i] < right[j]:
#                    result += left[i]
#                    i += 1
#                else:
#                    result +=right[j]
#                    j +=1
#            
#            result += left[i:]
#            result += right[j:]
#            
#            return result
#                    
#        
#        def msort_rec(arry):      
#            
#            n = len(arry)
#            mid = n // 2
#            
#            if mid < 1:
#                return arry
#                print arry
#            
#            left = msort_rec(arry[:mid])
#            right = msort_rec(arry[mid:])
#            
#            result = two_part_sort(left,right)
#            
#            print result
#            return result
##%%
#            # Iterative Merge sort (Bottom Up) 
#
## Iterative mergesort function to 
## sort arr[0...n-1] 
#def mergeSort(a): 
#	
#	current_size = 1
#	
#	# Outer loop for traversing Each 
#	# sub array of current_size 
#	while current_size < len(a) - 1: 
#		
#		left = 0
#		# Inner loop for merge call 
#		# in a sub array 
#		# Each complete Iteration sorts 
#		# the iterating sub array 
#		while left < len(a)-1: 
#			
#			# mid index = left index of 
#			# sub array + current sub 
#			# array size - 1 
#			mid = left + current_size - 1
#			
#			# (False result,True result) 
#			# [Condition] Can use current_size 
#			# if 2 * current_size < len(a)-1 
#			# else len(a)-1 
#			right = ((2 * current_size + left - 1, 
#					len(a) - 1)[2 * current_size 
#						+ left - 1 > len(a)-1]) 
#							
#			# Merge call for each sub array 
#			merge(a, left, mid, right) 
#			left = left + current_size*2
#			
#		# Increasing sub array size by 
#		# multiple of 2 
#		current_size = 2 * current_size 
#
## Merge Function 
#def merge(a, l, m, r): 
#	n1 = m - l + 1
#	n2 = r - m 
#	L = [0] * n1 
#	R = [0] * n2 
#	for i in range(0, n1): 
#		L[i] = a[l + i] 
#	for i in range(0, n2): 
#		R[i] = a[m + i + 1] 
#
#	i, j, k = 0, 0, l 
#	while i < n1 and j < n2: 
#		if L[i] > R[j]: 
#			a[k] = R[j] 
#			j += 1
#		else: 
#			a[k] = L[i] 
#			i += 1
#		k += 1
#
#	while i < n1: 
#		a[k] = L[i] 
#		i += 1
#		k += 1
#
#	while j < n2: 
#		a[k] = R[j] 
#		j += 1
#		k += 1
#
#
## Driver code 
#a = [12, 11, 13, 5, 6, 7] 
#print("Given array is ") 
#print(a) 
#
#mergeSort(a) 
#
#print("Sorted array is ") 
#print(a) 
#
## Contributed by Madhur Chhangani [RCOEM] 
#%%



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
        result += two_part_sort(arry[i],arry[i+1])
        i +=2
    
    if i == len(arry)-1:
        result += arry[i]
        
    return result
#%%      
a1 = [1]
a2 = [2,2,6]
a3 =[a1,a2]

#%%
print binary_function(a3)


#%%
a2 = [2,2,6]
result = [[val] for _,val in enumerate(a2)]

#%%
def two_sorted_arrys_sorting_in_place(arry,left,mid,right):
    result =[]
    i,j = left,mid+1
    while i <= mid and j <= right:
        if arry[i] <= arry[j]:
            result += [arry[i]]
            i += 1
        else:
            result += [arry[j]]
            j +=1
    
    result += arry[i:mid+1]
    result += arry[j:right+1]
    
    return result

#%%
#%%
def two_sorted_arrys_sorting_in_place1(arry,left,mid,right):
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
    
    arry[left:right+1] = result
#%%
a = [9,0,1,2,3,4]
print a
two_sorted_arrys_sorting_in_place1(a,0,0,5)
print a

#print two_sorted_arrys_sorting_in_place(a,1,2,9)
#%%
def siftDown(arry,start,end):
    i = start
    j = 2*i + 1
    temp = arry[i]
    while j <= end:
        if j <end and arry[j] < arry[j+1] :
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

def heapMax(arry,end):
    i = (end-1)/2
    while i>=0:
        siftDown(arry,i,end)
        i -=1
#%%
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
#%%
a = [9,0,1,21,3,4,9,7]
heapify(a,0,7)
print a
