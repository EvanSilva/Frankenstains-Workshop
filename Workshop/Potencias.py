def funcion(array1, array2):

    if array1 == None or array2 == None:
        return False
    
    if array1 == "" or array2 == "":
        return False

    array1_squared = []

    for number in array1:
        array1_squared.append(number ** 2)
      

    if sum(array1_squared) == sum(array2):
        return True
    else:
        return False

print(funcion([], [121, 144]))

