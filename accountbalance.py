class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("RS",amount,"was debited")
    
    def credit(self,amount):
        self.balance+=amount
        print("RS",amount,"was credited")
        






acc1=account(10000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.credit(1000)
acc1.debit(500)