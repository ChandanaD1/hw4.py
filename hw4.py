class ATM (object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number,
        self.pin_number = pin_number

    def Balance_Inquiry (self):
        print("Your balance: $100")
    
    def Cash_Withdrawl (self, amount):
        new_amount = 100-amount
        print("You withdrew: " + str(amount))
        print("Your balance: " + str(new_amount))

atm1 = ATM("100395820","4895")
print(atm1)