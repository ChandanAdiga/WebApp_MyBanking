#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog

TAG = "DASHBOARD"
mlog.debug(TAG, "At dashboard!")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

if(helperSession.any_session_active() == False):
    #Show session inactive..
    mlog.debug(TAG,"In dashboard with no active session. So prompting to sign in again..")
    print(helperHTML.get_html_invalid_session_preset())
    print(helperHTML.get_html_end_preset())
    sys.exit()
mlog.debug(TAG,"In dashboard with active session..")
try:
    mlog.debug(TAG, "Establishing database connection..")
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:
    mlog.error(TAG,"Unable to conenct to MyBanking Database.")
    helperSession.end_session()
    print('''
            <h4>Unable to conenct to MyBanking Database.</h4>
            <div id="entry" >
                <a href="index.py">HOME</a>
            </div>
        ''')
    print(helperHTML.get_html_end_preset())
#    print(e)
    sys.exit()

all_recs = None
account_number = helperSession.get_session_accout_no()
try:    
    query_user = "SELECT login_name, session FROM user WHERE account_number="+str(account_number)+";"
    conn.query(query_user)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

db_login_name = ""
if all_recs != None and all_recs.num_rows() > 0 :
    row = all_recs.fetch_row()
    for item in row:
        db_login_name = item[0]
        db_session = item[1]
#--------------------------------------------MENU DETAILS----------------------------------------------------
#Greet user and show MENU..
print('''
        <div id="entry" >
            <a id="dashboard_menu_a" href="show_add_payee.py">Add Payee</a>
            <a id="dashboard_menu_a" href="show_remove_payee.py">Remove Payee</a>
            <a id="dashboard_menu_a" href="show_deposit_money.py">Deposit Money</a>
            <a id="dashboard_menu_a" href="show_money_transfer.py">Money Transfer</a>
            <a id="dashboard_menu_a" href="logout.py">Logout</a>
        </div>
    ''')
print("<div id=\"entry\" >")
mlog.debug(TAG,"Welcoming user: " + str(db_login_name))
print("<h2> Welcome " + str(db_login_name,'utf-8') + "!</h2><br><br>")
print("</div>")
#--------------------------------------------ACCOUNT DETAILS----------------------------------------------------
#1.Get account details as dictonary and display as table.
try:
    query_account = "SELECT name, number, ifsc_code, bank_name, branch_name, balance FROM account WHERE number="+str(account_number)+";"
    conn.query(query_account)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

account_details = '''
        <div id="entry_dashboard_acc_details" >
            <p>Account details:</p>
            <table border=1>
            <tr>
                <th>ACC HOLDER NAME</th>
                <th>ACCOUNT NO</th>
                <th>BANK IFSC CODE</th>
                <th>BANK NAME</th>
                <th>BRANCH NAME</th>
                <th>BALANCE</th>
            </tr>
    '''

if all_recs != None and all_recs.num_rows() > 0 :
    row = all_recs.fetch_row()    
    for item in row:
        account_details += "<tr>"
        account_details += "<td>" + str(item[0],'utf-8') + "</td>"
        account_details += "<td>" + str(item[1]) + "</td>"
        account_details += "<td>" + str(item[2],'utf-8') + "</td>"
        account_details += "<td>" + str(item[3],'utf-8') + "</td>"
        account_details += "<td>" + str(item[4],'utf-8') + "</td>"
        account_details += "<td>" + str(item[5]) + "</td>"
        account_details += "</tr>"
else:
    account_details += "<tr>"
    for index in range(0,5):
        account_details += "<td>Null</td>"
    account_details += "</tr>"
account_details += "</table></div>"
print(account_details)

#--------------------------------------------TRANSACTION DETAILS----------------------------------------------------
#2.Get last 5 transactions and display as table.
try:
    #INSERT INTO transaction(id,from_account,to_account,amount,timestamp,message,status)
    query_transaction = "SELECT from_account, to_account, amount, timestamp, message, status FROM transaction WHERE from_account="+str(account_number)+" OR to_account="+str(account_number)+" ORDER BY timestamp DESC;"
    conn.query(query_transaction)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

transaction_details = '''
        <div id="entry_dashboard_transaction" >
            <br><p>Last 5 transaction details:</p>
            <table border=1>
            <tr>
                <th>FROM ACCOUNT</th>
                <th>TO ACCOUNT</th>
                <th>TRANSFER TYPE</th>
                <th>AMOUNT</th>
                <th>TIMESTAMP</th>                
                <th>MESSAGE</th>
            </tr>
    '''

if all_recs != None and all_recs.num_rows() > 0 :
    rows = all_recs.fetch_row(maxrows=5)
    done = False
    row_count =  all_recs.num_rows()
    if row_count > 5 :
        row_count = 5
    mlog.error(TAG,"transactions >> row_count: " + str(row_count))
    while (rows):
        for item in rows:
            if(row_count<=0):
                done = True
                break;
            row_count-=1
            transaction_details += "<tr>"
            if int(item[0]) == 1111:
                transaction_details += "<td>CASH</td>"
            else:
                transaction_details += "<td>" + item[0] + "</td>"
            transaction_details += "<td>" + item[1] + "</td>"
            if(int(account_number) == int(item[0])):
                #i.e my acc = from account => DEBIT
                transaction_details += "<td>DEBIT</td>"
            else:
                #i.e my acc = to account => CREDIT
                transaction_details += "<td>CREDIT</td>"
            transaction_details += "<td>" + item[2] + "</td>"
            transaction_details += "<td>" + str(item[3],'utf-8') + "</td>"
            transaction_details += "<td>" + str(item[4],'utf-8') + "</td>"
            transaction_details += "</tr>"
        if(done == True) :
            break;
else:
    transaction_details += "<tr>"
    for index in range(0,6):
        transaction_details += "<td>Null</td>"
    transaction_details += "</tr>"
transaction_details += "</table></div>"
print(transaction_details)

#--------------------------------------------PAYEE DETAILS----------------------------------------------------
#3.Get list of payees and display as table.
try:
    #payee_list(payee_name,owner_account,payee_account,payee_bank,payee_branch,payee_ifsc_code)
    query_payee_list = "SELECT payee_name, payee_account, payee_bank, payee_branch, payee_ifsc_code FROM payee_list WHERE owner_account="+str(account_number)+";"
    conn.query(query_payee_list)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

payee_details = '''
        <div id="entry_dashboard_payees" >
            <br><p>Available payees:</p>
            <table border=1>
            <tr>
                <th>PAYEE NAME</th>
                <th>PAYEE ACCOUNT</th>
                <th>PAYEE BANK</th>
                <th>BANK BRANCH</th>
                <th>IFSC CODE</th>
            </tr>
    '''

if all_recs != None and all_recs.num_rows() > 0 :
    rows = all_recs.fetch_row(maxrows=5)
    while (rows):
        for item in rows:
            payee_details += "<tr>"
            payee_details += "<td>" + str(item[0],'utf-8') + "</td>"
            payee_details += "<td>" + item[1] + "</td>"
            payee_details += "<td>" + str(item[2],'utf-8') + "</td>"
            payee_details += "<td>" + str(item[3],'utf-8') + "</td>"
            payee_details += "<td>" + str(item[4],'utf-8') + "</td>"
            payee_details += "</tr>"
        rows = all_recs.fetch_row(maxrows=5)
else:
    payee_details += "<tr>"
    for index in range(0,5):
        payee_details += "<td>Null</td>"
    payee_details += "</tr>"
payee_details += "</table></div>"
print(payee_details)

#CLOSE DB CONNECTION
conn.close()

print(helperHTML.get_html_end_preset())
