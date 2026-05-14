contador = 1
soma= 0
while contador <= 5:
    tr = int(input(f"digite seu {contador} número: "))
    soma = soma + tr
    contador += 1
print(f'sua soma é {soma}')
