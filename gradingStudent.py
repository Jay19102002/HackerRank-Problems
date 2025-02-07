grade = [73,67,38,33]   #list/array

for i in range(len(grade)):
    if(grade[i] > 37):
        if(5-(grade[i]%5) < 3):
            grade[i] += (5-(grade[i]%5))
            
    
print(grade)
