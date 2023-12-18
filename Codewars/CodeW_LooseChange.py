# https://www.codewars.com/kata/5571f712ddf00b54420000ee

def loose_change(cents):
    print(cents)
    base_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents <= 0:
        return base_dict

    basequarters = 0
    basedimes = 0
    basepennies = 0
    basenickels = 0

    while int(cents) != 0:
        if cents >= 25:
            cents = cents - 25
            basequarters = basequarters + 1
            base_dict['Quarters'] = basequarters
        elif cents >= 10:
            cents = cents - 10
            basedimes = basedimes + 1
            base_dict['Dimes'] = basedimes
        elif cents >= 5:
            cents = cents - 5
            basenickels = basenickels + 1
            base_dict['Nickels'] = basenickels
        elif cents >= 1:
            cents = cents - 1
            basepennies = basepennies + 1
            base_dict['Pennies'] = basepennies
    return base_dict