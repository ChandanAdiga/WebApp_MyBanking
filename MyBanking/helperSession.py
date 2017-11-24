#!/usr/bin/python3

import mlog

SESSION_FILE = 'session.txt'

def get_session_accout_no():
    session_fosr = open(SESSION_FILE,'r')
    value = session_fosr.read()
    session_fosr.close()
    account_number = 0
    try:
        account_number = int(value)
    except Exception as e:
        mlog.error("SESSION", "Something went wrong with session.txt content:"+str(value)+" >>" + str(e))
    return account_number

def any_session_active():
    account_number = get_session_accout_no()
    if int(account_number) > 0:
        return True
    else:
        return False

def start_session(account_number):
    session_fosw = open(SESSION_FILE,'w')
    session_fosw.write(str(account_number))
    session_fosw.close()

def end_session():
    session_fosw = open(SESSION_FILE,'w')
    session_fosw.write(str(0))
    session_fosw.close()
    
if (__name__ == '__main__'):
    print("any_session_active: " + str(any_session_active()))
