#!/usr/bin/python3

import mlog

class Account():
    TAG = "Account"
    number=0
    name=""
    bank_name=""
    ifsc_code=""
    branch_name=""
    balance=0

    #Constructor. Usage: obj_acc = Account()
    def __init__(self):
        mlog.debug(self.TAG,"Constructor()")

    def set(self, acc_number,acc_name,bank,branch,ifsc,balance_amt=0):
        self.number = int(acc_number)
        self.name = acc_number
        self.bank_name = bank
        self.branch_name = branch
        self.ifsc_code = ifsc
        self.balance_amt = int(balance_amt)

    def deposit(self, amount):
        mlog.debug(self.TAG,"deposit("+str(amount)+")")
        if int(amount) > 0:
            self.balance += int(amount)

    def can_debit(self, amount):
        mlog.debug(self.TAG,"can_debit("+str(amount)+")")
        if int(amount) > 0 and int(balance)>int(amount):
            return True
        else:
            return False

    def debit(self,amount):
        mlog.debug(self.TAG,"debit("+str(amount)+")")
        if self.can_debit(amount):
            self.balance -= int(amount)
            return True
        else:
            return False

    def transfer_to(self, account, amount):
        mlog.debug(self.TAG,"transfer_to("+str(amount)+")")
        if account is None:
            mlog.debug(self.TAG,"transfer_to(None,"+str(amount)+") failed.!")
            return False
        if int(amount) <= 0:
            mlog.debug(self.TAG,"transfer_to("+str(account.number)+"," +str(amount)+ ") failed.")
            return False
        mlog.debug(self.TAG,"transfer_to("+str(account.number)+"," +str(amount)+ ")")
        transferred = self.debit(amount)
        mlog.debug(self.TAG,"Status of transfer:"+str(transferred))
        if transferred == True:
            mlog.debug(self.TAG,"Depositing to target account..")
            account.deposit(amount)
        mlog.debug(self.TAG,"Transfer process completed!")
        return transferred
   

