#!/usr/bin/python3


tupla = ('valor1', 'valor2', 'valor3','valor4')

#print(tupla1)
#print(type(tupla1))

#Criar uma Tupla com valores aleatorios
print(f"1º) {tupla}")
#Acessar o primeiro indice
print(f"2º) {tupla[0]}")
#Mostrar o 3º indice em formato de titulo
print(f"3º) {tupla[2].title()}")
#mostrar a 3ª letra do 3º indice
print(f"2º) {tupla[2][2]}")
#converter a tupla para uma lista e mudar o 1º indice para outro valor
lista = list(tupla)
print(type(lista))
tupla[0] = 'Python'
print(tupla)