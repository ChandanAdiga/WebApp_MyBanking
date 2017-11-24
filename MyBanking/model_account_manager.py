#!/usr/bin/python3

import _mysql
import sys
import helperSession
import database.db_config as db_config
import mlog
import datetime
from model_account import Account

TAG = "ACC_MANAGER"
mlog.debug(TAG, "Account Manager")

class AccountManager():
    db_connection = None
    transaction_success = False
    transaction_message = ""
#----------------------------------------------------------------------------------
    def initialize(self):
        mlog.debug(TAG, "initialize()")
        transaction_success = False
        transaction_message = ""
        try:
            mlog.debug(TAG, "Establishing database connection..")
            self.db_connection = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
            transaction_success = True
        except Exception as e:
            mlog.error(TAG,"Unable to conenct to MyBanking Database.")
            transaction_message = '''
                <h4>Unable to conenct to MyBanking Database.</h4>
                <div id="entry" >
                    <a href="show_dashboard.py">BACK</a>
                </div>
            '''
        return transaction_success

#----------------------------------------------------------------------------------
    def register_new_account(self,account_obj):
        mlog.debug(TAG, "register_new_account()")
        self.transaction_success = False
        self.transaction_message = ""
        try:
            sql_insert = "INSERT INTO account(number,name,ifsc_code,bank_name,branch_name,balance)"
            sql_insert += " VALUES("+str(account_obj.number)+", '"+account_obj.name+"', '"+account_obj.ifsc_code+"', '"+account_obj.bank_name+"', '"+account_obj.branch_name+"',"+str(account_obj.balance)+")"
            self.db_connection.query(sql_insert)  
            self.transaction_success = True
            self.transaction_message = "Successfully registered new user!"
        except Exception as e:
            self.transaction_message = str(e)
            mlog.error(TAG,"Error: " + error_message)
        return self.transaction_success

#----------------------------------------------------------------------------------
    def get_account_details(self,account_number):
        mlog.debug(TAG, "get_account_details("+str(account_number)+")")
        self.transaction_success = False
        self.transaction_message = ""
        all_recs = None
        try:
            query_account = "SELECT name, number, ifsc_code, bank_name, branch_name, balance FROM account WHERE number="+str(account_number)+";"
            self.db_connection.query(query_account)
            all_recs = conn.store_result()
        except Exception as e:
            self.transaction_message = str(e)
            mlog.error(TAG,"Error: " + str(e))
        obj_account = None
        if all_recs != None and all_recs.num_rows() > 0 :
            row = all_recs.fetch_row()
            for item in row:
                obj_account = Account()
                obj_account.set(acc_number= int(str(item[1])),acc_name=str(item[0],'utf-8'),bank=str(item[3],'utf-8'),branch=str(item[4],'utf-8'),ifsc=str(item[2],'utf-8'),balance_amt=int(str(item[5])))
                self.transaction_success = True
                self.transaction_message = "Successfully fetched account details"
        else:
            self.transaction_success = False
            self.transaction_message = "Unable to fetch account details.."
        return obj_account

#----------------------------------------------------------------------------------
    def update_account_details(self,account_obj):
        mlog.debug(TAG, "set_account_details("+str(account_obj.number)+")")
        self.transaction_success = False
        self.transaction_message = ""
        all_recs = None
        try:
            query_update = "UPDATE account SET name='"+str(account_obj.name)+"', ifsc_code='"+str(account_obj.ifsc_code)+"', bank_name='"+str(account_obj.bank_name)+"', branch_name='"+str(account_obj.branch_name)+"', balance="+str(account_obj.balance)+" WHERE number="+str(account_obj.number)+";"
            self.db_connection.query(query_update)
            self.transaction_success = True
            self.transaction_message = "Successfully updated account details in DB."
        except Exception as e:
            self.transaction_message = str(e)
            mlog.error(TAG,"Error: " + str(e))
        return self.transaction_success
#----------------------------------------------------------------------------------
    def finalize(self):
        mlog.debug(TAG, "finalize()")
        if self.db_connection is not None:
            self.db_connection.close()
#----------------------------------------------------------------------------------

