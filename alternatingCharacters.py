s = "AAAA"

count = 0
for i in range(1,len(s)):   #i=1
    if s[i] == s[i-1]:
        count += 1

print("eleminated characters is : ",count)
    