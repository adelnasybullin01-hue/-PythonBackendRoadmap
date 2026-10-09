# tup1 = tuple('hello')

# print(tup1)

#tuple() кортеж, по сути неизменяемый список

#ключ должен быть неизмменяемым типом данных

# dict1 = {"name": "Adel", "age": "19"}
# dict1 = {'password': '123'}
# print(dict1['password']) 

dict2 = dict(name = "Adeldo",age=90,password="1234")
# print(dict2)

# выводит ключи .keys()
print(list(dict2.keys()))

# выводит значения .values()
print(list(dict2.values()))

# выдает кортежи .items()
print(list(dict2.items()))

# находит значение по ключу, нет ключа = None .get(key)
print(dict2.get('name'))

# удаляет значение по ключу .pop(key)
print(dict2.pop('age'))
print(dict2)

# множество
# set() {}

set1 = set()
set1.add('1')
set1.add('2')
set1.add('3')
set1.add('4')
set1.remove('2')
print(set1)

froz= frozenset('1234')

print(froz)