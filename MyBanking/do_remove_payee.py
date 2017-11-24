#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog

TAG = "DO_REMOVE_PAYEE"
mlog.debug(TAG, "Trying to remove payee..")
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
            <a id="dashboard_menu_a" href="show_remove_payee.py">Remove Payee</a>
            <a id="dashboard_menu_a" href="show_deposit_money.py">Deposit Money</a>
            <a id="dashboard_menu_a" href="show_money_transfer.py">Money Transfer</a>
            <a id="dashboard_menu_a" href="logout.py">Logout</a>
        </div>
    ''')
#---------------------------------------------PULL PAYEE DETAILS-----------------------------------------------

all_recs = None
try:
    #payee_list(payee_name,owner_account,payee_account,payee_bank,payee_branch,payee_ifsc_code)
    query_payee_list = "SELECT id, payee_name, payee_account FROM payee_list WHERE owner_account="+str(account_number)+";"
    conn.query(query_payee_list)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

selected_payees_list = []
if all_recs != None and all_recs.num_rows() > 0 :
    my_db_payees = []
    rows = all_recs.fetch_row(maxrows=5)
    while (rows):
        for item in rows:
            my_db_payees.append(helperHTML.payee_input_prefix + str(item[0]))
        rows = all_recs.fetch_row(maxrows=5)
    mlog.debug(TAG,"my_db_payees:"+str(my_db_payees))
    mlog.debug(TAG,"Fetching HTML form values..")
    try:
        form_entries = cgi.FieldStorage()
        for item in my_db_payees:
            value = form_entries.getvalue(item)
            if(value):
                selected_payees_list.append(str(value))
    except Exception as e:
#        print(e)
         mlog.error(TAG,"Error occured while retrieving form values:"+str(e))

mlog.debug(TAG,"selected_payees_list to remove:"+str(selected_payees_list))


print("<div id=\"entry\" >")
print("<h4> Remove Payee status:</h4><br><br>")
print("</div>")
print("<div id=\"entry\" >")
print("<div id=\"entry\" >")#to give margin..
status_failed = False
if(len(selected_payees_list))>0:
    #Iterate and delete each payee..
    for payee in selected_payees_list:
        mlog.debug(TAG,"Removing payee " + payee + " from payee table..")
        try:
            payee_row_id = payee.replace(helperHTML.payee_input_prefix,"");
            sql_delete = "DELETE FROM payee_list WHERE id=" + payee_row_id + ";"
            conn.query(sql_delete)
        except Exception as e:
            status_failed = True
            mlog.error(TAG,"Error while removing payee-("+payee+"): " + str(e))
    if(status_failed == True) :
        print("<p>Unable to remove payee(s)!</p>")
    else:
        print("<p>Successfully removed payee(s)!</p>")
else:
    #Nothing to delete!
    print("<p>Either no payee(s) selected to remove OR no matching payee(s) in database to remove!</p>")
print("</div>")
print("</div>")
conn.close()
print(helperHTML.get_html_end_preset())

