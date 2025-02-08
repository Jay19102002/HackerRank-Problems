arr = {1,2,3,4,5}

print(sum(arr) - max(arr), sum(arr) - min(arr))

max = max(arr)  #5 
min = min(arr)  #1
add = sum(arr)  #15

print("Min of array Sum: ",add - max)   #15-5 = 10
print("Max of array sum: ",add - min)   #15-1 = 14