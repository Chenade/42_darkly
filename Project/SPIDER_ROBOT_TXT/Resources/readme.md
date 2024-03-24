## How we found the flag
- First, We used "Dirb" which is a Web Content Scanner, it looks for existing (and/or hidden) Web Objects. We used the following command
```
dirb http://{ip} -o dirb.log
```

-  The output is in dirb.log in this directory. We found something named "http://{ip}/robots.txt", with the content
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

- We go to "http://{ip}/whatever, and find a file "htpasswd", which has the content 
```
root:437394baff5aa33daa618be47b75cb49
```

- After decrpyed with md5, the true value is 
```
root:qwerty123@
```

- And we used the new pair of crendital to login on admin section, and we got the flag

## Resources
- DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary based attack against a web server and analyzing the responses.
- robots.txt is the filename used for implementing the Robots Exclusion Protocol, a standard used by websites to indicate to visiting web crawlers and other web robots which portions of the website they are allowed to visit. 


## How to exploit the breach
- By using the the web scanner, we can easily find all the web object, even it's hidden

## What's the correct way
- Be careful with robots.txt content, avoid including any sensitive information in this file, as it is intended for directing web crawlers and other automated agents.