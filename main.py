from peewee import SqliteDatabase
from models.user import User
from models.account import Account
from models.card import Card

db = SqliteDatabase('python_certification_task2.db')

def add_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    phone = input("Enter user phone: ")
    user = User.create(name=name, email=email, phone=phone)
    print(f"User '{user.name}' with email '{user.email}' and phone '{user.phone}'added.")

def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    try:
        user = User.get(User.id == user_id)
        user.delete_instance()
        print(f"User '{user.name}' with ID {user_id} deleted.")
    except User.DoesNotExist:
        print("User with the specified ID does not exist.")

def add_account():
    user_id = int(input("Enter user ID to add an account: "))
    try:
        user = User.get(User.id == user_id)
        account_number = input("Enter account number: ")
        balance = float(input("Enter initial account balance: "))
        account = Account.create(user=user, account_number=account_number, balance=balance)
        print(f"Account '{account.account_number}' added to user '{user.name}' with balance {account.balance}.")
    except User.DoesNotExist:
        print("User with the specified ID does not exist.")


def add_card_to_user():
    user_id = int(input("Enter user ID: "))
    try:
        user = User.get(User.id == user_id)
        account_number = input("Enter account number: ")
        balance = float(input("Enter initial card balance: "))
        card = Card.create(account=user.account, card_number=account_number, balance=balance)
        print(f"Card '{card.card_number}' added to user '{user.name}' with balance {card.balance}.")
    except User.DoesNotExist:
        print("User with the specified ID does not exist.")

def edit_account():
    account_number = input("Enter account number to edit: ")
    try:
        account = Account.get(Account.account_number == account_number)
        new_balance = float(input("Enter new account balance: "))
        account.balance = new_balance
        account.save()
        print(f"Account '{account.account_number}' balance updated to {account.balance}.")
    except Account.DoesNotExist:
        print("Account with the specified number does not exist.")

def delete_account():
    account_number = input("Enter account number to delete: ")
    try:
        account = Account.get(Account.account_number == account_number)
        account.delete_instance()
        print(f"Account '{account.account_number}' deleted.")
    except Account.DoesNotExist:
        print("Account with the specified number does not exist.")

def delete_card_from_user():
    card_number = input("Enter card number to delete: ")
    try:
        card = Card.get(Card.card_number == card_number)
        card.delete_instance()
        print(f"Card '{card.card_number}' deleted.")
    except Card.DoesNotExist:
        print("Card with the specified number does not exist.")



def make_transaction():
    card_number = input("Enter card number: ")
    try:
        card = Card.get(Card.card_number == card_number)
        amount = float(input("Enter transaction amount: "))
        transaction_type = input("Enter 'deposit' or 'withdraw': ").lower()
        if transaction_type == 'deposit':
            card.process_deposit(amount)
            print(f"Deposited {amount} to card '{card.card_number}'. New balance: {card.balance}.")
        elif transaction_type == 'withdraw':
            try:
                card.process_expense(amount)
                print(f"Withdrew {amount} from card '{card.card_number}'. New balance: {card.balance}.")
            except ValueError as e:
                print("Withdrawal failed:", e)
        else:
            print("Invalid transaction type.")
    except Card.DoesNotExist:
        print("Card with the specified number does not exist.")

def main():
    db.connect()

    db.create_tables([User, Account, Card])

    while True:
        print("\n---- MENU ----")
        print("1. Add User")
        print("2. Add Card to User")
        print("3. Make Transaction")
        print("4. Delete User")
        print("5. Add Account")
        print("6. Edit Account")
        print("7. Delete Account")
        print("8. Delete Card")
        print("9. Exit")


        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_card_to_user()
        elif choice == "3":
            make_transaction()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            add_account()
        elif choice == "6":
            edit_account()
        elif choice == "7":
            delete_account()
        elif choice == "8":
            delete_card_from_user()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    db.close()

if __name__ == "__main__":
    main()
