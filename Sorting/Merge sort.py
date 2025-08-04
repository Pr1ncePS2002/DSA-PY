def merge_sort(arr):
    if len(arr)<=1:
        return arr
        
    mid=len(arr)>>1
    left=merge_sort(arr[:mid]) #SORT BOTH HALVES
    right=merge_sort(arr[mid:])
    
    return merge(left,right) #MERGE BOTH SORTED HALVES
    
def merge(left,right):
    sorted_list=[]
    i=j=0
    
    while i<len(left) and j<len(right):  
        if left[i]<right[j]:   #COMPARE EACH ELEMENT WITH OTHER LIST AS WELL
            sorted_list.append(left[i])
            i+=1 
        else:
            sorted_list.append(right[j])
            j+=1 
            
    #FILL THE REMAINING LEFT ELEMENTS
    while i<len(left):
        sorted_list.append(left[i])
        i+=1 
    while j<len(right):
        sorted_list.append(right[j])
        j+=1
            
    return sorted_list

arr=[20,15,17,8,90,45]
sorted_arr=merge_sort(arr)
print(sorted_arr)

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr)>>1
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

        
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1