# https://www.codewars.com/kata/58ae6ae22c3aaafc58000079

def permute_a_palindrome(myinput): 
    
    lista = []
    
    for letter in myinput:      
        if letter in lista:
            lista.remove(letter)
        else:
            lista.append(letter)
        
    return len(lista) <= 1    