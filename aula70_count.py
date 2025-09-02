frase = "Python é uma linguagem de programação multiparadigma." 
        

max_letra = 0
quant_letra = 0

for letra in frase:
    
    if letra == ' ':
        continue
    quant_letra = frase.count(letra)
    
    if  quant_letra > max_letra:
        max_letra = quant_letra
        mais_letras = letra

print(f'A letra que mais apareceu na frase é: {mais_letras} e tem {max_letra} ocorrências.')

