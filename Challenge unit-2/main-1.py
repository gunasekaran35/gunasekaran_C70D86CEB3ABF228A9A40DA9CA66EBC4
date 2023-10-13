class BankAccount:
 def __init__(self,accountnumber,accountholdername,initialbalance=0.0):
  self .__accountnumber=accountnumber
  self.__accountholdername=accountholdername
  self.__accountbalance=initialbalance
 def deposit(self,amount):
    if amount >0:
      self.__accountbalance+=amount
      print("Deposit ₹{}.New balance: ₹. {}".format(amount,self.__accountbalance))
    
    else:
      print("invalid deposit amount")
 def withdraw(self,amount):
   if amount > 0 and amount< self.__accountbalance:
      self.__accountbalance-=amount
      print("Withdraw ₹{}.New balance: ₹{}   ".format(amount,self.__accountbalance))
   else:
     print("insuficiant balance.")
 def displaybalance(self):
     print("Account balance for {}(Account #{}): ₹{}".format(self.__accountholdername,self.__accountnumber,self.__accountbalance))
account=BankAccount(accountnumber="1234566889",accountholdername="jb",initialbalance=5000.0)
account.displaybalance()
account.deposit(500.0)
account.withdraw(200.0)