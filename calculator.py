"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code


while True:
    user_input = input ("Enter your equation > ")
    math_operations = user_input.split(' ') 
    if math_operations[0] == "q":
        break
    elif math_operations[0] == "+":
        print (add(float(math_operations[1]), float(math_operations[2])))
    elif math_operations[0] == "-":
        print (subtract(float(math_operations[1]), float(math_operations[2])))
    elif math_operations[0] == "*":
        print (multiply(float(math_operations[1]), float(math_operations[2])))
    elif math_operations[0] == "/":
        print (divide(float(math_operations[1]), float(math_operations[2])))
    elif math_operations[0] == "square":
        print (square(float(math_operations[1])))
    elif math_operations[0] == "cube":
        print (cube(float(math_operations[1])))
    elif math_operations[0] == "power":
        print (power(float(math_operations[1]), float(math_operations[2]))) 
    elif math_operations[0] == "mod":
        print (mod(float(math_operations[1]), float(math_operations[2])))


