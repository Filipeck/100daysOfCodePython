from art import logo

print(logo)
bids = {}
biggest_bet = 0
biggest_bidder = ""
flow = True

while flow:
    bidder = input('Informe o nome do apostador:\n').title().strip()
    bid_amount = float(input("Informe o valor em R$").strip())
    bids[bidder] = bid_amount

    new_bidder = input("Você gostaria de fazer um novo lance? [S] | [N]\n").upper()
    if new_bidder == "S":
        print("\n" * 40)
        continue
    else:
        flow = False

# vamos descobrir agora qual foi o maior lance
for bid in bids:
    if bids[bid] > biggest_bet:
        biggest_bet = bids[bid]
        biggest_bidder = bid

print(f"{biggest_bidder} deu o maior lance do leilão, no valor de R${biggest_bet:.2f}")
