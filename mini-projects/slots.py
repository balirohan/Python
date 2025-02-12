# Python Slot Machine

import random, time

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")
    print()

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row == "⭐":
            return bet * 20
    return 0

def spinning_loader():
    print("Spinning", end="", flush=True)
    time.sleep(0.5)

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print("\n")

def main():
    balance = 100

    print("************************")
    print("Weclome to Python Slots!")
    print("Symbols: 🍒 🍉 🔔 ⭐ 🍋")
    print("************************")
    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        # spinning_loader()
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout:.2f}")
        else:
            print("Sorry you lost this round.")
        balance += payout

        if balance > 0:
            play_again = input("Do you want to spin again? (y/n): ").lower()
            if play_again != "y":
                break
        else:
            break

    print()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    print(f"Game Over! Your final balance is ${balance:.2f}")
    print()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()

if __name__ == '__main__':
    main()