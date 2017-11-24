#!/usr/bin/python3

import cgi, cgitb
import sys
import helperHTML
import helperSession

cgitb.enable()
print(helperHTML.get_html_init())
print(helperHTML.get_html_start_preset())

helperSession.end_session()

print('''
    <div id="entry" >
        <a href="index.py">HOME</a>
        <br>
        <div id="entry" >
            <h4> Successfully logged out! </h4>
        </div>        
    </div>

''')
print(helperHTML.get_html_end_preset())




