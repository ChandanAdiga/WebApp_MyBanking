#!/usr/bin/python3

import cgi, cgitb
import _mysql
import sys
import helperHTML
import helperSession
import database.db_config as db_config
import mlog
from helperRegEx import Validator

TAG = "DOLOGIN"
mlog.debug(TAG, "Trying to login..")
cgitb.enable()
print(helperHTML.get_html_init())
login_name = ""
login_key = ""
mlog.debug(TAG,"Fetching form values..")
try:
    form_entries = cgi.FieldStorage()
    login_name = form_entries.getvalue("login_name")
    login_key = form_entries.getvalue("login_key")
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

#if invalid attributes, show error and eixt.
error_message = None
login_validator = Validator()
if login_validator.validate_login_name(login_name,6,10) == False:
    error_message = login_validator.message
elif login_validator.validate_login_key(login_key,6,10) == False:
    error_message = login_validator.message

mlog.error(TAG,"login validator error message: " + str(error_message))
if error_message != None:
    print(helperHTML.get_html_start_preset())
    print('''
        <h4>Failed to login:</h4>
        <div id="entry" >
    ''')
    print(error_message)
    print('''
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
    mlog.error(TAG,"Unable to conenct to MyBanking Database.")
    print(helperHTML.get_html_init())
    print(helperHTML.get_html_start_preset())
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
try:
    query_login = "SELECT login_key, account_number, session FROM user WHERE login_name='"+login_name+"';"
    conn.query(query_login)
    all_recs = conn.store_result()
except Exception as e:
    mlog.error(TAG,"Error: " + str(e))

account_number = 0
if all_recs != None and all_recs.num_rows() > 0 :
    row = all_recs.fetch_row()
    for item in row:
        db_login_key = item[0]
        db_account_number = item[1]
        db_session = item[2]
        #print("<br> db_login_key:{0}".format(str(db_login_key,'utf-8')))
        if(str(login_key) == str(db_login_key,'utf-8')) :
            account_number = db_account_number
            #print("<br> account number found to be:{0}".format(account_number))

#CLOSE DB CONNECTION
conn.close()

#Validate session iff login_attempt
#First clear any previous sessions:
helperSession.end_session()
if login_name != None and int(account_number) > 0:
    #Overrite any current session
    helperSession.start_session(account_number)

mlog.debug(TAG,"any_session_active:"+str(helperSession.any_session_active()))
if(helperSession.any_session_active()):
    #Redirect to dashboard..
    print(helperHTML.get_html_content_with_redirect("show_dashboard.py"))
else :
    print(helperHTML.get_html_init())
    print(helperHTML.get_html_start_preset())
    print("<div id=\"entry\" >")
    print("Unable to sign in. Try again!<br>")
    print("</div>")
    print('''
        <div id="entry" >
            <a href="index.py">Sign In</a>
        </div>
    ''')
    print(helperHTML.get_html_end_preset())


