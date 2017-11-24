#!/usr/bin/python3

import re
import mlog

class Validator():
    TAG = "Validator"
    result = False
    message = ""
    #Constructor. Usage: obj = Validator()
    def __init__(self):
        self.result = False
        self.message = ""

    def validate_generic_name(self, generic_name,min_len=5, max_len=8):
        self.result = False
        self.message = ""
        self.min_len = min_len
        self.max_len = max_len
        mlog.debug(self.TAG,"Validating : " + str(generic_name) +"(" + str(self.min_len) + "-" + str(self.max_len) + ")")
        regex_generic_name = re.compile("[a-zA-Z]+[ {1}][a-zA-Z]*")
        if generic_name == None:
            self.message = "<P>User name can not be empty!</p>"
        elif len(str(generic_name)) < self.min_len or len(str(generic_name)) > self.max_len:
            self.message = "<p>User name must be at least " + str(self.min_len) + " characters and  max " + str(self.max_len) + "</p>"
        elif regex_generic_name.match(generic_name) is None:
            self.message = "<p>User name should be only alphabetic.</p>"
        else:
            match = regex_generic_name.match(generic_name)
            if generic_name == match.group(0):
                self.result = True
                self.message = "<p>Valid User name!</p>"
            else:
                self.message = "<p>User name should be only alphabetic(Only first and last names are accepted).</p>"
        return self.result


    def validate_login_name(self, login_name,min_len=5, max_len=8):
        self.result = False
        self.message = ""
        self.min_len = min_len
        self.max_len = max_len
        mlog.debug(self.TAG,"Validating : " + str(login_name) +"(" + str(self.min_len) + "-" + str(self.max_len) + ")")
        regex_login_name = re.compile("[a-zA-Z][a-zA-Z0-9]*")
        if login_name == None:
            self.message = "<P>Login name can not be empty!</p>"
        elif len(str(login_name)) < self.min_len or len(str(login_name)) > self.max_len:
            self.message = "<p>Login name must be at least " + str(self.min_len) + " characters and  max " + str(self.max_len) + "</p>"
        elif regex_login_name.match(login_name) is None:
            self.message = "<p>Login name should be only alphanumeric, must start with alphabet and may or may not contain digits.</p>"
        else:
            match = regex_login_name.match(login_name)
            if login_name == match.group(0):
                self.result = True
                self.message = "<p>Valid login name!</p>"
            else:
                self.message = "<p>Login name should be only alphanumeric, must start with alphabet and may contain digits.</p>"
        return self.result

    def validate_login_key(self, login_key,min_len=5, max_len=8):
        self.result = False
        self.message = ""
        self.min_len = min_len
        self.max_len = max_len
        mlog.debug(self.TAG,"Validating : " + str(login_key) +"(" + str(self.min_len) + "-" + str(self.max_len) + ")")
        regex_login_key = re.compile("[a-zA-Z0-9]+")
        if login_key == None:
            self.message = "<P>Password can not be empty!</p>"
        elif len(str(login_key)) < self.min_len or len(str(login_key)) > self.max_len:
            self.message = "<p>Password must be at least " + str(self.min_len) + " characters and  max " + str(self.max_len) + "</p>"
        elif regex_login_key.match(login_key) is None:
            self.message = "<p>Password can be only alphanumeric, may or may not contain digits.</p>"
        else:
            match = regex_login_key.match(login_key)
            #print(match.group(0))
            if login_key == match.group(0):
                self.result = True
                self.message = "<p>Valid password!</p>"
            else:
                self.message = "<p>Password should be only alphanumeric, must start with alphabet and may contain digits.</p>"

        return self.result

    def validate_bank_name(self, bank_name,min_len=3, max_len=15):
        self.result = False
        self.message = ""
        self.min_len = min_len
        self.max_len = max_len
        mlog.debug(self.TAG,"Validating : " + str(bank_name) +"(" + str(self.min_len) + "-" + str(self.max_len) + ")")
        regex_bank_name = re.compile("[a-zA-Z]+[ ]{0,1}[a-zA-Z]+")
        if bank_name == None:
            self.message = "<P>Bank name can not be empty!</p>"
        elif len(str(bank_name)) < self.min_len or len(str(bank_name)) > self.max_len:
            self.message = "<p>Bank name must be at least " + str(self.min_len) + " characters and  max " + str(self.max_len) + "</p>"
        elif regex_bank_name.match(bank_name) is None:
            self.message = "<p>Bank name must be alphabetic. May contain one space in between.</p>"
        else:
            match = regex_bank_name.match(bank_name)
            #print(match.group(0))
            if bank_name == match.group(0):
                self.result = True
                self.message = "<p>Valid bank name!</p>"
            else:
                self.message = "<p>Bank name must be alphabetic. May contain one space in between.</p>"

        return self.result

    def validate_branch_name(self, branch_name,min_len=5, max_len=15):
        self.result = False
        self.message = ""
        self.min_len = min_len
        self.max_len = max_len
        mlog.debug(self.TAG,"Validating : " + str(branch_name) +"(" + str(self.min_len) + "-" + str(self.max_len) + ")")
        regex_branch_name = re.compile("[a-zA-Z]+[ ]{0,1}[a-zA-Z]+")
        if branch_name == None:
            self.message = "<P>Branch name can not be empty!</p>"
        elif len(str(branch_name)) < self.min_len or len(str(branch_name)) > self.max_len:
            self.message = "<p>Branch name must be at least " + str(self.min_len) + " characters and  max " + str(self.max_len) + "</p>"
        elif regex_branch_name.match(branch_name) is None:
            self.message = "<p>Branch name must be alphabetic. May contain one space in between.</p>"
        else:
            match = regex_branch_name.match(branch_name)
            #print(match.group(0))
            if branch_name == match.group(0):
                self.result = True
                self.message = "<p>Valid Branch name!</p>"
            else:
                self.message = "<p>Branch name must be alphabetic. May contain one space in between.</p>"

        return self.result

    def validate_ifsc_code(self, ifsc_code):
        self.result = False
        self.message = ""
        mlog.debug(self.TAG,"Validating : " + str(ifsc_code) +". Length must be 10 characters.")
        regex_ifsc_code = re.compile("[a-zA-Z]{4}[0-9]{6}")
        if ifsc_code == None:
            self.message = "<P>IFSC code can not be empty!</p>"
        elif len(str(ifsc_code)) != 10:
            self.message = "<p>IFSC code must be 10 characters</p>"
        elif regex_ifsc_code.match(ifsc_code) is None:
            self.message = "<p>IFSC code must be alphanumeric and in pattern: XXXXDDDDDD where X- alphabet and D-Digit.</p>"
        else:
            match = regex_ifsc_code.match(ifsc_code)
            #print(match.group(0))
            if ifsc_code == match.group(0):
                self.result = True
                self.message = "<p>Valid IFSC code!</p>"
            else:
                self.message = "<p>IFSC code must be alphanumeric and in pattern: XXXXDDDDDD where X- alphabet and D-Digit.</p>"

        return self.result


