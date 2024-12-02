import secrets

uppercase_letters = "QWERTZUIOPASDFGHJKLYXCVBNM"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.?!§#*+-_"

upper = True
lower = True
digit = True
symbol = True

password = ""

all = ""
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if digit:
    all += digits
if symbol:
    all += symbols

length = 15
amount = 5

for i in range(amount):
    password = ''.join(secrets.choice(all) for i in range(length))
    print(password)