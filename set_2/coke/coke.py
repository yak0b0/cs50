def main():
    coke_game()


def coke_game():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin == 25:
            amount_due = amount_due - 25
        elif inserted_coin == 10:
            amount_due = amount_due - 10
        elif inserted_coin == 5:
            amount_due = amount_due - 5
        else:
            continue
    change_owed = amount_due * -1
    print("Change Owed:", change_owed)


main()
