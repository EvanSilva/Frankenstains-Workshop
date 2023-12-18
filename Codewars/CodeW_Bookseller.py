# https://www.codewars.com/kata/54dc6f5a224c26032800005c

def stock_list(list_of_books, categorie):
    
    base_string = ""
    
    if list_of_books == [] or categorie == []:
        return base_string
    
    book_dictionary = {}
    for letter in categorie:

        book_dictionary[letter] = 0

        for bundle in list_of_books:
            
            number = str(bundle.split(" ")[-1])

            if bundle[0] == letter:
                book_dictionary[letter] += int(number)

    for entry, value in book_dictionary.items():
        base_string += str(entry)+ " : " +str(value)+ ") - ("
        closed_string = "(",base_string,")"
        starting = str(closed_string[1:]).replace("'","")
        ending = starting.replace(" - (, ))","")
        
    return str(ending)