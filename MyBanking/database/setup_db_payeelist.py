#!/usr/bin/python3

import _mysql
import db_config

try:
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:
    print(e)
#-------------------------------------------------DROP------------------------------------------------------------
print("\n--------------------------------------DROP-payee_list---------------------------------------")
query_drop_table = "DROP TABLE payee_list"
try:
    print("Query: ",query_drop_table)
    conn.query(query_drop_table)
    print("Result: Successfully dropped table.")
except Exception as e:    
    print(e)

#-------------------------------------------------CREATE------------------------------------------------------------
print("\n--------------------------------------CREATE-payee_list---------------------------------------")
query_create_payee_list = '''CREATE TABLE payee_list (
  id INT NOT NULL AUTO_INCREMENT,
  payee_name VARCHAR(45) NOT NULL,
  owner_account INT NOT NULL,
  payee_account INT NOT NULL,
  payee_bank VARCHAR(45) NOT NULL,
  payee_branch VARCHAR(45) NOT NULL,
  payee_ifsc_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (id));'''
try:
    print("Query: ",query_create_payee_list)
    conn.query(query_create_payee_list)
    print("Result: Successfully executed.")    
except Exception as e:
    print("Error occured!");
    print(e)

#---------------------------------------------------INSERT----------------------------------------------------------
print("\n--------------------------------------INSERT-payee_list---------------------------------------")
try:
    sql_insert1 = "INSERT INTO payee_list(payee_name,owner_account,payee_account,payee_bank,payee_branch,payee_ifsc_code)"
    sql_insert1 += " VALUES('Anthony', 20001, 20002, 'PNB', 'Panjab','PNB123456')"
    conn.query(sql_insert1)
    sql_insert2 = "INSERT INTO payee_list(payee_name,owner_account,payee_account,payee_bank,payee_branch,payee_ifsc_code)"
    sql_insert2 += " VALUES('Chandan', 20002, 20001, 'SBI', 'Bangalore','SBI123456')"
    conn.query(sql_insert2)
    print("Result: Successfully inserted.")
except Exception as e:
    print("Insert error!")
    print(e)
print("\n--------------------------------------DONE---------------------------------------")
conn.close()
