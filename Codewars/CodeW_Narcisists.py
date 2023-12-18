# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(value):
        
    value_str = str(value)
    length = len(value_str)
    base_list = [int(digit) for digit in value_str]
    sum_of_powers = sum([digit ** length for digit in base_list])
    
    return sum_of_powers == value