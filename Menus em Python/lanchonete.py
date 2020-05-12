from os import system
from time import sleep

system('clear')

conf = 0
sel = 0
select = 0

burger = {'sr': 0, 'when': 0, 'mega': 0}
appetizer = {'batata': 0, 'nugget': 0, 'onion': 0}
drink = {'refri': 0, 'suco': 0, 'agua': 0}
prog = True

def confirm():
    print("\n---------------------------------------\n")
    print("Mais alguma coisa?")
    print("[1] - SIM, QUERO ESCOLHER OUTRO ITEM")
    print("[2] - NÃO, QUERO VOLTAR PARA O MENU PRINCIPAL")

def menu_inicial():
    system('clear')
    print("O que você deseja pedir?")
    print("[1] - Hamburgueres")
    print("[2] - Aperitivos")
    print("[3] - Bebidas")
    print("[4] - Nada =(")

def menu_final():
    system('clear')
    print("O que você deseja pedir?")
    print("[1] - Hamburgueres")
    print("[2] - Aperitivos")
    print("[3] - Bebidas")
    print("[4] - Nada =(")
    print("[5] - Finalizar Pedido")

def quantBurger():
    global select
    global conf
    print("\n---------------------------------------\n")
    quant = int(input("Quantos você vai querer? "))
    if select == 1:
        burger["sr"] = burger["sr"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            burgers()
    elif select == 2:
        burger["when"] = burger["when"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            burgers()
    elif select == 3:
        burger["mega"] = burger["mega"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            burgers()

def quantAppetizer():
    global select
    global conf
    print("\n---------------------------------------\n")
    quant = int(input("Quantos você vai querer? "))
    if select == 1:
        appetizer["batata"] = appetizer["batata"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            appetizers()
    if select == 2:
        appetizer["nugget"] = appetizer["nugget"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            appetizers()
    if select == 3:
        appetizer["onion"] = appetizer["onion"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            appetizers()

def quantDrink():
    global select
    global conf
    print("\n---------------------------------------\n")
    quant = int(input("Quantos você vai querer? "))
    if select == 1:
        drink["refri"] = drink["refri"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            drinks()
    if select == 2:
        drink["suco"] = drink["suco"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            drinks()
    if select == 3:
        drink["agua"] = drink["agua"] + quant
        confirm()
        conf = int(input())
        if conf == 1:
            drinks()

def burgers():
    global select
    system('clear')
    print("Escolha o que quer?")
    print("[1] - SHORT RODEIO             R$ 7.99")
    print("[2] - WHENPPER                 R$ 10.99")
    print("[3] - MEGA STACKER SUIÇO 5.0   R$ 15.99")
    print("[4] - VOLTAR")
    select = int(input())
    if (select == 1 or select == 2 or select == 3):
        quantBurger()
    elif select == 4:
        menu_final()

def appetizers():
    global select
    system('clear')
    print("[1] - BATATA FRITA             R$ 9.99")
    print("[2] - NUGGETS                  R$ 9.99")
    print("[3] - ONION RINGS              R$ 9.99")
    print("[4] - VOLTAR")
    select = int(input())
    if (select == 1 or select == 2 or select == 3):
        quantAppetizer();
    elif select == 4:
        menu_final()

def drinks():
    global select
    system('clear')
    print("[1] - REFRIGERANTE             R$ 4.99")
    print("[2] - SUCO                     R$ 3.99")
    print("[3] - ÁGUA                     R$ 2.99")
    print("[4] - VOLTAR")
    select = int(input())
    if (select == 1 or select == 2 or select == 3):
        quantDrink();
    elif select == 4:
        menu_final()

def finalizar_pedido():
    system('clear')

    valorBurger = 0
    valorAppetizer = 0
    valorDrink = 0
    valorTotal = 0

    if burger["sr"] > 0:
        valorBurger = valorBurger + (burger["sr"]*7.99)

    if burger["when"] > 0:
        valorBurger = valorBurger + (burger["when"]*10.99)

    if burger["mega"] > 0:
        valorBurger = valorBurger + (burger["mega"]*15.99)

    if appetizer["batata"] > 0:
        valorAppetizer = valorAppetizer + (appetizer["batata"]*9.99)

    if appetizer["nugget"] > 0:
        valorAppetizer = valorAppetizer + (appetizer["nugget"]*9.99)

    if appetizer["onion"] > 0:
        valorAppetizer = valorAppetizer + (appetizer["onion"]*9.99)

    if drink["refri"] > 0:
        valorDrink = valorDrink + (drink["refri"]*4.99)

    if drink["suco"] > 0:
        valorDrink = valorDrink + (drink["suco"]*3.99)

    if drink["agua"] > 0:
        valorDrink = valorDrink + (drink["agua"]*2.99)

    valorTotal = valorBurger + valorAppetizer + valorDrink
    print("Sua conta deu: R$ " + str(valorTotal))
    print("Volte sempre! <3")

print("Bem-Vindo ao BurgerQueen!!!\n")
def main():
    global prog
    global sel

    while prog:

        menu_inicial()
        sel = int(input('Escolha uma opção: '))

        while(sel <= 0 or sel >= 6):
            print("Opção inválida. Tente novamente!")
            menu_inicial()
            sel = int(input('Escolha uma opção: '))

        while(sel > 0 or sel < 6):
            if sel == 1:
                burgers()
                menu_final()
                sel = int(input('Escolha uma opção: '))

            if sel == 2:
                appetizers()
                menu_final()
                sel = int(input('Escolha uma opção: '))

            if sel == 3:
                drinks()
                menu_final()
                sel = int(input('Escolha uma opção: '))

            if sel == 4:
                system('clear')
                print("Obrigado pela preferência")
                sel = 0
                prog = False
                break

            if sel == 5:
                finalizar_pedido();
                sel = 0
                prog = False
                break

main();
