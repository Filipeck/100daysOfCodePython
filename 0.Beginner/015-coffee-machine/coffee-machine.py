MENU = {
    "espresso": {
        "ingredients": {
            "agua": 50,
            "cafe": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}


def is_resource_sufficient(order_ingredients):
    """Retorna True quando o pedido pode ser feito, False se não houver ingredientes suficientes."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Desculpe não há {item} o suficiente para produzir esta bebida.")
            return False
    return True


def process_coins():
    """Retorna o total calculado das moedas inseridas."""
    print("Por favor, insira as moedas.")
    total = int(input("Quantas moedas de 50 centavos?: ")) * 0.5
    total += int(input("Quantas moedas de 25 centavos?: ")) * 0.25
    total += int(input("Quantas moedas de 10 centavos??: ")) * 0.1
    total += int(input("Quantas moedas de 5 centavos??: ")) * 0.05
    return total


def is_transaction_successful(money_received, drink_cost):
    """Retorna True quando o pagamento é aceito, False se o pagamento for insuficiente."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"O troco é de R${change:.2f}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Desculpe, o valor inserido não é o suficiente. Dinheiro retornado.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Reduz os ingredientes necessários da variável resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui está o seu {drink_name} ☕️. Aproveite!\n")


is_on = True

while is_on:
    choice = input("O que você gostaria de pedir? \nEspresso: R$1.50\nLatte R$2.50\nCappuccino R$ 3.00: ").lower().strip()
    if choice not in MENU and choice != "report":
        is_on = False
        print('Obrigado pela preferência, até breve! 🙋')
    elif choice == "report":
        print(f"Água: {resources['agua']}ml")
        print(f"Leite: {resources['leite']}ml")
        print(f"Café: {resources['cafe']}g")
        print(f"Saldo: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

