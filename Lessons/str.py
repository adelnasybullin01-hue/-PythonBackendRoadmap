
# str1 = "i am string"

# print(type(str1))

# str2 = "I-AM-PIDORAS"

#print(str2[0])
#print(str2[0:4])
#print(str2[0:6:2])

#str3 = "111"

#str4 = "222"

#print(str3+str4)
#print(str3 * 2)

# methods

str11 = "111222333"

# count() кол-во символов

#print(str11.count('1'))

# find() rfind() найти полож 1го символа с начала/с конца 

#print(str11.find('2'))
#print(str11.rfind('2'))

# index() rindex() найти полож 1го символа с начала/с конца 
# по сути тоже самое, но если не находит число, выдает ошибку

# lower() upper() переводит в верхний/нижний регистр

strTest = "Hello"

print(strTest.lower())
print(strTest.upper())

# rerlace(что заменить, на что заменить, сколько раз)
#если 3е знач не указывать то заменит все

strTest2 = "1000110010100101011"

strTest2 = strTest2.replace('0','!')

print(strTest2)





