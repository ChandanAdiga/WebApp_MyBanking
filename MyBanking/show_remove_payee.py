#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog

TAG = "SHOW_REMOVE_PAYEE"
mlog.debug(TAG, "At show_remove_payee!")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

if(helperSession.any_session_active() == False):
    #Show session inactive..
    mlog.debug(TAG,"In show_remomve_payee with no active session. So prompting to sign in again..")
    print(helperHTML.get_html_invalid_session_preset())
    print(helperHTML.get_html_end_preset())
    sys.exit()

#ELSE: Show list of payees to remove
account_number = helperSession.get_session_accout_no()

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

#--------------------------------------------MENU DETAILS----------------------------------------------------
#Show MENU..
print('''
        <div id="entry" >
            <a id="dashboard_menu_a" href="show_dashboard.py">DASHBOARD</a>
            <a id="dashboard_menu_a" href="show_add_payee.py">Add Payee</a>
            <a id="dashboard_menu_a" href="show_deposit_money.py">Deposit Money</a>
            <a id="dashboard_menu_a" href="show_money_transfer.py">Money Transfer</a>
            <a id="dashboard_menu_a" href="logout.py">Logout</a>
        </div>
    ''')

#---------------------------------------------PULL PAYEE DETAILS-----------------------------------------------
all_recs = None
try:
    #payee_list(payee_name,owner_account,payee_account,payee_bank,payee_branch,payee_ifsc_code)
    query_payee_list = "SELECT id, payee_name, payee_account, payee_bank, payee_branch, payee_ifsc_code FROM payee_list WHERE owner_account="+str(account_number)+";"
    conn.query(query_payee_list)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))
payee_details = ""
if all_recs != None and all_recs.num_rows() > 0 :
    payee_details += '''
        <div id="entry_dashboard_payees">
            <h4>Remove Payees:</h4>
            <div id="entry">
                <form action="do_remove_payee.py" method="post">
                <br><p>Select payees to remove:</p>
                <table border=1>
                <tr>
                    <th></th>
                    <th>PAYEE NAME</th>
                    <th>PAYEE ACCOUNT</th>
                    <th>PAYEE BANK</th>
                    <th>BANK BRANCH</th>
                    <th>IFSC CODE</th>
                </tr>
    '''
    rows = all_recs.fetch_row(maxrows=5)
    while (rows):
        for item in rows:
            payee_details += "<tr>"
            place_holder = helperHTML.payee_input_prefix + str(item[0])
            payee_details += "<td><input type=\"checkbox\" name=\"" + place_holder +"\" value=\"" + place_holder + "\" ></input></td>"
            payee_details += "<td>" + str(item[1],'utf-8') + "</td>"
            payee_details += "<td>" + item[2] + "</td>"
            payee_details += "<td>" + str(item[3],'utf-8') + "</td>"
            payee_details += "<td>" + str(item[4],'utf-8') + "</td>"
            payee_details += "<td>" + str(item[5],'utf-8') + "</td>"
            payee_details += "</tr>"
        rows = all_recs.fetch_row(maxrows=5)
    payee_details += "</table>"
    payee_details += '''
                    <br><button type="submit">Remove Selected Payees</button>
                </form>
             </div>
         </div>
    '''
else:
    payee_details += '''
        <div id="entry_dashboard_payees">
            <h4>Remove Payees:</h4>
            <br><br><br><p> No payees found. Please add some payees.</p>
        </div>
    '''
print(payee_details)
conn.close()

print(helperHTML.get_html_end_preset())


