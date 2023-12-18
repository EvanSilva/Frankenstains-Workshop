# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    
    if text == "" and " ":
        return text
    else:
        dashRemover = text.replace("_", " ").replace("-", " ")
        addTitle = dashRemover.title()
        noSpaces = addTitle.replace(" ", "")
        camelCase = text[:1] + noSpaces[1:]
        
    return camelCase