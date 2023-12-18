# https://www.codewars.com/kata/54ff3102c1bad923760001f3

# Barely effective. Count with a failsafe in case there's not the vowel we are seaching for
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