# irei tratar com métodos de string para que o nome saia da forma que desejamos (letra inicial maiúscula demais minúsculas).

print('=+'*30, '\nBem-vindo(a) ao Gerador de Nome de Bandas!', '\nPara que o nome seja gerado nos informe por favor:\n')
cidade = input('Qual o nome da cidade que você nasceu:\n').strip().casefold().title()
pet = input('Qual o nome do seu animal de estimação:\n').strip().casefold().title()

print('A sua banda será chamada de: ' + cidade + ' ' + pet, '=+'*30, sep='\n')