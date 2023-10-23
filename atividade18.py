# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1,n2=float(input("numero 1: ")), float(input("numero 2: "))
if n1>n2:
    print("o primeiro valor é maior")
elif n2>n1:
    print("o segundo valor é maior")
else: 
    print("não existe valor maior, os dois são iguais")