# 3. Write a program that will convert celsius value to fahrenheit.
num1, num2 = map(int, input("Enter two numbers: ").split()) 

def swap_numbers(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2
swap_numbers(num1, num2)
#why is tuple unpacking can be useful here
#Is there somethinig wrong?