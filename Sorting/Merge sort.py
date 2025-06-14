def merge_sort(arr):
    if len(arr)<=1:
        return arr
        
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    
    return merge(left,right)
    
def merge(left,right):
    sorted_list=[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_list.append(left[i])
            i+=1 
        else:
            sorted_list.append(right[j])
            j+=1 
    while i<len(left):
        sorted_list.append(left[i])
        i+=1 
    while j<len(right):
        sorted_list.append(right[j])
        j+=1
            
    return sorted_list
