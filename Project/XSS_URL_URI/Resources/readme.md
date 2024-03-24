## How we found the flag
- We clicked on the nsa image on the index page, which led us to "http://{ip}/?page=media&src=nsa"
- We attempting to changed the value of src, and getting Wrong Answer, so we knew we are doing the right thing
- And we try to use a data uri to test if we can create a reflected cross site scrpting. So we inject something like this "src=data:text/html;base64,PHNjcmlwdD5jb25zb2xlLmxvZyg0Mik8L3NjcmlwdD4=" which is "<script>console.log(42)</script>" in base64. And we found 42 is printing in the console, but still got wrong answer, we confirm there is a XSS breach
- So, we chnaged to src into "src=data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=" which is "<script>alert(42)</script>", and we found the flag


## Resouces 
- Reflected cross-site scripting (or XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.

## How to exploit the breach
- we can inject any command in the url which would run automatically, and control the website that is only forbidden by user behavior

## What's the correct way
- Implement strict input validation and output encoding to prevent injection attacks, including XSS.
- Sanitize user input and encode output to ensure that user-supplied data is treated as data, not executable code.
- Utilize Content Security Policy (CSP) headers to mitigate the impact of XSS attacks by restricting the sources from which scripts can be loaded.
