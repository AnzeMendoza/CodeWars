def max_number(n):
    array=[]
    long_return=0

    while n >=1:
        array.append(n%10)
        n = int(n/10)
    array.sort()

    for n in range(0,len(array)):
        long_return +=  array[n]*pow(10,n)

    return long_return

def max_number2(n):
    return (int(''.join(sorted(str(n), reverse=True))))
    
print(max_number2(79584))

