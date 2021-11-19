
#Leon's solution

#Goal: “Create a Budget class that can instantiate objects based on different budget categories  
#   - create class that will make a few objects
#   - cat1 = class()
#   - cat2 = class()
#like food, clothing, and entertainment.

# These objects should allow for depositing and withdrawing funds from each category, 
#  - actions, therefore i need to write methods
# def deposit() withdraw()

# as well computing category balances and 
# - Classes are not just code, they are also data! Therefore a balance variable.
# - all transactions must use the balance var

# transferring balance amounts between categories”
# - what info do I need? 
#   - from cat name - this is the object we created
#   - to cat name  - this is the deposit method in another class object
#   - balance amount


import pdb
pdb.set_trace()



class Budget:

    def __init__(self):
        self.balance = 0.0
    
    def deposit(self,moneyin):
        self.balance += moneyin
    
    def withdraw(self,moneyout):
        self.balance -= moneyout

    def transferto(self,account,value):
        self.withdraw(value)
        account.deposit(value)



food = Budget()
clothes = Budget()
house = Budget()
entertainment = Budget()
pets = Budget()

pets.deposit(120)


food.deposit(100)
food.withdraw(1.99)

print("food", food.balance)

food.transferto(clothes, 30)

print("food:", food.balance)
print("clothes:",clothes.balance)

clothes.transferto(house, 15)
print("clothes:",clothes.balance)
print("house:",house.balance)

total = 0

for i in [food,clothes,house]:
    total += i.balance
print(total)