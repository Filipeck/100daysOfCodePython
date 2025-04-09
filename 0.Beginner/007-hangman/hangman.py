import random, hangman_words, hangman_art

# Usamos a lista de palavras que estão no arquivo hangman_words.py e as imagens dos níveis na variável stages
# que está inclusa no arquivo hangman_art.py
word_list = hangman_words.word_list
stages = hangman_art.stages
lives = 6

# Importamos a logo de hangman_art.py e a imprimimos no início do jogo.
print(hangman_art.logo)
chosen_word = random.choice(word_list).casefold()

placeholder = "_" * len(chosen_word)
print("Adivinhe a palavra: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Informamos quantas vidas o jogador possui e solicitamos que ele insira uma letra
    print(f"**************************** {lives}/6 VIDAS RESTANTES****************************")
    guess = input("Insira uma letra: ").lower().strip()

    # Caso o usuário insira uma letra que já havia sido descoberta, o informaremos
    if guess in correct_letters:
        print(f"Você já digitou a letra '{guess}'")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Seu progresso até agora: " + display)

    # Se a letra escolhida não estiver na palavra sorteada reduzimos uma vida e informamos ao usuário o erro.

    if guess not in chosen_word:
        lives -= 1
        print(f"Você digitou a letra '{guess.upper()}', ela não está na palavra sorteada. Você perdeu uma vida!")

        if lives == 0:
            game_over = True
            # Com 0 vidas o jogo finaliza, informamos qual era a palavra correta e que o jogador perdeu o jogo.
            print(f"\nVocê não tem mais vidas restantes, a palavra era '{chosen_word}'\n***********************VOCÊ PERDEU!**********************")

    if "_" not in display:
        game_over = True
        print("****************************VOCÊ GANHOU!****************************")

    # Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])
