answer = ''
expenses = []

# запрос у пользователя данных
while answer != 'нет':

    yes = ["да"]
    no = ["нет","не"]

    categoryUser = input('Введите категорию вашей траты: ')
    print()

    amountUser = int(input('Введите сумму вышей траты: '))
    print() 

    dict1 = {'category': categoryUser, 'amount': amountUser}
    expenses.append(dict1)

    answer = input('Вы хотите продолжить дополнять список? (Да/Нет): ').lower()
    print()

    if answer != "да" not in yes and "нет" not in no:
        print("Некорректное значение")
        break

    if answer == "нет" in no:
        break

def calculateSum():
    total = 0
    for amount in expenses:
        amount = amount["amount"]
        total = total + amount
    return f'Общие расходы: {total}'


def viewAllCategoryes():
    for i in expenses:
        category = i["category"]
        amount = i["amount"]
        print(f'За категорию {category}, сумма: {amount}')

def findMostExpensive():
    mostExpensive = 0
    for i in expenses:
        amount = i["amount"]
        category = i["category"]
        if amount > mostExpensive:
            mostExpensive = amount
            mostExpensiveCategory = category
    return (f'Наибольшей тратой является {mostExpensiveCategory}: {mostExpensive}')

def filterExpenses(minAmount):
    filterList = []
    for expense in expenses:
        amount = expense["amount"]
        if amount < minAmount:
            filterList.append(expense)
    if not filterList: return (f'Трат менее чем {minAmount}, не найдено')    
    # для красивового вывода листа в терминал
    print(f'Траты менее {minAmount}:')
    for expense in filterList:
        category = expense["category"]
        amount = expense["amount"]
        print(f'{category}: {amount}')

print(calculateSum())
print()

viewAllCategoryes()
print()

print(findMostExpensive())
print()

filterAnswer = int(input('Ниже какого значения вам нужны категории? '))

filterExpenses(filterAnswer)
print()

