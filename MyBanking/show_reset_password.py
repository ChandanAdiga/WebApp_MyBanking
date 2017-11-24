#!/usr/bin/python3

import cgi, cgitb
import sys
import helperHTML
import helperSession
import mlog

TAG = "SHOW_RESET_PASSWORD."
mlog.debug(TAG, "At show_reset_password.py!")
cgitb.enable()
print(helperHTML.get_html_init())

if(helperSession.any_session_active() == True):
    #session active..Redirect to dashboard..
    mlog.debug(TAG,"In show_reset_password.py with active session. So showing dashboard..")
    print(helperHTML.get_html_content_with_redirect("show_dashboard.py"))    
    sys.exit()

#Dump register page content..
content = '''
    <h4>Forgont password:</h4>
    <form action="/do_reset_password.py" method="post">
       <div id="entry">
            <label>Enter Username</label>
            <input type="text" placeholder="Enter Username" name="login_name" required>
	   </div>
       <div id="entry">
            <label>New Password</b></label>
            <input type="password" placeholder="Enter Password" name="login_key" required>
       </div>
       <div id="entry">
            <label>Confirm New Password</b></label>
            <input type="password" placeholder="Confirm Password" name="login_key_confirm" required>
       </div>
	  
      <div id="entry" >
            <button type="submit">Reset password</button>
      </div>
      <div id="entry" >
            <a href="index.py">Sign In</a>
      </div>
    </form>
'''

print(helperHTML.get_html_start_preset())
print(content)
print(helperHTML.get_html_end_preset())



