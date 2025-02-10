
s = "1234"

if len(s) == 1:
    print("no")
    
else:
    for i in range(1, len(s)//2 + 1):
        str = s[:i] # starting
        pre = int(str)

        while len(str) < len(s):
            next = pre - 1
            str += next
            pre = next
        
        if str == s:
            print("yes",s[:i])
        else:
            print("No")
      


        
        

