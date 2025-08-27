num_str = input('Digite um número inteiro: ')
if num_str.isdigit():
    num = int(num_str)
    resto = num % 2
    if resto == 0:
        mensagem= 'Número par'
    else:
        mensagem = 'Número ímpar'
else:
    mensagem = 'Não é um número inteiro'

print(mensagem)

hora = input('Informe a hora: ')
if hora.isdigit():
    hora_num = int(hora)
    if hora_num <=11:
        mensagem = 'Bom dia'
    elif hora_num>=12 and hora_num<= 17:
         mensagem = 'Boa tarde'
    elif hora_num > 17 and hora_num <= 23:
         mensagem = 'Boa noite'
else:
    mensagem = 'Não é uma hora válida.'

print(mensagem)