def selection_sort(lst):
    
    for i in range(len(lst)):
        min_idx=i 
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_idx]:
                min_idx=j
        lst[i],lst[min_idx]=lst[min_idx],lst[i]
    return lst

arr=[20,15,17,8,90,45]
sorted_arr=selection_sort(arr)
print(sorted_arr)