#!/usr/bin/python3

import _mysql
import db_config
from time import sleep
import datetime

try:
    conn = _mysql.connect(db_config.db_host,db_config.db_user,db_config.db_password,db_config.db_name)
except Exception as e:    
    print(e)
#-------------------------------------------------DROP------------------------------------------------------------
print("\n--------------------------------------DROP-transaction---------------------------------------")
query_drop_table = "DROP TABLE transaction"
try:
    print("Query: ",query_drop_table)
    conn.query(query_drop_table)
    print("Result: Successfully dropped table.")
except Exception as e:    
    print(e)

#-------------------------------------------------CREATE------------------------------------------------------------
print("\n--------------------------------------CREATE-transaction---------------------------------------")
query_create_transaction = '''CREATE TABLE transaction (
  id INT NOT NULL AUTO_INCREMENT,
  from_account INT NOT NULL,
  to_account INT NOT NULL,
  amount INT NOT NULL,
  timestamp VARCHAR(20) NOT NULL,
  message VARCHAR(45) NOT NULL,
  status VARCHAR(10) NOT NULL,
  PRIMARY KEY (id));'''
try:
    print("Query: ",query_create_transaction)
    conn.query(query_create_transaction)
    print("Result: Successfully executed.")
    
except Exception as e:
    print("Error occured!");
    print(e)
#---------------------------------------------------INSERT----------------------------------------------------------
print("\n--------------------------------------INSERT-transaction---------------------------------------")
try:
    time_format = "%Y:%m:%d-%H:%M:%S"
    timenow = datetime.datetime.now().strftime(time_format)
    sql_insert1 = "INSERT INTO transaction(from_account,to_account,amount,timestamp,message,status)"
    sql_insert1 += " VALUES(20001, 20002, 500, '"+timenow+"', 'Transaction 1,M old. Dont see me.', 'Success')"
    conn.query(sql_insert1)
    print("Inserted successfully @ "+timenow)

    print("Sleeping now..")
    sleep(5)
    timenow = datetime.datetime.now().strftime(time_format)
    sql_insert2 = "INSERT INTO transaction(from_account,to_account,amount,timestamp,message,status)"
    sql_insert2 += " VALUES(20002, 20001, 500, '"+timenow+"', 'Transaction 2', 'Success')"
    conn.query(sql_insert2)
    print("Inserted successfully @ "+timenow)

    print("Sleeping now..")
    sleep(5)
    timenow = datetime.datetime.now().strftime(time_format)
    sql_insert2 = "INSERT INTO transaction(from_account,to_account,amount,timestamp,message,status)"
    sql_insert2 += " VALUES(20002, 20001, 1200, '"+timenow+"', 'T3 Some more message', 'Success')"
    conn.query(sql_insert2)
    print("Inserted successfully @ "+timenow)

    print("Sleeping now..")
    sleep(5)
    timenow = datetime.datetime.now().strftime(time_format)
    sql_insert2 = "INSERT INTO transaction(from_account,to_account,amount,timestamp,message,status)"
    sql_insert2 += " VALUES(20002, 20001, 5000, '"+timenow+"', 'T4 Okay got it', 'Success')"
    conn.query(sql_insert2)
    print("Inserted successfully @ "+timenow)

    print("Sleeping now..")
    sleep(5)
    timenow = datetime.datetime.now().strftime(time_format)
    sql_insert2 = "INSERT INTO transaction(from_account,to_account,amount,timestamp,message,status)"
    sql_insert2 += " VALUES(20001, 20002, 50, '"+timenow+"', 'T5 A small amount though', 'Success')"
    conn.query(sql_insert2)
    print("Inserted successfully @ "+timenow)

    print("Sleeping now..")
    sleep(5)
    timenow = datetime.datetime.now().strftime(time_format)
    sql_insert2 = "INSERT INTO transaction(from_account,to_account,amount,timestamp,message,status)"
    sql_insert2 += " VALUES(20002, 20001, 50, '"+timenow+"', 'Transaction6 ', 'Success')"
    conn.query(sql_insert2)
    print("Inserted successfully @ "+timenow)

except Exception as e:
    print("Insert error!")
    print(e)
print("\n--------------------------------------DONE---------------------------------------")
conn.close()
