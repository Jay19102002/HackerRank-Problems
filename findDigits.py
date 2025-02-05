n = 246810
print("Original list: ", n)



count = 0

for i in map(int, str(n)):
    if i==0:
        continue
    elif n%i==0:
        count += 1

print(count)