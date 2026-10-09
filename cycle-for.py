str1 = "HelloHHello"

# range(начало, конец, шаг)
# len()


for i in range(len(str1)):
    if i == 5:
        continue
    print(str1[i])
else:
    print("buy")

print("end")

# for i in str:
#    print(i)