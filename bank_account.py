program_working = True
current_account = 0
accounts = []
start_text = "What would you like to do:" \
             "\n1 - Show all accounts\n" \
             "2 - Select an Account\n" \
             "3 - Deposit to an Account\n" \
             "4 - Get Account Balance\n" \
             "5 - Add an Account\n" \
             "6 - Exit Program\n"


class Account:
    _balance = 0.0
    _owner = ""
    _type = ""

    def __init__(self, name, issue):
        self._owner = name
        self._type = issue

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner

    def get_type(self):
        return self._type

    def set_balance(self, money):
        self._balance = money

    def deposit(self, money):
        current = self.get_balance()
        updated = current + money
        return self.add_to_balance(updated)

    def add_to_balance(self, amount):
        self.set_balance(amount)
        return amount


def show_all_account():
    if len(accounts) > 0:
        counter = 0
        for account in accounts:
            print("Name: ("+str(counter)+")" + account.get_owner()
                + "("+account.get_type()+") | ["
                + str(account.get_balance()) + "]")
            counter = counter +1
    else:
        print("You have no accounts\n")
        

def get_total_accounts():
    return len(accounts)


def select_account():
    global current_account
    account = input("What account are you select?\n")
    selected_account = int(account)
    if get_total_accounts() > 0:
        print(accounts[selected_account].get_owner() + " account selected\n")
        current_account = selected_account
    else:
        print("YOu have no accounts\n")


def is_account_selected():
    if get_total_accounts() > 0:
        return True
    else:
        return False


def add_account():
    global current_account
    name = input("Account name: \n")
    desc = input("Account Type:\n")
    account = Account(name, desc)
    accounts.append(account)
    current_account = len(accounts) - 1


def deposit_account():
    if is_account_selected():
        amount = int(input("Amount to add: \n"))
        account = get_account()
        account.deposit(amount)
        print(str(amount) + " Added to your account\n")
    else:
        print("No account selected\n")


def get_account():
    return accounts[current_account]


def account_balance():
    if is_account_selected():
        account = get_account()
        print("You account balance is " + str(account.get_balance()) + "\n")
    else:
        print("NO account selected\n")


def add_default_account():
    account = Account("Barry More", "Savings")
    account.deposit(500)
    accounts.append(account)


def run_program():
    option = input(start_text)
    number = int(option)
    if number == 1:
        show_all_account()
    elif number == 2:
        select_account()
    elif number == 3:
        deposit_account()
    elif number == 4:
        account_balance()
    elif number == 5:
        add_account()
    else:
        global program_working
        program_working = False


add_default_account()

while program_working:
    run_program()
