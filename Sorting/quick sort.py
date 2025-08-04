def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    
    left=[x for x in arr if x<pivot ]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    
    return quick_sort(left)+middle+quick_sort(right)

arr=[20,15,17,8,90,45,4,22,33,321,33,22,233,455]
sorted_arr=quick_sort(arr)
print(sorted_arr)