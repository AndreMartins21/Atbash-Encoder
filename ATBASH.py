def atbash(palav):
    '''
    Função exclusiva para receber como parâmetro uma frase/palavra qualquer, convertendo-a para a cifra simples de substituição ATBASH.
    Caso queira saber mais a respeito dessa codificação, acesse o site: https://pt.wikipedia.org/wiki/Atbash.
    Autor: André Martins
    '''

    alfabeto = []
    reverse = []
    letras = []
    atb = []

    # ALFABETO / ALFABETO INVERTIDO:
    alf_junto = 'abcdefghijklmnopqrstuvwxyz'
    for contador in range(len(alf_junto)):
        alfabeto.append(alf_junto[contador])

    for inverse in range(len(alfabeto)-1, -1, -1):
        reverse.append(alfabeto[inverse])

    # SEPARAR AS LETRAS E FORMAR O ATBASH
    for cont in range(0, len(palav)):
        letras.append(palav[cont])
    
    for letra in letras:
        if letra not in alfabeto:
            atb.append(letra)
        else:
            atb.append(reverse[alfabeto.index(letra)])
    return atb


# PROGRAMA PRINCIPAL:

while True: 
    words = input("\n<()> Informe uma frase: ").lower()

    # DIGITAR N ou n fechará o programa
    if words in 'Nn': break

    var_atbash = atbash(words)

    print("-="*30, '\nOUTPUT:\n')
    for cont in var_atbash:
        print(cont, end='')
    print()
    print("-="*30)
