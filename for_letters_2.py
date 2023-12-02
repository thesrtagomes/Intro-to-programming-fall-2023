word = 'Gabriel'
number_letters = len(word)  #aqui eu posso declarar o número que eu quero ou eu posso usar o length
#usando len para achar o numero da quantidade de caracteres que a palavra possui
for index in range(number_letters):
    print(f'position: {index} and letter: {word[index]}')
    #index não significa nada, apenas diz que esta variavel dentro de um arranjo feito pelo numero de letras
    #que a palavra tem, ele vai printar o numero de letras. 
    #Dizendo para printar apenas o index, é o numero de cada posição que tem o number_letters
    #e dizendo que word que é a palavra em si printando separadamente a letra pertencente a cada
    #posição ao colocar um colchete ao lado dela, indicando assim que a palavra do word será printado.