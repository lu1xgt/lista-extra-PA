num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
opr = int(input("1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão: "))
cal = (num1 + num2)
cal2 = (num1 - num2)
cal3 = (num1 * num2)
cal4 = (num1 / num2)
if opr == 1:
    print (f"o resultado da sua conta é: {cal}")
elif opr == 2:
    print (f"o resultado da sua conta é: {cal2}")
elif opr == 3:
    print (f"o resultado da sua conta é: {cal3}")
elif opr == 4:
    print (f"o resultado da sua conta é: {cal4}")
