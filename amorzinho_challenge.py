# peça ao usuario para digitar um numero inteiro
# com o numero inteiro, desenhe um triangulo
# caso o numero digitado for 5, a estrutura deve se parecer assim:
# dica: voce pode usar "*".repeat(numero) para repetir os asteristicos
# *
# **
# ***
# ****
# *****

user_number = int(input('Digite o numero: '))
number = user_number + 1
for star in range(number):  
    estrela = "*" * star  #estrela diz que na multiplicação de * é feita porque a star vai chegar na posição
    print(estrela) #de numero X ou Y e ela vai repetir o numero da variavel, neste caso, a *. Porque é string, eles se repetem ao invés de multiplicarem-se 