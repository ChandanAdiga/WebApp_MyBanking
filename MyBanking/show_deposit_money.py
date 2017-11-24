#!/usr/bin/python3

import cgi, cgitb
import sys
import helperHTML
import helperSession
import mlog

TAG = "SHOW_DEPOSIT_MONEY"
mlog.debug(TAG, "At show_deposit_money!")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

if(helperSession.any_session_active() == False):
    #Show session inactive..
    mlog.debug(TAG,"In show_deposit_money with no active session. So prompting to sign in again..")
    print(helperHTML.get_html_invalid_session_preset())
    print(helperHTML.get_html_end_preset())
    sys.exit()

#Dump menu and sow form to add money..
content = '''
        <div id="entry" >
            <a id="dashboard_menu_a" href="show_dashboard.py">Dashboard</a>
            <a id="dashboard_menu_a" href="show_add_payee.py">Add Payee</a>
            <a id="dashboard_menu_a" href="show_remove_payee.py">Remove Payee</a>
            <a id="dashboard_menu_a" href="show_money_transfer.py">Money Transfer</a>
            <a id="dashboard_menu_a" href="logout.py">Logout</a>
        </div>
  		<div id="entry">
            <h4>Deposit money:</h4>
		</div>
  		<div id="entry">
            <form action="/do_deposit_money.py" method="post">
              <div id="entry">
                <label>Deposit Amount</label>
                <input type="number" placeholder="Enter amount" name="deposit_amount" required>
		      </div>
              <div id="entry" >
                  <br><br><button type="submit">Deposit Amount</button>
              </div>
            </form>
        </div>
'''
print(content)
print(helperHTML.get_html_end_preset())



