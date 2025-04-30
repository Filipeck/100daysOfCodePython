from random import randint as rd
import art

print(art.logo)

def set_difficulty(difficult):
    if difficult == "D":
        return 5
    else:
        return 10

challenge_lvl = set_difficulty(input("Escolha qual modo deseja jogar, Fácil [F] ou Difícil [D]:\n").upper().strip())

def start_game(lives):
    count = 1
    random_number = rd(1,100)
    while count <= lives:
        attempt = int(input("Adivinhe qual o número sorteado entre 1 e 100:\n"))
        if attempt > random_number:
            print(f"O número sorteado é menor do que {attempt}!")
        elif attempt < random_number:
            print(f"O número sorteado é maior do que {attempt}!")
        else:
            print(f"Você ACERTOU! O número sorteado é {random_number}!")
            break

        if lives - count > 0:
                print(f"Você tem mais {lives - count} tentativas!\n")
        else:
            print(f"Acabaram as suas tentativas, o número sorteado era {random_number}!\nFIM DE JOGO!")
        
        count += 1

start_game(challenge_lvl)