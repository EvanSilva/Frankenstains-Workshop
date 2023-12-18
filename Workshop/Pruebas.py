def get_count(sentence):
    a = sentence.count("a")
    if a == None:
        a = 0
    e = sentence.count("e")
    if e == None:
        e = 0
    i = sentence.count("i")
    if i == None:
        i = 0
    o = sentence.count("o")
    if o == None:
        o = 0
    u = sentence.count("u")
    if u == None:
        u = 0

    counter = a + e + i + o + u
    return counter


print(get_count("aeiou  ljnzxxm,ncdasnjfksisbednm,acsc mlknasjbvdasvbndsabnc"))


def xo(s):
    x = s.count("x")
    xup = s.count("X")
    o = s.count("o")
    oup = s.count("O")
    
    if x + xup == o + oup:
        return True
    else:
        return False
    

def to_camel_case(text):
    no_dash = text.replace("_", " ").replace("-", " ")
    titled = no_dash.title()
    no_spaces = titled.replace(" ", "")
    camelCase = text[0] + no_spaces[1:]
 
    return camelCase

print(to_camel_case("The-Stealth-Warrior"))

# Takes string, tests if its empty, else, does the intended work, replacing
# first letter for the text's basic letter. 

def to_camel_case2(text):
    
    if text == "" and " ":
        return text
    else:
        dashRemover = text.replace("_", " ").replace("-", " ")
        addTitle = dashRemover.title()
        noSpaces = addTitle.replace(" ", "")
        return text[:1] + noSpaces[1:]
    if text[:1] == "_" or "-":        
        return 
    

print(to_camel_case2('the_steal-warrior_'))
print(to_camel_case2('the-steal_warrior-'))
print(to_camel_case2('-the_steal_warrior'))
print(to_camel_case2('_the-steal-warrior'))
