from atm_service import ATMService

def show_menu():
    print("\n====== ATM MENU ======")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

def main():
    atm = ATMService()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.display_balance()

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)

        elif choice == "4":
            atm.show_statement()

        elif choice == "5":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()