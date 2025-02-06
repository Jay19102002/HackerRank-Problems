# anagram of a palindrome.      string = aaabbbb,  result = bbaaabb, abbabba, bababab

str = "aaabbbb"

hm = {}     #hash map
for i in str:
    if i not in hm:
        hm[i] = str.count(i)        #key: value
                                    #a: 3
odd_c = 0
for key in hm:
    if hm[key]%2 == 1:
        odd_c += 1
if odd_c > 1:
    print("No anagram of palindrome")
else:
    print("Anagram of palindrome")
