def rString(str):
    for i in range(len(str)):
        if str[i] == ' ':
            str1 = str[:i]      #starting: i  i.e.,shivanshu
            str2 = str[i+1:]    #i+1 :ending    i.e.,singh
    
    
    return str
        
str1 = "Digesh Gabel"

print("Original String: ",str1)
print("Reversed String: ", rString(str1))

print("another string: ", str1[::-1])

# Time complexity: O(n)
# Space complexity: O(n)