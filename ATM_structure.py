import random
class ATM:
    def lan(self):
        self.language =int(input("Enter a language:"
                                 "1.English"" "
                                 "2.Hindi"" "
                                 "3.Marathi : "))
        if self.language == 1:
            print("English")
        elif self.language == 2:
            print("Hindi")
        elif self.language == 3:
            print("Marathi")
        else:
            print("invalid language")


    def details(self):
        self.account_mode =int(input("Enter account type:"
                                     "1.Current Account "
                                     "2.Saving Account : "))
        if self.account_mode == 1:
            print("Current Account")
        elif self.account_mode == 2:
            print("Saving Account")
        else:
            print("Invalid account type")

    def pincode(self):
        self.pin = random.randrange(1000, 9999)
        print("The OTP is :",self.pin)

        while True:
            Pin = int(input("Enter OTP"))
            if self.pin == Pin:
                bal = 200000
                action = int(input("""Enter the input : 
1. Check Balance
2. Withdrawal Cash"""))
                if action == 1:
                    print("Your balance is : ",bal)
                elif action == 2:
                    amt = int(input("Enter the amount to be withdrawal : "))
                    b = bal - amt
                    print("Your current balance is : Rs.",b)
                break
            else:
                print("Enter OTP Again")

a=ATM()
a.lan()
a.details()
a.pincode()
