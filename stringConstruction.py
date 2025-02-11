s = "abab"      #output = 2       ,     ex= input= "abcd"  output=4


res = []        # empty list
for i in s:
    if i not in res:
        res.append(i)
        
print(len(res))  



