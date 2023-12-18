# https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    
    print(array1, array2)
    
    if array1 == None or array2 == None:
        return False 

    array1_squared = []

    for number in array1:
        array1_squared.append(number ** 2)
      
    if sorted(array1_squared) == sorted(array2):
        return True
    else:
        return False
	