
# try:
#     f = open('test.txt', 'r')
#     f.write('11')
# except Exception as e:
#     print('error',e)
# finally:
#     f.close()
#     print('file closing')


# print('дальше код')

try: 
    num1 = int(input('write a num 1: '))
    num2 = int(input('write a num 2: '))
    print("division: ", num1/num2)
except ValueError as e:
    print('неуспешное преоразование',e)
except ZeroDivisionError as e:
    print('нельзя на ноль делить',e)
finally:
    print('программа завершена')
    
