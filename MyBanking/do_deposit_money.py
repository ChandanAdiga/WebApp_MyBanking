#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog
import datetime

TAG = "DO_DEPOSIT"
mlog.debug(TAG, "Trying to do deposit..")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

#Validate session..
if(helperSession.any_session_active() == False):
    #Show session inactive..
    mlog.debug(TAG,"In do_deposit_money with no active session. So prompting to sign in again..")
    print(helperHTML.get_html_invalid_session_preset())
    print(helperHTML.get_html_end_preset())
    sys.exit()

account_number = helperSession.get_session_accout_no()
deposit_amount = 0
mlog.debug(TAG,"Fetching form values..")
try:
    form_entries = cgi.FieldStorage()
    deposit_amount = form_entries.getvalue("deposit_amount")
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
print("<h4> Deposit money status:</h4><br><br>")
print("</div>")
#------------------------------------------------------------------------------------------------------------

error_message = None
if(deposit_amount == None) :
    error_message = "<br><p>Failed to deposit amount. No balance value provided! Make sure balance is greater than 0.</p>"
elif int(deposit_amount)<=0 or int(deposit_amount)>100000:
    error_message = "<br><p>Failed to deposit amount. Make sure balance is greater than 0 and less than 100000.</p>"

mlog.error(TAG,"Deposit money error message: " + str(error_message))
if error_message != None:
    print('''
        <div id="entry" >        
            <p>Failed to deposit money:</p>
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

deposit_money_failed = False
final_available_balance = 0
try:
    sql_update = "UPDATE account SET balance=balance+" + deposit_amount + " WHERE number=" + str(account_number) + ";"
    conn.query(sql_update)
    sql_select = "SELECT balance FROM account WHERE number=" + str(account_number) + ";"
    conn.query(sql_select)
    all_recs = conn.store_result()
    if all_recs != None and all_recs.num_rows() > 0 :
        row = all_recs.fetch_row()    
        for item in row:
            final_available_balance = item[0]
    try:
        time_format = "%Y:%m:%d-%H:%M:%S"
        timenow = datetime.datetime.now().strftime(time_format)
        sql_insert1 = "INSERT INTO transaction(from_account,to_account,amount,timestamp,message,status)"
        mlog.debug(TAG,"Make sure all account number during registration is >10000, so that we can differentiate from self deposits acc i.e '1111'")
        sql_insert1 += " VALUES(1111, " + str(account_number) + ", " + deposit_amount + ", '"+timenow+"', 'Self deposit', 'Success')"
        conn.query(sql_insert1)
    except Exception as e:
        mlog.error(TAG,"Unable to insert deposit event to transaction table:"+str(e))
except Exception as e:
    deposit_money_failed = True
    mlog.error(TAG,"Unable to add payee to database:"+str(e))

conn.close()

print('''<div id="entry" >''')
print('''<div id="entry" >''') # to give margin
if(deposit_money_failed == True) :
    print("<br><p>Unable to add deposit amount to MyBanking Account Database.!</p>")
else:
    print("<br><p>Successfully deposited amount! Now, available balance is " + str(final_available_balance) + "</p>")
print("</div>")
print("</div>")
print(helperHTML.get_html_end_preset())

