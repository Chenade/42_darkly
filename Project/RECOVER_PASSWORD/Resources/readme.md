## How we found the flag
- From the main page, click on "SIGN IN", then click on "I forgot my password" (http://{ip}/?page=recover)
- Notice that there is only a "SUBMIT" button without an input field to type the email or username for recovering
- By inspecting around the submit button, we can find this snippet of html code
```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```
- There is hidden field with prefilled email value "webmaster@borntosec.com"
- Remove the `type="hidden"` to get the email input filed
- Change the prefilled value, then click on "SUBMIT"

## How to exploit the breach
- The website hard-coded an email address in the html and hid it with a hidden filed, but the value stays in the html and can be easily accessed inspecting the page.
- The email address might be the admin email used as login username somewhere, once we have the email, we can brutal force the login by trying to login with the email and tons of common/breached passwords
- If this email value is not supposed to be changed and is used as the destination of some mails containing sensitive information, by changing the value to another email adress we have access to, we can intercept these information.

## What's the correct way
- Never put sensitive information in the html code even if it's a hidden field.