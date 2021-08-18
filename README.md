# Bitstocks coding test

This is a Django coding/knowledge test.  You can run this either in docker, or not.  This test is not about Docker, so if you are not familar, please just setup your environment however you normally would.

Please spend no more than 30 minutes on this test.  Task 4 is optional, only do it if you have time left over.  In all tasks, consider that this is in the context of a financial system, and data integrity and precision is of key importance.

### Docker

The Dockerfile includes running of migrations, and then performing the test suite.  So simply be in the root directory of the project, and run:

```shell
docker build .
```

## Tasks

The project is simple, containing only 1 app with 2 models.  It is a basic implementaion of a system where users can have accounts.  Those accounts can have balances, and we wish to be able to track changes to balances by storing transactions.

There is already a basic deposit service written, allowing for an amount to be added to an Account, and a deposit Transaction created.

### Task 1

The Transaction model is fairly basic, and some important information is missing.  Make sure that whenever a Transaction is created, we store the time it was created.
* I have added create_at which store txn date time
* amount column I have added to txn record for each txn either deposit or withdrawal

### Task 2

The accounts app has a tests.py, which has 2 tests, one of which fails.

Why does the test fail?

* This issue with In most programming languages.
* https://en.wikipedia.org/wiki/Double-precision_floating-point_format

How can you change the application to fix the test?

* Updated balance to type FloatField because when there's enough rounding involved it may not matter, but for money we really can't have rounding errors.
* Saving txn amount into satoshis and while fetching converting into btc

### Task 3

The deposit service is quite basic right now, and not much could go wrong.  But what risks are there with the way it's written? Imagine that it's possible for the creation of the Transaction to fail, what would happen in this case? What could you do to improve it?

* Added check for account and txn then if txn getting pass then only updating amount

### Task 4

The perform_withdrawal service is unwritten.  Implement a basic version of this service - no extra models should be required.  What considerations might you need to make for this service, and how might you approach preventing any issues it might raise?

* Added the perform_withdrawal and their test case also

## Added docker compose file and corrected docker file:
### Output of docker logs after running docker-compose up"
```
$ docker logs -f 629b5a5c3b0f
System check identified some issues:

WARNINGS:
accounts.Account: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
accounts.Transaction: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
Migrations for 'accounts':
  project/accounts/migrations/0001_initial.py
    - Create model Account
    - Create model Transaction
System check identified some issues:

WARNINGS:
accounts.Account: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
accounts.Transaction: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
Operations to perform:
  Apply all migrations: accounts, admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying accounts.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
System check identified some issues:

WARNINGS:
accounts.Account: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
accounts.Transaction: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.

System check identified 2 issues (0 silenced).

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
Watching for file changes with StatReloader
Performing system checks...

System check identified some issues:

WARNINGS:
accounts.Account: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
accounts.Transaction: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the AccountsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.

System check identified 2 issues (0 silenced).
August 18, 2021 - 14:38:03
Django version 3.2.6, using settings 'bitcoin.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```