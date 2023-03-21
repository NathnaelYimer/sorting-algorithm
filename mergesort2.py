import time
start=time.time()
from typing import Counter
def merge_sort(inp_arr):
    counter=0
    size = len(inp_arr)
    if size <=1:
        return(inp_arr,counter)
    left_arr=merge_sort(inp_arr[:size//2])
    right_arr=merge_sort(inp_arr[size//2:])
    counter=left_arr[1] + right_arr[1]
    
    left_index=0
    right_index=0
    final_index=0
    while left_index < len(left_arr[0]) and right_index < len(right_arr[0]):
        counter+=1
        if left_arr[0][left_index] < right_arr[0][right_index]:
            inp_arr[final_index]=left_arr[0][left_index]
            left_index+=1
        else:
            inp_arr[final_index]=right_arr[0][right_index]
            right_index+=1
        final_index+=1
    while left_index < len(left_arr[0]):
        inp_arr[final_index]=left_arr[0][left_index]
        left_index+=1
        final_index+=1
        counter+=1
    while right_index < len(right_arr[0]):
        inp_arr[final_index]=right_arr[0][right_index]
        right_index+=1
        final_index+=1
        counter+=1
    return (inp_arr,counter)
listtosort=[]
listtosort.reverse()
print(merge_sort(listtosort))
end=time.time()
print(end-start)