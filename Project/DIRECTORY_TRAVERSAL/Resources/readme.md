# Directory Traversal
## How we found the flag
- When we navigate though the website, we can see the "page" variable in GET method.
- We decided to try with some path, considering the website is normally place at /var/www/html, we go with "./../../../etc/passwd" and we got "Almost"
- So, we just add path until we are at "http://{ip}/?page=./../../../../../../etc/passwd", then we got the flag


## How to exploit the breach
- Manipulating the "page" parameter in the URL to navigate to sensitive system files, such as the "/etc/passwd" file, which contains user account information.
- Utilize traversal sequences like "../" to navigate through directories and access files outside of the web root, potentially exposing sensitive data or system configuration files.

## What's the correct way
- Implement strict input validation and sanitization to prevent directory traversal attacks by filtering out or encoding traversal sequences in user-supplied input. Apply a whitelist filter on the "page" variable to allow only permitted characters like '.', '/', and '%'.
- For Remote File Inclusion (RFI) vulnerabilities on PHP websites, disable "allow_url_open" and "allow_url_include" in the PHP configuration to prevent attackers from including remote files via URLs, enhancing the security posture of the application.