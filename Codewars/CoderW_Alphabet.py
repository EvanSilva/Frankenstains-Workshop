# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    
    textLower = text.lower()
    
    import string
    abecedario = string.ascii_lowercase
    
    numberAssigned = ""
    
    for letter in textLower:
        if letter not in abecedario:
            continue
        else:
            numberLetter = abecedario.index(letter) 
            numberAssigned += str(numberLetter + 1) + " "
        
    return numberAssigned[:-1]
        