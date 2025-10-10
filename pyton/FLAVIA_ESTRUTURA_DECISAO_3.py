#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino
#M - Masculino
#Sexo Inválido.

#Desenvolvido por: Flávia Alessandra Fernandes

sexo = (input('Qual seu sexo?: '))

if sexo == 'F' or sexo == 'f':
    print('Sexo feminino.')
elif sexo == 'M' or sexo == 'm': 
    print('Sexo masculino.')
else:
    print('Sexo inválido!')
