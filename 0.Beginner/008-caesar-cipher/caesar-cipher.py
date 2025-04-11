from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text: # percorremos cada letra do texto informado pelo usuário
        if letter in alphabet: # se a letra estiver contida na lista alphabet, seguiremos com a transformação dela
            shifted_position = alphabet.index(letter) + shift_amount # buscamos o index na lista e aplicamos os passos necessários
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter # caso não esteja na lista alfabeto, o caracter não será tratado e será adicionado em sua forma original na string

    print(f"Here is the {encode_or_decode}d result: {output_text}")

# iniciando o programa
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        pass
    else:
        print("Please, insert a valid option!")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    choice = input("If you would like to go again, type 'yes'. Otherwise, type 'no':\n").lower()
    if choice in 'yes':
        continue
    else:
        break

print("Thanks for using the Caesar Cipher Programa, \nCreated by: Filipe Cayres")

