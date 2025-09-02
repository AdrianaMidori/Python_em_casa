palavra_secreta = 'ARMÁRIO'
numero_tentativas = 0
letras_acertadas = ''

while True:
    letra_informada = input('Digite apenas uma letra da palavra secreta ou [SAIR]: ').upper()
    if letra_informada == 'SAIR':
        print(f'Número de tentativas: {numero_tentativas}')
        break
    
    numero_tentativas += 1
    if len(letra_informada) > 1:
        print('Informe apenas uma letra.')
        continue

    if letra_informada in palavra_secreta:
        letras_acertadas += letra_informada

    nova_palavra = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            nova_palavra += letra
        else:
            nova_palavra += '*'

    print(f'Nova Palavra: {nova_palavra}')

    if nova_palavra == palavra_secreta:
        print(f'PARABÉNS! Você acertou, com {numero_tentativas} tentativas')
        print('A palavra era ', palavra_secreta)
        break
