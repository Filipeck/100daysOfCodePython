from random import randint as rd
from art import logo

print(logo)
print("Estou pensando em um número entre 1 e 100, você consegue descobrir qual é este número?")

def set_difficulty(difficult):
    if difficult == "D":
        return 5
    else:
        return 10

def check_answer(user_guess, correct_answer):

    if user_guess > correct_answer:
        return f"O número sorteado é menor do que {user_guess}!"
    
    elif user_guess < correct_answer:
        return f"O número sorteado é maior do que {user_guess}!"
    
    else:
        return f"Você ACERTOU! O número sorteado é {correct_answer}!"

def start_game(lives):
    count = 1
    random_number = rd(1,100)

    print(f"\nVocê tem {lives} tentativas!")

    while count <= lives:
        # Vamos verificar que o usuário informe um número, para evitar que o código quebre.
        while True:
            try:
                attempt = int(input("Adivinhe qual o número sorteado entre 1 e 100:\n"))
                break
            except:
                print("Você não inseriu um número válido, por favor informe um número!")

        # após a verificação, seguimos com o código
        print(check_answer(attempt, random_number))       

        if attempt == random_number: # caso verdadeiro o jogo se encerra
            break

        if lives - count > 0:
                print(f"Você tem mais {lives - count} tentativas!\n")
        else:
            print(f"Acabaram as suas tentativas, o número sorteado era {random_number}!\nFIM DE JOGO!")
        
        count += 1 # com isso controlamos a quantidade de vidas do usuário e garantimos o fim do jogo por falta de tentativas restantes

# Começando o jogo
challenge_lvl = set_difficulty(input("Escolha qual modo deseja jogar, Fácil [F] ou Difícil [D]:\n").upper().strip())

start_game(challenge_lvl)