cc = input("Введите ваш номер карты чтобы его скрыть: ")

def maskify(cc):
    if len(cc) > 4:
        vision = cc[-4:]
        blurCc = (len(cc) - 4) * "#" + vision
        print(blurCc)
    else:
      print(cc)
maskify(cc)