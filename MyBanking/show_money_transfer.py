#!/usr/bin/python3

import cgi, cgitb
import sys
import helperHTML
import helperSession
import mlog

TAG = "SHOW_MONEY_TRANSER"
mlog.debug(TAG, "At show_money_transfer!")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

if(helperSession.any_session_active() == False):
    #Show session inactive..
    mlog.debug(TAG,"In show_money_transfer with no active session. So prompting to sign in again..")
    print(helperHTML.get_html_invalid_session_preset())
    print(helperHTML.get_html_end_preset())
    sys.exit()

#Dump menu and sow form to transfer money..
content = '''
        <div id="entry" >
            <a id="dashboard_menu_a" href="show_dashboard.py">Dashboard</a>
            <a id="dashboard_menu_a" href="show_add_payee.py">Add Payee</a>
            <a id="dashboard_menu_a" href="show_remove_payee.py">Remove Payee</a>
            <a id="dashboard_menu_a" href="show_deposit_money.py">Deposit Money</a>
            <a id="dashboard_menu_a" href="logout.py">Logout</a>
        </div>
  		<div id="entry">
            <h4>Transfer money:</h4>
		</div>
  		<div id="entry">
            <form action="/do_money_transfer.py" method="post">
              <div id="entry">
                <label>Beneficiery Name</label>
                <input type="text" placeholder="Beneficiery Name" name="beneficiery_name" required>
			  </div>
              <div id="entry">
                <label>Beneficiery Account No.</label>
                <input type="number" placeholder="Beneficiery Acc No." name="beneficiery_account" required>
			  </div>
              <div id="entry">
                <label>Beneficiery Bank Name</label>
                <input type="text" placeholder="Bank Name" name="beneficiery_bank" required>
			  </div>
              <div id="entry">
                <label>Branch Name</label>
                <input type="text" placeholder="Branch Name" name="beneficiery_branch" required>
			  </div>
              <div id="entry">
                <label>IFSC Code</label>
                <input type="text" placeholder="IFSC Code" name="beneficiery_ifsc_code" required>
			  </div>
			  <div id="entry">
                <label>Amount to transfer</label>
                <input type="number" placeholder="Amount to transfer" name="transfer_amount" required>
			  </div>
              <div id="entry" >
                <button type="submit">Transfer amount</button>
              </div>
            </form>
        </div>
'''
print(content)
print(helperHTML.get_html_end_preset())

