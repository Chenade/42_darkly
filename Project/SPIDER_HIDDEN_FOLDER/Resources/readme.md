## How we found the flag

- Upon visiting the URL "http://{ip}/.hidden/", numerous folders were discovered, each potentially containing subfolders and README files.
- We wrote a python script with Scrapy to systematically traversed through the folders and subfolders, extracting the content of README files encountered.
- The Scrapy spider followed links within each folder, recursively exploring nested directories to locate any README files present.
- If a README file was found within a folder, its content was extracted and analyzed for the presence of the term "flag."
- Upon encountering a README file containing the term "flag," its content was stored in an output file for further examination, marking the successful identification of sensitive information.

- We can start the python script with 
```
scrapy runspider spider.py
```

- After the scripted and we can find the flag in our output.txt file

## How to exploit the breach
An automated script was used to systematically search through directories and retrieve content. However, unauthorized access to sensitive information, such as flags, could potentially occur if proper access controls are not in place.

## What's the correct way
- Implement strict access controls and permission settings to prevent unauthorized access to sensitive directories and files.
- Regularly monitor and audit directory structures to identify any unauthorized or exposed content.
- Employ encryption or other protective measures to safeguard sensitive information stored within README files or similar resources.
- Utilize secure coding practices to ensure that sensitive data is not inadvertently exposed through directory traversal vulnerabilities or insecure file storage mechanisms.