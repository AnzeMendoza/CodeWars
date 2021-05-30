def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    diccionario = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,'D': 500,'M': 1000}
    anio = 0
    if len(roman) == 1:
        return diccionario[roman[0]]
    
    if diccionario[roman[0]] > diccionario[roman[1]]:
        anio = diccionario[roman[0]]
    
    for i in range(2,len(roman)):
        if diccionario[roman[i-1]] < diccionario[roman[i]] :
            parcial = 0
            parcial = diccionario[roman[i]] - diccionario[roman[i-1]]
        if parcial = 0:
            anio+=parcial
        else:
            anio+=diccionario[roman[i]]
    return anio

#print(solution('XIV'))
print(solution('XXI'))