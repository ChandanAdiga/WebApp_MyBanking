#!/usr/bin/python3

import cgi, cgitb

cgitb.enable()

payee_input_prefix = "payee_"

def get_html_init():
    return "Content-Type: text/html"

def get_html_start_preset():
        content = '''
            <html>
                <head>
                    <title>MyBanking</title>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="def_style.css">
                </head>
                <body>
                    <div id="content_bg_main">
        '''
        return content

def get_html_content_with_redirect(url):
    content = '''
            <html>
                <head>
                    <title>MyBanking</title>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="def_style.css">
    '''
    content += "<META HTTP-EQUIV=\"refresh\" CONTENT=\"1;URL="+url+"\">"
    content += '''
            </head>
                <body>
                    <div id="entry">
                        <br>
                        <p>Do not refresh. You will be redirected automatically soon..</p>
                    </div>
                </body>
            </html>
    '''
    return content;

def get_html_invalid_session_preset():
    content = '''
        <div id="entry" >
            <p>Invalid session. Login again!<br></p>
        </div>
        <div id="entry" >
            <a href="index.py">Sign In</a>
        </div>
    '''
    return content

def get_html_end_preset():
        return '''
                    </div>
                </body>
            </html>
            '''
