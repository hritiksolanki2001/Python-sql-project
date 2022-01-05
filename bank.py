import mysql.connector as mc
db = mc.connect(host = 'localhost', user = 'root', password = '*B2i9#ren0',database ='customeraccount')
cur = db.cursor()

class bank:
    __interest_rate = 12
    __bank_name = "Bro Bank Pvt. Ltd."

    def __init__ (self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = 0

    def check_balance(self):
        print(f"Current balance is {self.balance}")

    def deposit_balance(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        
        else: 
            print("Enter a valid amount.")

        self.check_balance()

    def withdraw_balance(self, amount):
        if amount < 0 or amount > self.balance:
            print("Enter a valid amount.")
        
        else:
            self.balance = self.balance - amount

        self.check_balance()

    @classmethod

    def get_interest_rate(cls):
        print(f"Bank's current interest rate is {bank.__interest_rate}")
        
    
    @classmethod
    
    def get_bank_name(cls):
        return cls.__bank_name

    @staticmethod
    
    def print_holiday():
        print("There is a holiday on Dasain for 5 days.")
        print("To get notice on different holiday, please look at the national calendar.")


# def sub():
#     f = input("Enter your first name: ")
#     l = input("Enter your last name: ")
#     g = int(input("Enter your age: "))
#     u = int(input("enter your accout number:  "))
#     p = input("enter your password:  " )
#     s = 'INSERT INTO customeraccount.login values(%s,%s)'
#     user = bank(f, l , g)
#     t = (u, p,)
#     cur.execute(s, t)
#     db.commit()
#     print("You have successfully registered your account info.")
#     print("Enter 1 to check your balance, 2 to make a deposit, 3 to withdraw, 4 to check interest rate and 5 to check the list of holidays.")
#     inin = int(input())
    # if inin == 1:
    #     check_balance()
    # elif inin == 2:





# def main():
#     a = int(input("your accountnumber: "))
#     b = input("your password: ")

#     query = "SELECT * FROM login"
#     cur.execute(query)
#     rez = cur.fetchall()

#     for el in rez:
#         i = 0
#         if el[0] == a and el[1] == b:
#             print("Congratulations!, You are successfully logged in.")
#             i += 1
#             break
#         else:
#             pass
             
#     if i == 0:
#         print("Sorry!, You have entered incorrect account number and password.")
#     else:
#         pass

print(f"************************************************* Welcome to {bank.get_bank_name()} ******************************************")
print("Do you have Bro bank account?")
print("enter 'Y' if you have account or enter 'N' if you want to register?")
entered = input()
if entered == "Y" or entered == "y":
    print("Please answer the following to verify your account info.")
    f = input("Enter your first name: ")
    l = input("Enter your last name: ")
    g = input ("Enter your age: ")
    a = int(input("your accountnumber: "))
    b = input("your password: ")
    user = bank(f,l,g)

    query = "SELECT * FROM login"
    cur.execute(query)
    rez = cur.fetchall()

    for el in rez:
        i = 0
        if el[0] == a and el[1] == b:
            print("Congratulations!, You are successfully logged in.")
            i += 1
            break
        else:
            pass
             
    if i == 0:
        print("Sorry!, You have entered incorrect account number and password.")
    else:
        j = 0
        while j == 0:
            print("Enter 1 to check your balance. \nEnter 2 to make a deposit.\nEnter 3 to withdraw.\nEnter 4 to check interest rate.\nEnter 5 to check the list of holidays.\nEnter 6 to log out.")
            inin = int(input())
            if inin == 1:
                user.check_balance()
            elif inin == 2:
                print("Enter amount you would like to deposit.")
                amount = int(input())
                user.deposit_balance(amount)
            elif inin == 3:
                print("Enter the amount you want to withdraw.")
                amount = int(input())
                user.withdraw_balance(amount)
            elif inin == 4:
                user.get_interest_rate()
            elif inin == 5:
                user.print_holiday()
            elif inin == 6:
                print("You are logged out.")
                j += 1
            else:
                print("Invalid input.\nEnter only one numbers among 1,2,3,4,5,6.")

    # main()

else:
    f = input("Enter your first name: ")
    l = input("Enter your last name: ")
    g = int(input("Enter your age: "))
    a = int(input("enter your accout number:  "))
    b = input("enter your password:  " )
    user = bank(f, l, g)
    query = "SELECT * FROM login"
    cur.execute(query)
    rez = cur.fetchall()

    for el in rez:
        i = 0
        if el[0] == a and el[1] == b:
            print("***********This account info has already been registered************.\nWelcome to the bank service.")
            i += 1
            break
        else:
            pass
    if i == 0:
        s = 'INSERT INTO customeraccount.login values(%s,%s)'
        user = bank(f, l , g)
        t = (a, b)
        cur.execute(s, t)
        db.commit()

        print("*********You have successfully registered your account info.************")
        i = 0
        while i == 0:
            print("Enter 1 to check your balance. \nEnter 2 to make a deposit.\nEnter 3 to withdraw.\nEnter 4 to check interest rate.\nEnter 5 to check the list of holidays.\nEnter 6 to log out.")
            inin = int(input())
            if inin == 1:
                user.check_balance()
            elif inin == 2:
                print("Enter amount you would like to deposit.")
                amount = int(input())
                user.deposit_balance(amount)
            elif inin == 3:
                print("Enter the amount you want to withdraw.")
                amount = int(input())
                user.withdraw_balance(amount)
            elif inin == 4:
                user.get_interest_rate()
            elif inin == 5:
                user.print_holiday()
            elif inin == 6:
                print("You are logged out.")
                i += 1
            else:
                print("Invalid input.\nEnter only one numbers among 1,2,3,4,5,6.")
    else:
        k = 0
        while k == 0:
            print("Enter 1 to check your balance. \nEnter 2 to make a deposit.\nEnter 3 to withdraw.\nEnter 4 to check interest rate.\nEnter 5 to check the list of holidays.\nEnter 6 to log out.")
            inin = int(input())
            if inin == 1:
                    user.check_balance()
            elif inin == 2:
                print("Enter amount you would like to deposit.")
                amount = int(input())
                user.deposit_balance(amount)
            elif inin == 3:
                print("Enter the amount you want to withdraw.")
                amount = int(input())
                user.withdraw_balance(amount)
            elif inin == 4:
                user.get_interest_rate()
            elif inin == 5:
                user.print_holiday()
            elif inin == 6:
                print("You are logged out.")
                k += 1
            else:
                print("Invalid input.\nEnter only one numbers among 1,2,3,4,5,6.") 

   


        




