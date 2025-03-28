print("Bem-vindo(a) ao simulador de gorjeta!")
conta = float(input("Qual o valor total da conta: R$"))
gorjeta = int(input("Qual o percentual de gorjeta que você irá pagar? "))
pessoas = int(input("Quantas pessoas dividirão a conta? "))

gorjeta_total = round(conta *(gorjeta / 100), 2)
total_pagar = round(conta + gorjeta_total, 2)
total_pessoa = round((conta / pessoas) * (1 + gorjeta / 100), 2)

print("=+" * 20 + f"\nResumo da conta:\nConta: R${conta:.2f}\nGorjeta: R${gorjeta_total:.2f}\n"
      f"Total a pagar: R${total_pagar:.2f}\nPreço por pessoa ({pessoas}): R${total_pessoa:.2f}\n" + "=+" * 20)
