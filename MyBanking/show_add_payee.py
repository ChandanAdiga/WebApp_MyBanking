#!/usr/bin/python3

import cgi, cgitb
import sys
import helperHTML
import helperSession
import mlog

TAG = "SHOW_ADD_PAYEE"
mlog.debug(TAG, "At show_add_payee!")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

if(helperSession.any_session_active() == False):
    #Show session inactive..
    mlog.debug(TAG,"In add_payee with no active session. So prompting to sign in again..")
    print(helperHTML.get_html_invalid_session_preset())
    print(helperHTML.get_html_end_preset())
    sys.exit()

content = '''
    <div id="entry" >
        <a id="dashboard_menu_a" href="show_dashboard.py">Dashboard</a>
        <a id="dashboard_menu_a" href="show_remove_payee.py">Remove Payee</a>
        <a id="dashboard_menu_a" href="show_deposit_money.py">Deposit Money</a>
        <a id="dashboard_menu_a" href="show_money_transfer.py">Money Transfer</a>
        <a id="dashboard_menu_a" href="logout.py">Logout</a>
    </div>
	<div id="entry">
        <h4>Add Payee:</h4>
	</div>
    <div id="entry">
        <form action="/do_add_payee.py" method="post">
          <div id="entry">
            <label>Payee Name</label>
            <input type="text" placeholder="Payee Name" name="payee_name" required>
	      </div>
          <div id="entry">
            <label>Payee Account No.</label>
            <input type="number" placeholder="Payee Acc No." name="payee_account" required>
	      </div>
          <div id="entry">
            <label>Bank Name</label>
            <input type="text" placeholder="Bank Name" name="payee_bank" required>
	      </div>
          <div id="entry">
            <label>Branch Name</label>
            <input type="text" placeholder="Branch Name" name="payee_branch" required>
	      </div>
          <div id="entry">
            <label>IFSC Code</label>
            <input type="text" placeholder="IFSC Code" name="payee_ifsc_code" required>
	      </div>
	      
          <div id="entry" >
            <button type="submit">Add Payee</button>
          </div>
        </form>
    </div>
'''
print(content)
print(helperHTML.get_html_end_preset())
