## How we found the flag
- When we checked the cookie of the iste, we found out that there is a cookie named i_am_admin, and the value is "68934a3e9455fa72420237eb05902327" which is frecogized as "false" after encrpyed with md5
- So, we encryoted "true" in md5, and replace the value the the cookie
- I got the access of the admin and find the flag

## How to exploit the breach
- Exploit the vulnerability by manipulating the "i_am_admin" cookie value to "true" after encryption with MD5, granting unauthorized access to the admin privileges.
- This breach allows for unauthorized access to sensitive functionalities or resources within the website, potentially compromising security and integrity.

## What's the correct way
- Implement secure session management practices, including the proper validation and encryption of session tokens and cookies.
- Utilize strong cryptographic algorithms and protocols to protect sensitive data such as user session information.
- Employ additional authentication mechanisms, such as multi-factor authentication, to prevent unauthorized access even if session tokens are compromised.