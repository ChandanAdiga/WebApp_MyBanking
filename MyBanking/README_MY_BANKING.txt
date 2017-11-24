
-------------------------------------------ABOUT-------------------------------------------

                Web Application : MyBanking
                OS Environment  : Ubuntu 16.04LTS(64bit)
                Server          : Apache2(/etc/apache2/)
                Database        : MySql(Refer: /database/README_DATABASE.txt)
                Python Version  : Python3.5(Accessible @ /usr/bin/python3)

-------------------------------------------AUTHOR------------------------------------------

                Author  : Chandan Adiga

-------------------------------------------NOTES-------------------------------------------

        * This project is a web app developped using Linux, Apache2, MySql and 
    Python(LAMP stack where p -> Perl/Php/Python..)

        * It is expected that environment is as defined in 'ABOUT' section.

        * '/etc/apache2/sites-enabled/000-default.conf' file of apache2 needs to be 
    configured as in sample @ /000-default.conf. Note that project root folder is 'MyBanking'
    and path of the same to be configued in 000-default.conf. Ideally 'MyBanking' has to be
    placed in '/var/www/' folder with all permissions(777) granted.
        
        * Make sure mysql server is up and a database is created in it. Configure MySql
    login details and database information at MyBanking/database/db_config.py which will
    be used across the application. Then, execute below python scripts to create and
    initialize necessary tables:
        $python3 ~MyBanking/database/setup_db_account.py
        $python3 ~MyBanking/database/setup_db_user.py
        $python3 ~MyBanking/database/setup_db_payeelist.py
        $python3 ~MyBanking/database/setup_db_transaction.py
        Above script if not altered, will set up below user accounts
            1. [Login Name:chandan; Password:password; Account No:20001]
            2. [Login Name:anthony; Password:welcome; Account No:20002]

        * This web application uses session.txt file to track user login session. I know
    it is not the right way. However, considering purpose of the project work, this should
    be acceptable. Idea is to write/read logged in user account no to session.txt. Note 
    that at any given point of time, only one user account no is written to this file. And
    the file is stored on server side(i.e not on client side!) So at any given instant, 
    only one user can login to the system. Sad, but true :)

        * All python logs are stored under /my_account_app.log file. And all apache2 server
    logs are stored under /var/log/apache2/.

        * Note that to register new user, there is no hint for account no to register 
    against. However if account no already exists, it will give error.
        
-------------------------------------------POC------------------------------------------
    +CGI programming        : index.py, dashboard.py
    +Classes and Objects    : model_account.py, model_account_manager.py, helperRegEx.py(In rest of the places, I could not make use of these/new classes to make it complete OOP due to my time constraints) These are used in do_register.py & show_dashboard.py.
    +Regular expressions    : helperRegEx.py, do_login.py, do_register.py
    +Database programming   : model_account_manager.py and in all do_*.py files.
    +Logging                : mlog.py > Can configure loggin level level=logging.DEBUG(Most of logs used are ERROR, DEBUG and INFO.)
    +CSS                    : def_style.css
    +naming coventions      : Followed as per project description.    

-------------------------------------------COMMANDS-------------------------------------------

    [/etc/apache2] 2s $ sudo systemctl start apache2
    [/etc/apache2] 2s $ sudo systemctl stop apache2

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $mysql -u root -p
    password:
    ....
    mysql>create database my_banking;
    mysql>use my_banking;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    [/var/log/apache2] $ sudo rm -rf ./*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    [/var/www] $ sudo rm -rf MyBanking
    [/var/www] $ sudo cp -R /home/<user>/Desktop/MyBanking .
    [/var/www] $ sudo chmod -R 777 MyBanking

-----------------------------------------------------------------------------------------------


