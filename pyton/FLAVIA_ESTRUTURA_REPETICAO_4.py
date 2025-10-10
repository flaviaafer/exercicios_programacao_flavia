#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

#Desenvolvido por: Flávia Alessandra Fernandes

# Programa que mostra os números de 1 a 20

print("Números de 1 a 20 (um abaixo do outro):")
for i in range(1, 21):
    print(i)

print("\nNúmeros de 1 a 20 (um ao lado do outro):")
for i in range(1, 21):
    print(i, end = ' ')
