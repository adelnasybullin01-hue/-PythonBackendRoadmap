# open(путь, режим) r w 

# read readline readlines

# test1 = file1.read()
# test2 = file1.readline()
# test2 = file1.readlines()
# print (test2)

# file1 = open('test.txt', 'r')

# for i in file1:
#     print(i)

with open('test.txt', 'r+') as f:
    print(f.read())
    f.write('hello')

