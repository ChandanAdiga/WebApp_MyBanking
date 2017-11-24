#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog
from helperRegEx import Validator

TAG = "DO_RESET_PASSWORD"
mlog.debug(TAG, "Trying to reset password..")
cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

print("<h4>Reset password status:</h4><br><br>")

login_name = ""
login_key = ""
login_key_confirm = ""
mlog.debug(TAG,"Fetching form values..")
try:
    form_entries = cgi.FieldStorage()
    login_name = form_entries.getvalue("login_name")
    login_key = form_entries.getvalue("login_key")
    login_key_confirm = form_entries.getvalue("login_key_confirm")
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

error_message = None
if(login_name == None or login_key == None or login_key_confirm == None) :
    error_message = "<br><p>Failed to change password! Invalid attributes provided. Try again with valid attributes</p>"
else:
    reset_validator = Validator()
    if reset_validator.validate_login_name(login_name,6,15) == False:
        error_message = reset_validator.message
    elif reset_validator.validate_login_key(login_key,6,12) == False:
        error_message = reset_validator.message
    elif login_key != login_key_confirm:
        error_message = "<P>New password and confirm passwords did not match!</p>"

mlog.error(TAG,"Reset password validator error message: " + str(error_message))
if error_message != None:
    print('''
        <div id="entry" >        
            <p>Failed to reset password:</p>
            <div id="entry" >
    ''')
    print(error_message)
    print('''</div></div>''')
    print('''
        <div id="entry" >
            <br><a href="show_reset_password.py">Reset password</a>
        </div>
        <div id="entry" >
            <br><a href="index.py">Sign In</a>
        </div>
    ''')
    print(helperHTML.get_html_end_preset())
    sys.exit()

try:
    mlog.debug(TAG, "Establishing database connection..")
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:
    mlog.error(TAG,"Unable to conenct to MyBanking Database:" +  str(e))
    print('''
            <h4>Unable to conenct to MyBanking Database.</h4>
            <div id="entry" >
                <a href="show_dashboard.py">BACK</a>
            </div>
        ''')
    print(helperHTML.get_html_end_preset())
    sys.exit()

all_recs = None
reset_failed = False
try:
    query_login = "SELECT login_name, session FROM user WHERE login_name='"+login_name+"';"
    conn.query(query_login)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

db_login_name = None
if all_recs != None and all_recs.num_rows() > 0 :
    row = all_recs.fetch_row()
    for item in row:
        if(login_name == str(item[0],'utf-8')) :
            db_login_name = login_name
if db_login_name == None:
    error_message = "No user found with login name '" + login_name +"'"
    mlog.error(TAG,"Error: " + error_message)
    reset_failed = True
else:
    try:
        sql_update = "UPDATE user SET login_key='"+login_key+"' WHERE login_name='"+login_name+"';"
        conn.query(sql_update)
    except Exception as e:
        error_message = str(e)
        mlog.error(TAG,"Error: " + error_message)
        reset_failed = True
conn.close()
print('''<div id="entry" >''')
if(reset_failed == True):
    print("<br><p>Failed to  reset password! "+error_message+" Try again.</p><br>")
else:
    print("<br><p>Congratulations. Password has been changed successfull!</p><br>")
print("</div>")
print('''
    <div id="entry" >
        <br><a href="show_reset_password.py">Reset password</a>
    </div>
    <div id="entry" >
        <br><a href="index.py">Sign In</a>
    </div>
''')

print(helperHTML.get_html_end_preset())

