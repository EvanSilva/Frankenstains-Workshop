def sum(a, b):

    sumaBasica = a + b
    return sumaBasica


print(sum("Argon", "chisss"))
print("--------------------------")
def square(primerNumero):

    cuadrado = primerNumero * primerNumero
    return cuadrado

print(square(5))
print("--------------------------")
def sum3(primerNumero, segundoNumero, tercerNumero):
    
    
    return primerNumero + segundoNumero + tercerNumero

print(sum3(1, 2 ,3))
print("--------------------------")
def abbaize(firstString, secondString):
    
    return firstString + (secondString * 2) + firstString

print(abbaize("hola", "caracola"))
print("--------------------------")

def find_second(firstString, secondString):

    fullString = firstString + secondString

    return fullString.find(secondString)


print(find_second("horacioelcaracol ", "caracola"))
print("--------------------------")

def find_secondOne(targetWord, searchText):

    firstFind = searchText.find(targetWord)
    secondFind = searchText.find(targetWord, firstFind + 1)

    return secondFind


print(find_secondOne("caracoles", "Los caracoles son muy amigables caracoles."))
print("--------------------------")
def bigger(firstNum, secondNum):

    if firstNum > secondNum:
        biggerNum = firstNum
        return biggerNum
    
    if  secondNum > firstNum:
        biggerNum = secondNum
        return biggerNum
    if firstNum == secondNum:
        biggerNum = firstNum
        return biggerNum



print(bigger(2,7))
print(bigger(3,2))
print(bigger(3,3))
print("--------------------------")


def elsebigger(firstNum, secondNum):
    if firstNum > secondNum:
        return firstNum
    else:
        return secondNum


print(bigger(2,7))
print(bigger(3,2))
print(bigger(3,3))
print("--------------------------")


def is_friend(nameFriend):

    if nameFriend[0] == "D":
        return True
    else:
        return False
    
print(is_friend("David"))
print(is_friend("David"))
print(is_friend("Marcos"))
print(is_friend("Javier")) 
print("--------------------------") 


def is_friend_two(nameFriend):

    if nameFriend[0] == "D":
        return True
    else:
        if nameFriend[0] == "N":
            return True
        else:
            return False


    
print(is_friend("David"))
print(is_friend("David"))
print(is_friend("Marcos"))
print(is_friend("Javier")) 
print(is_friend("Naruto"))
print("--------------------------") 

def biggest(firstNum, secondNum, thirdNum):
    if firstNum > secondNum and firstNum > thirdNum:
        return firstNum
    else:
        if secondNum > firstNum and secondNum > thirdNum:
            return secondNum
        else:
            if thirdNum > firstNum and secondNum:
                return thirdNum

print(biggest(6, 2, 3))
print(biggest(6, 2, 7))
print(biggest(6, 9, 3))
print(biggest(6, 16, 3))
print(biggest(9, 2, 7))
print(biggest(6, 99, 3))
print(biggest(6, 2, 169))
print(biggest(1, 2, 7))
print(biggest(2, 1, 3))
            
print("--------------------------") 


# Meter aqui el numero que quieres contar hasta
printNumbers = 10
baseNumber = 0
while baseNumber != printNumbers:
    baseNumber = baseNumber + 1
    print(baseNumber)