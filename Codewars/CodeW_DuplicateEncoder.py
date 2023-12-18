# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    wordLower = word.lower()
    final_string = ""
    for char in wordLower:
        if wordLower.count(char) == 1:
            final_string += "("
        else:
            final_string += ")"
    return final_string