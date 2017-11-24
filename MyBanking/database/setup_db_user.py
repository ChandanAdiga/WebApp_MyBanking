#!/usr/bin/python3

import _mysql
import db_config

try:
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:    
    print(e)
#-------------------------------------------------DROP------------------------------------------------------------
print("\n--------------------------------------DROP-user---------------------------------------")
query_drop_table = "DROP TABLE user"
try:
    print("Query: ",query_drop_table)
    conn.query(query_drop_table)
    print("Result: Successfully dropped table.")
except Exception as e:    
    print(e)

#---------------------------------------------------CREATE----------------------------------------------------------
print("\n--------------------------------------CREATE-user---------------------------------------")
query_create_user = '''CREATE TABLE user (
  login_name VARCHAR(20) NOT NULL,
  login_key VARCHAR(20) NOT NULL,
  account_number INT NOT NULL UNIQUE,
  session TINYINT(4) NOT NULL,
  PRIMARY KEY (login_name));'''
try:
    print("Query: ",query_create_user)
    conn.query(query_create_user)
    print("Result: Successfully executed.")
    
except Exception as e:
    print("Error occured!");
    print(e)

#---------------------------------------------------INSERT----------------------------------------------------------
print("\n--------------------------------------INSERT-user---------------------------------------")
try:
    sql_insert1 = "INSERT INTO user(login_name,login_key,account_number,session)"
    sql_insert1 += " VALUES('chandan', 'password', 20001, 0)"
    conn.query(sql_insert1)
    sql_insert2 = "INSERT INTO user(login_name,login_key,account_number,session)"
    sql_insert2 += " VALUES('anthony', 'welcome', 20002, 0)"
    conn.query(sql_insert2)
    print("Result: Successfully inserted.")
except Exception as e:
    print("Insert error!")
    print(e)
print("\n--------------------------------------DONE---------------------------------------")
conn.close()
