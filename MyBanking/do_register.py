#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog
from helperRegEx import Validator
from model_account import Account
from model_account_manager import AccountManager

TAG = "DO_REGISTER"
mlog.debug(TAG, "Trying to register new user..")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

print("<div id=\"entry\" >")
print("<h4> Register new user status:</h4><br><br>")
print("</div>")

full_name = ""
login_name = ""
login_key = ""
login_key_confirm = ""
account_number = 0
bank_name = ""
branch_name = ""
ifsc_code = ""
mlog.debug(TAG,"Fetching form values..")
try:
    form_entries = cgi.FieldStorage()
    full_name = form_entries.getvalue("full_name")
    login_name = form_entries.getvalue("login_name")
    login_key = form_entries.getvalue("login_key")
    login_key_confirm = form_entries.getvalue("login_key_confirm")
    account_number = form_entries.getvalue("account_number")
    bank_name = form_entries.getvalue("bank_name")
    branch_name = form_entries.getvalue("branch_name")
    ifsc_code = form_entries.getvalue("ifsc_code")
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

#if invalid attributes, show error and eixt.
error_message = None
if(full_name == None or login_name == None or login_key == None or login_key_confirm == None or account_number == None or bank_name == None or branch_name == None or ifsc_code == None) :
    error_message = "<br><p>Failed to register! Invalid attributes provided. Register again with valid attributes</p>"
else:
    register_validator = Validator()
    if register_validator.validate_generic_name(full_name,6,15) == False:
        error_message = register_validator.message
    elif register_validator.validate_login_name(login_name,6,15) == False:
        error_message = register_validator.message
    elif register_validator.validate_login_key(login_key,6,12) == False:
        error_message = register_validator.message
    elif login_key != login_key_confirm:
        error_message = "<P>Passwords do not match!</p>"
    elif int(account_number)<10000 or int(account_number) > 999999:
        error_message = "<P>Account number must be greater than 10000 and less than 999999!</p>"
    elif register_validator.validate_bank_name(bank_name,3,10) == False:
        error_message = register_validator.message
    elif register_validator.validate_branch_name(branch_name,5,10) == False:
        error_message = register_validator.message
    elif register_validator.validate_ifsc_code(ifsc_code) == False:
        error_message = register_validator.message

mlog.error(TAG,"Register validator error message: " + str(error_message))
if error_message != None:
    print('''
        <p>Failed to register:</p>
        <div id="entry" >
    ''')
    print(error_message)
    print('''
        </div>
        <div id="entry" >
            <a href="show_register.py">Register</a>
        </div>
        <div id="entry" >
            <a href="index.py">Sign In</a>
        </div>
    ''')
    print(helperHTML.get_html_end_preset())
    sys.exit()

try:
    mlog.debug(TAG, "Establishing database connection..")
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:
    mlog.error(TAG,"Unable to conenct to MyBanking Database:" +  str(e))
    print('''
            <h4>Unable to conenct to MyBanking Database.</h4>
            <div id="entry" >
                <a href="show_dashboard.py">BACK</a>
            </div>
        ''')
    print(helperHTML.get_html_end_preset())
    sys.exit()

register_failed = False
error_message = ""
try:
    sql_insert = "INSERT INTO user(login_name,login_key,account_number,session)"
    sql_insert += " VALUES('"+login_name+"', '"+login_key+"', "+account_number+", 0)"
    conn.query(sql_insert)

    obj_account = Account()
    obj_account.set(account_number,full_name,bank_name,bank_name,ifsc_code,0)
    obj_account_manager = AccountManager()
    obj_account_manager.initialize()
    obj_account_manager.register_new_account(obj_account)
    obj_account_manager.finalize()
    if obj_account_manager.transaction_success == False:                  
        error_message = obj_account_manager.transaction_message
        mlog.error(TAG,"Error: " + error_message)
        register_failed = True
        #Drop entry made just before to user table..
        sql_delete = "DELETE FROM user WHERE login_name='"+login_name+"';"
        conn.query(sql_delete)
except Exception as e:
    error_message = str(e)
    mlog.error(TAG,"Error: " + error_message)
    register_failed = True

conn.close()
print('''<div id="entry" >''')
if(register_failed == True):
    print("<br><p>Failed to register! "+error_message+". Register again.</p>")        
else:
    print("<br><p>Congratulations. Registration successfull!</p>")
print("</div>")
print('''
    <div id="entry" >
        <a href="show_register.py">Register</a>
    </div>
    <div id="entry" >
        <a href="index.py">Sign In</a>
    </div>
''')

print(helperHTML.get_html_end_preset())

