import math

def comp(array1, array2):
    array1 = sorted(array1)
    
    for n in range(0, len(array2)):
        array2[n] = int(math.sqrt(array2[n]))
    array2 = sorted(array2)
    
    for m in range(0, len(array1)) :
        if array1[m] != array2[m]:
            print(array1[m], array2[m])
            return False         
    return True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1, a2))