print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo(a) a ilha do tesouro!")
print("Sua missão nesta aventura é encontrar o tesouro.")
escolha1 = input("Você está na ilha em que dizem haver um tesouro. Na sua direita você avista uma floresta e na esquerda uma caverna. Qual caminho você escolhe? (direita/esquerda) ").lower()

if escolha1 == "direita":
    # escolha se o usuário escolheu a direita
    escolha2 = input("Você entrou na floresta e encontrou um rio. Você pode nadar ou construir uma jangada. O que você faz? (nadar/jangada) ").lower()
    if escolha2 == "nadar":
        print("Você foi atacado por um crocodilo. Fim de jogo.")
    elif escolha2 == "jangada":
        print("Você construiu uma jangada e atravessou o rio com segurança. Você encontrou o tesouro! Parabéns!")
    else:
        print("Escolha inválida. Fim de jogo.")
elif escolha1 == "esquerda":
    # escolha se o usuário escolheu a esquerda
    escolha2 = input("Você entrou na caverna e encontrou dois túneis. Um parece seguro e o outro está escuro e assustador. Qual você escolhe? (seguro/escuro) ").lower()
    if escolha2 == "seguro":
        print("O túnel seguro estava cheio de armadilhas. Fim de jogo.")
    elif escolha2 == "escuro":
        print("Você corajosamente entrou no túnel escuro e encontrou o tesouro! Parabéns!")
    else:
        print("Escolha inválida. Fim de jogo.")
else:
    print("Escolha inválida. Fim de jogo.")