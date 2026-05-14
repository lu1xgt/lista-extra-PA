soma_notas = 0
quantidade = 0
maior_nota = 0
menor_nota = 0
parar = False
while parar == False:
    nota = float(input("Digite a nota: "))
    soma_notas = soma_notas + nota
    quantidade = quantidade + 1
    if quantidade == 1:
        maior_nota = nota
        menor_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
    resposta = input("Deseja continuar? (s/n): ")
    if resposta == 'n' or resposta == 'N':
        parar = True
media = soma_notas / quantidade
print("--------------------------")
print("Quantidade de notas:", quantidade)
print("Média da turma:", media)
print("Maior nota:", maior_nota)
print("Menor nota:", menor_nota)
