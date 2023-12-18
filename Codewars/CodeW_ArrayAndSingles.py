# https://www.codewars.com/kata/59f11118a5e129e591000134`

def repeats(arr):
    NotRepeated = []
    for number in arr:
        if arr.count(number) == 2:
            continue
        else:
            NotRepeated.append(number)
            
    return sum(NotRepeated)