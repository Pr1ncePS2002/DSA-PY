def insertion_sort(arr):
    n= len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0:
            if arr[j]<key:
                break
            else:
                arr[j+1]=arr[j]
                j-=1
        arr[j+1]=key
    return arr

arr=[20,15,17,8,90,45]
sorted_arr=insertion_sort(arr)
print(sorted_arr)
        
