a=[1,3,4]
b=[4,1,4]

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if (a[i] < b[i]):
            bob +=1
        elif a[i] > b[i]:
            alice +=1
    
    return alice,bob