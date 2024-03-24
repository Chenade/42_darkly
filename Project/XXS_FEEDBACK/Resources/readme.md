## How we found the flag
- From the main page, go to the bottom and click on "LEAVE A FEEDBACK" (http://{ip}/?page=feedback)
- Try to insert some script in the Name input field, notice that there is length limit. Open the inspect and remove the `maxlength="10"`.
- Try to insert `<script />` tag, notice that the tag gets escaped.
- Try `<body onload=alert('test1')>` ([doc](https://owasp.org/www-community/attacks/xss/)), an alert is shown, but no flag appears.
- Actually we only need to type "script" in the input and submit it to get the flag.

## How to exploit the breach

- Malicious script can be injected to trusted websites and ran on other end users' browser to modify the page content and to retrive cookies, session tokens, or other sensitive information.

## What's the correct way 
[doc](https://portswigger.net/web-security/cross-site-scripting/preventing)
- Filter input on arrival.
- Encode data on output.
In an HTML context, you should convert non-whitelisted values into HTML entities:
```
< converts to: &lt;
> converts to: &gt;
```
In a JavaScript string context, non-alphanumeric values should be Unicode-escaped:
```
< converts to: \u003c
> converts to: \u003e
```
- Use appropriate response headers.
