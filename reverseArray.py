arr = [1,2,3]

# print(arr[::-1])  

# arr.reverse()
# print(arr)

#get the length of array
n = len(arr)-1              # 2
       
for i in range((n//2)+1):   # 2/2+1 = 0+1 = [1]
    temp = arr[i]           # [] <= 2[1]
    arr[i] = arr[n-i]       # [] <= 1[0]
    arr[n-i] = temp         # [] <= 2[1]

print(arr)
