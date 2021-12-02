class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    #def display_user_balanceself:


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
javi = User("Javier Vieyra", "Javier@dojo.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_withdrawal(50)
print(guido.account_balance)

monty.make_deposit(50)
monty.make_deposit(500)
monty.make_withdrawal(250)
print(monty.account_balance)

javi.make_deposit(900)
javi.make_withdrawal(100)
javi.make_withdrawal(150)
javi.make_withdrawal(200)
print(javi.account_balance)


