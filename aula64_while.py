nome = input('Digite um nome: ')
tam_nome = len(nome)

if tam_nome > 0:
    contador = 0
    novo_nome = ''
    while contador < tam_nome:
        novo_nome += '*'+nome[contador]
        contador += 1
    print(novo_nome)
else:
    print('Nome digitado incorretamente.')
