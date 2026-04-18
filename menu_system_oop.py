class Bank:
    def __init__(self,name,balance,pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.history = []
        

    def show_balance(self):
         print("balance:", self.balance)
         
    def deposit(self,amount):
        self.balance += amount
        self.history.append(f"deposit {amount}")
        print("deposited:", amount)
    
         
         
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"withdraw {amount}")
            print("withdrwan:", amount)
        else:
            print("insufficient balance")

    def show_history(self):
        print("Transaction history: ")
        for h in self.history:
            print(h)
            
b1 = Bank("neeraja", 1000,1234)
b2 = Bank("ravi", 2000,5678)

print("select user:")
print("1.neeraja")
print("2.ravi")

choice = int(input("enter choice: "))

if choice == 1:
    user = b1
elif choice == 2:
    user = b2
else:
    print("invalid balance")
    exit()
    
entered_pin = int(input("enter pin: "))

if entered_pin != user.pin:
    print("wrong pin ")
    exit()
else:
    print("login successful")

while True:

    print("1. check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.show history")
    print("5.exit")

    option = int(input("enter option: "))

    if option == 1:
        user.show_balance()
        
    elif option == 2:
        amount = int(input("enter amount: "))   
        user.deposit(amount)
        
    elif option == 3:
        amount = int(input("enter amount: "))  
        user.withdraw(amount)
        
    elif option == 4:
        user.show_history()
        
    elif option == 5:
        print("thank you")
        break
    else:
        print("invalid option")




 


         
