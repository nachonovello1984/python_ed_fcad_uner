from math import floor
from data_structures import ArrayStack

def decimal_to_binary(decimal_number: int) :
    stack = ArrayStack()
    number = decimal_number
    binary_str = ''
    while number > 0 : 
        rem = str(floor(number % 2)) 
        stack.push(rem) 
        number = floor(number / 2) 
    
    while not stack.is_empty() :
        binary_str += str(stack.pop())

    return binary_str


expresion1 = 5
expresion2 = 100
expresion3 = 2021

print(f"expresión1: {expresion1} -> ", decimal_to_binary(expresion1))
print(f"expresión1: {expresion2} -> ", decimal_to_binary(expresion2))
print(f"expresión1: {expresion3} -> ", decimal_to_binary(expresion3))

