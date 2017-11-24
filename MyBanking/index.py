#!/usr/bin/python3

import cgi, cgitb
import sys
import helperHTML
import helperSession
import mlog

TAG = "INDEX.py"
mlog.debug(TAG, "At index.py!")
cgitb.enable()
print(helperHTML.get_html_init())

if(helperSession.any_session_active() == True):
    #session active..Redirect to dashboard..
    mlog.debug(TAG,"In index.py with active session. So showing dashboard..")
    print(helperHTML.get_html_content_with_redirect("show_dashboard.py"))    
    sys.exit()

#Dump login page content..
content = '''
    <h4>Login:</h4>
    <form action="/do_login.py" method="post">
      <div id="entry">
        <label>Username</label>
        <input type="text" placeholder="Enter Username" name="login_name" required>
	  </div>
	  <div id="entry">
        <label>Password</label>
        <input type="password" placeholder="Enter Password" name="login_key" required>                
      </div>
      <div id="entry" >
        <button type="submit">Login</button>
      </div>
      <div id="entry" >
        <a href="show_register.py">Register/Sign Up</a>
      </div>
      <div id="entry" >
        <a href="show_reset_password.py">Forgot password</a>
      </div>
    </form>
'''

print(helperHTML.get_html_start_preset())
print(content)
print(helperHTML.get_html_end_preset())



