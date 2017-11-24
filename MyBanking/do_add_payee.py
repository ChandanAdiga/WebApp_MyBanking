#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog
from helperRegEx import Validator

TAG = "DO_ADD_PAYEE"
mlog.debug(TAG, "Trying to add payee..")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

#Validate session..
if(helperSession.any_session_active() == False):
    #Show session inactive..
    mlog.debug(TAG,"In do_add_payee with no active session. So prompting to sign in again..")
    print(helperHTML.get_html_invalid_session_preset())
    print(helperHTML.get_html_end_preset())
    sys.exit()

account_number = helperSession.get_session_accout_no()
payee_name = ""
payee_account = 0
payee_bank = ""
payee_branch = ""
payee_ifsc_code = ""
mlog.debug(TAG,"Fetching form values..")
try:
    form_entries = cgi.FieldStorage()
    payee_name = form_entries.getvalue("payee_name")
    payee_account = form_entries.getvalue("payee_account")
    payee_bank = form_entries.getvalue("payee_bank")
    payee_branch = form_entries.getvalue("payee_branch")
    payee_ifsc_code = form_entries.getvalue("payee_ifsc_code")
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

#--------------------------------------------MENU DETAILS----------------------------------------------------
#Show MENU..
print('''
        <div id="entry" >
            <a id="dashboard_menu_a" href="show_dashboard.py">DASHBOARD</a>
            <a id="dashboard_menu_a" href="show_add_payee.py">Add Payee</a>
            <a id="dashboard_menu_a" href="show_remove_payee.py">Remove Payee</a>
            <a id="dashboard_menu_a" href="show_deposit_money.py">Deposit Money</a>
            <a id="dashboard_menu_a" href="show_money_transfer.py">Money Transfer</a>
            <a id="dashboard_menu_a" href="logout.py">Logout</a>
        </div>
    ''')
print("<div id=\"entry\" >")
print("<h4> Add Payee status:</h4><br><br>")
print("</div>")
#------------------------------------------------------------------------------------------------------------

error_message = None
if(payee_name == None or payee_account == None or payee_bank == None or payee_branch == None) or payee_ifsc_code == None:
    error_message = "<br><p>Failed to add payee! Invalid attributes provided. Add payee again with valid attributes</p>"
else:
    payee_validator = Validator()
    if payee_validator.validate_generic_name(payee_name,6,15) == False:
        error_message = payee_validator.message
    elif int(payee_account)<10000 or int(payee_account) > 999999:
        error_message = "<P>Account number must be greater than 10000 and less than 999999!</p>"
    elif payee_validator.validate_bank_name(payee_bank,3,10) == False:
        error_message = payee_validator.message
    elif payee_validator.validate_branch_name(payee_branch,5,10) == False:
        error_message = payee_validator.message
    elif payee_validator.validate_ifsc_code(payee_ifsc_code) == False:
        error_message = payee_validator.message

mlog.error(TAG,"Add payee validator error message: " + str(error_message))
if error_message != None:
    print('''
        <div id="entry" >        
            <p>Failed to add payee:</p>
            <div id="entry" >
    ''')
    print(error_message)
    print('''</div></div>''')
    print(helperHTML.get_html_end_preset())
    sys.exit()


try:
    mlog.debug(TAG, "Establishing database connection..")
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:
    mlog.error(TAG,"Unable to conenct to MyBanking Database.")
    print('''
            <h4>Unable to conenct to MyBanking Database.</h4>
            <div id="entry" >
                <a href="show_dashboard.py">BACK</a>
            </div>
        ''')
    print(helperHTML.get_html_end_preset())
#    print(e)
    sys.exit()

all_recs = None
add_payee_failed = False
try:
    sql_insert = "INSERT INTO payee_list(payee_name,owner_account,payee_account,payee_bank,payee_branch,payee_ifsc_code)"
    sql_insert += " VALUES('"+ payee_name +"', "+ str(account_number) +", "+ payee_account +", '"+ payee_bank +"', '"+ payee_branch +"', '"+ payee_ifsc_code +"')"
    conn.query(sql_insert)
    all_recs = conn.store_result()
except Exception as e:
    add_payee_failed = True
    mlog.error(TAG,"Unable to add payee to database:"+str(e))

print('''<div id="entry" >''')
print('''<div id="entry" >''')# to give a margin.
if(add_payee_failed == True) :
    print("<br><p>Unable to add payee to MyBanking Database.!</p>")        
else:
    print("<br><p>Successfully added payee!</p>")
print("</div>")
print("</div>")

conn.close()
print(helperHTML.get_html_end_preset())

