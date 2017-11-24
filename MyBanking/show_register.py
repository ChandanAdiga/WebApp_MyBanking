#!/usr/bin/python3

import cgi, cgitb
import sys
import helperHTML
import helperSession
import mlog

TAG = "SHOW_REGISTER.py"
mlog.debug(TAG, "At show_register.py!")
cgitb.enable()
print(helperHTML.get_html_init())

if(helperSession.any_session_active() == True):
    #session active..Redirect to dashboard..
    mlog.debug(TAG,"In show_register.py with active session. So showing dashboard..")
    print(helperHTML.get_html_content_with_redirect("show_dashboard.py"))    
    sys.exit()

#Dump register page content..
content = '''
    <h4>Register/Sign up:</h4>
    <form action="/do_register.py" method="post">
       <div id="entry">
            <label>Full Name</label>
            <input type="text" placeholder="Enter Full Name" name="full_name" required>
	   </div>
       <div id="entry">
            <label>Username</label>
            <input type="text" placeholder="Enter Username" name="login_name" required>
	   </div>
	   <div id="entry">
            <label>Password</b></label>
            <input type="password" placeholder="Enter Password" name="login_key" required>
       </div>
       <div id="entry">
            <label>Confirm Password</b></label>
            <input type="password" placeholder="Confirm Password" name="login_key_confirm" required>
       </div>
       <div id="entry">
            <label>Account Number</b></label>
            <input type="number" placeholder="Enter Account Number" name="account_number" required>
            <br><label>PS: Account number has to be greater than 10000</b></label>
       </div>
       <div id="entry">
            <label>Bank Name</b></label>
            <input type="text" placeholder="Enter Bank Name" name="bank_name" required>
       </div>
       <div id="entry">
            <label>Bank Branch</b></label>
            <input type="text" placeholder="Enter Bank Branch" name="branch_name" required>
       </div>
       <div id="entry">
            <label>IFSC Code</b></label>
            <input type="text" placeholder="Enter IFSC Code" name="ifsc_code" required>
       </div>

       <div id="entry" >
            <button type="submit">Register</button>
       </div>
       <div id="entry" >
            <a href="index.py">Sign In</a>
        </div>
    </form>
'''

print(helperHTML.get_html_start_preset())
print(content)
print(helperHTML.get_html_end_preset())



