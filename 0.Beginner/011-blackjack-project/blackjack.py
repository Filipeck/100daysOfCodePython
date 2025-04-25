import random
from art import logo

def deal_card():
    """Retorna uma carta aleatória do baralho"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# vamos criar uma função para calcular o score, verificar se houve blackjack(quando o total é 21 com apenas 2 cartas)
def calculate_score(cards: list):
    """Recebe uma lista de cartas e retorna o cálculo da soma dessas cartas"""
    total_hand = sum(cards)
    if total_hand == 21 and len(cards) == 2:
        return 0

    if total_hand > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return total_hand

def check_winner(u_score, dealer_score):
    if u_score == dealer_score:
        return "É um empate! 😶"
    elif dealer_score == 0:
        return "Você perdeu! A mesa tem um Blackjack! 😱"
    elif u_score == 0:
        return "Você ganhou com um BLACKJACK! 😎"
    elif u_score > 21:
        return "Você passou de 21 e perdeu! 😥"
    elif dealer_score > 21:
        return "A mesa passou de 21 e você VENCEU! 🤩"
    elif u_score > dealer_score:
        return "Você VENCEU! 🥳"
    else:
        return "Você perdeu! 😵"

def play_game():
    print(logo)
    # criaremos 2 variáveis para armazenar as cartas do usuário e do computador/dealer
    user_cards = []
    computer_cards = []

    user_score = -1
    computer_score = -1
    is_game_over = False

    # sorteamos 2 cartas aleatórias para o usuário e o computador/dealer
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Sua mão: {user_cards}, pontuação atual: {user_score}')
        print(f'Carta desvirada da mesa: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_continue = input("Gostara de pegar uma nova carta? Digite 's' para sim e 'n' para encerrar a jogada:\n").lower()
            if user_continue in 'sim':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # na regra do blackjack, enquanto o dealer tiver uma mão menor que 17, ele precisará comprar até conseguir 17 ou mais
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Sua mão final: {user_cards}. Sua pontuação final: {user_score}")
    print(f"Mão final da mesa: {computer_cards}. Pontuação final da mesa: {computer_score}")
    print(check_winner(user_score, computer_score))

while input("Gostaria de começar um novo jogo? Digite 's' ou 'n.\n").lower() in 'sim':
    print('\n' * 40)
    play_game()

print("Obrigado por jogar Blackjack, até a próxima!")