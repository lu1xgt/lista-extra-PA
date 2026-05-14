aluno = input("digite seu nome completo: ")
nf = float(input("digite a nota final: "))
if nf >= 7:
    print (f"você aluno: {aluno}, passou!.")
elif nf >= 5 and nf <= 6.9:
    print (f"você aluno: {aluno}, esta de recuperação.")
else:
    print (f"você aluno: {aluno}, foi reprovado.")
    
