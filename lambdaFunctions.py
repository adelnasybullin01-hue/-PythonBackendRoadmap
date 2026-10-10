
def SumNum (num1, num2):
    return num1 + num2
print(SumNum(1,2))

# lambda
func1 = lambda x,y : x + y
print(func1(10,20))

# map
list1 = ['1', '2', '3',]
list1_res = list(map(int, list1))
print(list1_res)

list_dollars = [21,22,32,8,19.33]
list_rub = list(map(lambda x: x*92, list_dollars))
print(list_rub)

#  zip
listC =[1,2,3,4,5]
strC = "ABCD"
tupleC = (True, False, True, False)
res = list(zip(listC, strC, tupleC))
print(res)