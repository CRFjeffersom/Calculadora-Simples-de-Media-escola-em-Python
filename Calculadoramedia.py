print ('======== Calculadora de media escolar ========')
media1 = float (input('digite sua primeira mèdia aqui'))
media2 = float (input('digite sua segunda mèdia aqui'))
media3 = float (input('digite sua terceira mèdia aqui'))
media4 = float (input('digite sua quarta mèdia aqui'))
resultado = media1 + media2 + media3 + media4 /4
print (resultado)
if resultado > 7:
    print('Você passou')
elif resultado >= 6:
    print('Passou mas com recuperação')
else:
    print('Você foi reprovado')
