
class user():
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password
    def print_user(self):
        print('i am', self.name, 'i am', self.age, 'y.o', 'my password is: ',self.password)    


user1 = user("Adel", 10, 123)

user1.print_user()

str1 = '123'

print(str1.count('4'))



