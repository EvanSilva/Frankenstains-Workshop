# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    
    sin_a = string_.replace("a", "")
    sin_e = sin_a.replace("e", "")
    sin_i = sin_e.replace("i", "")
    sin_o = sin_i.replace("o", "") 
    sin_u = sin_o.replace("u", "")
    sin_ocap = sin_u.replace("O", "")
    sin_acap = sin_ocap.replace("A", "") 
    sin_ecap = sin_acap.replace("E", "")
    sin_icap = sin_ecap.replace("I", "")
    sin_ucap = sin_icap.replace("U", "")
    
    return sin_ucap