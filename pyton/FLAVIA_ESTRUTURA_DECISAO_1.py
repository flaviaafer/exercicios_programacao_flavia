#Faça um programa que peça dois números e imprima o maior deles.

#Desenvolvido por: Flávia Alessandra Fernandes

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 > num2:
    print(num1,'é o maior!')
elif num1 < num2:
    print(num2,'é o maior!')
else:
    print('Os números são iguais!')