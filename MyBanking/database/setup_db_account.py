#!/usr/bin/python3

import _mysql
import db_config

try:
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:    
    print(e)
#-------------------------------------------------DROP------------------------------------------------------------
print("\n--------------------------------------DROP-account---------------------------------------")
query_drop_table = "DROP TABLE account"
try:
    print("Query: ",query_drop_table)
    conn.query(query_drop_table)
    print("Result: Successfully dropped table.")
except Exception as e:    
    print(e)
#-------------------------------------------------CREATE------------------------------------------------------------
print("\n--------------------------------------CREATE-account---------------------------------------")
query_create_account = '''CREATE TABLE account (
  number INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  ifsc_code VARCHAR(10) NOT NULL,
  bank_name VARCHAR(45) NOT NULL,
  branch_name VARCHAR(45) NOT NULL,
  balance INT NOT NULL,
  PRIMARY KEY (number));'''
try:
    print("Query: ",query_create_account)
    conn.query(query_create_account)
    print("Result: Successfully created.")
except Exception as e:
    print("Error occured!");
    print(e)


#---------------------------------------------------INSERT----------------------------------------------------------
print("\n--------------------------------------INSERT-account---------------------------------------")
try:
    sql_insert1 = "INSERT INTO account(number,name,ifsc_code,bank_name,branch_name,balance)"
    sql_insert1 += " VALUES(20001, 'Chandan', 'SBIB123456', 'SBI', 'Bangalore',1000)"
    conn.query(sql_insert1)
    sql_insert2 = "INSERT INTO account(number,name,ifsc_code,bank_name,branch_name,balance)"
    sql_insert2 += " VALUES(20002, 'Anthony', 'PNB123456', 'PNB', 'Panjab',2000)"
    conn.query(sql_insert2)
    print("Result: Successfully inserted.")
except Exception as e:
    print("Insert error!")
    print(e)

#---------------------------------------------------UPDATE-balance----------------------------------------------------------
print("\n--------------------------------------UPDATE-account---------------------------------------")
try:
    sql_update1 = "UPDATE account SET balance=1500 WHERE number=20001"
    conn.query(sql_update1)
    print("Result: Successfully updated.")
except Exception as e:
    print("Insert error!")
    print(e)
print("\n--------------------------------------DONE---------------------------------------")
conn.close()

