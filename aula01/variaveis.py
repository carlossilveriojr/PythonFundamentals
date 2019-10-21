#!/usr/bin/python3

num = 1
decimal = 10.3
texto = "Valor em texto"

# concatenação de variáveis
print("O valor numerico é: " + str(num) \
+" e valor decimal é: " + str(decimal)) 

# concatenação de variáveis com f string
print(f"O valor é: {num}")

print(f"O valor é: {num} e o valor da decimal é: {decimal}")

print("O meu texto da variavel é {}".format(texto))

nome = input("Digite seu nome:")

print(f"o Seunome é: {nome}")
