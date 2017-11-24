

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Configure db_config.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2. Execute respective python scripts for each table:
    user: python3 setup_db_user.py
    acount: python3 setup_db_account.py
    payee_list: python3 setup_db_payeelist.py
    transaction: setup_db_transaction.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FYI: Above scripts will
    -Drop any existing table and create fresh one.
    -Insert some preconfigured values to fill up some data to start with.
        Ex: User1: with login_name = 'chandan' and password = 'password'
            User2: with login_name = 'anthony' and password = 'welcome'
        and some transactions and payee details for above accounts.
