# Bank Project

This project is an Bank system simulator for managing debit cards. It allows you to create users, add cards to users, and perform transactions such as deposits and withdrawals.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AldoColl/python_certification_task2.git
cd python_certification_task2
```


2. Create a virtual environment (optional but recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the project dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the 'main.py' script to start the application:
```bash
python main.py
```

2. You will see a menu with options to perform different actions:
```bash
---- MENU ----
1. Add User
2. Add Card to User
3. Make Transaction
4. Delete User
5. Add Account
6. Edit Account
7. Delete Account
8. Delete Card from User
9. Exit
```
3. Enter the number corresponding to the action you want to perform and follow the prompts.

    - To add a new user, select option 1 and provide the user's name and email.
    - To add a card to a user, select option 2 and provide the user ID, account number, and initial balance.
    - To make a transaction (deposit or withdraw) for a card, select option 3 and follow the prompts.
    - To delete a user, select option 4 and provide the user ID to be deleted.
    - To add an account to a user, select option 5 and provide the user ID, account number, and initial balance.
    - To edit the balance of an account, select option 6 and provide the account number and the new balance.
    - To delete an account, select option 7 and provide the account number to be deleted.
    - To delete a card from a user, select option 8 and provide the card number to be deleted.
    - To exit the application, select option 9.