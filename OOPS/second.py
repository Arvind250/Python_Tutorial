class Account:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
    def credit (self,amount):
        self.balance +=amount
        print("The balance after crediting amount ",amount," is ",self.balance)
    def debit (self,amount):
        self.balance -=amount
        print("The balance after debiting amount ",amount," is ",self.balance)
user1=Account(1,10000)
user1.credit(500)
user1.debit(200)