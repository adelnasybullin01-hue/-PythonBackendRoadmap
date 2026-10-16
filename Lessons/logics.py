# bool - true or false

num1 = input('Write a number 01: ')
num2 = input('Write a number 02: ')
sign = input('Write a type of operationt[+}[-][/][//][%][**]: ')

if type(num1) != int or type(num2) != int:
    print('You did not enter a number!')
elif sign != "+" or sign != "-" or sign != "/" or sign != "//" or sign != "%" or sign != "**":
    print('Yu did not enter a sign')
elif sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "/" and num2 <= 0:
    print('You can not division by zero!')
elif sign == "/" and num2 > 0:
    print(num1 / num2)
elif sign == "//" and num2 <= 0:
    print('You can not division by zero!')
elif sign =="//":
    print(num1 // num2)
elif sign == "%":
    print(num1 % num2)
elif sign == "**":
    print(num1 ** num2)    