import random

def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (1 - 20)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")
    
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 20, 7
    elif choice == "2":
        return 50, 6
    else:
        return 100, 5


def play_game():
    max_range, attempts = choose_difficulty()
    secret_number = random.randint(1, max_range)
    
    score = 100
    print(f"\nI have chosen a number between 1 and {max_range}.")
    print(f"You have {attempts} attempts.\n")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Numbers only!")
            continue

        attempts -= 1
        score -= 10

        if guess == secret_number:
            print(f"\n🎉 Correct! You guessed it!")
            print(f"🏆 Final Score: {score}")
            break
        else:
            if attempts == 0:
                print("\n💀 Game Over!")
                print(f"The number was: {secret_number}")
                break

            if secret_number % 2 == 0:
                print("🔍 Hint: The number is EVEN.")
            else:
                print("🔍 Hint: The number is ODD.")

            if abs(secret_number - guess) <= 5:
                print("🔥 You are VERY close!")
            else:
                print("❄️ You are far away!")

            print(f"Attempts left: {attempts}\n")


def main():
    print("🎮 WELCOME TO THE GUESSING GAME 🎮")
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for playing 👋")
            break


main()
