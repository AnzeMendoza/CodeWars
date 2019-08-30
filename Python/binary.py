def print_trasfer(lst_data):
    list_return = ["+"+str(lst_data[n])+"s^"+str(n) for n in range(0,len(lst_data)) ]
    return "".join(list_return)

print(print_trasfer([1,2,3,4,5]))

ll = [n for n in range(10)]

print(ll)