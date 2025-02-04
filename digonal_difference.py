#The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is |15-17|=2.

arr = [[1,2,3],
       [4,5,6],
       [9,8,9]]     

ans1 = 0
ans2 = 0

for i in range(len(arr)):
    ans1 += arr[i][i]
    ans2 += arr[i][len(arr[0])-i-1]

res = abs(ans1 - ans2)
print(res) 

