## How we found the flag
- when i inspecting the html code on the website, i found the link to the facebook,twitter,instagram is coded as below
```
<ul class="icons">
    <li><a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a></li>
    <li><a href="index.php?page=redirect&amp;site=twitter" class="icon fa-twitter"></a></li>
    <li><a href="index.php?page=redirect&amp;site=instagram" class="icon fa-instagram"></a></li>
</ul>
```
- From the content, the a tag is redirect the user back to the index page, and with paraemeter of page and site
- So, we changed the parameter of site to something else, the redirection failed to make it and we got the flag

## How to exploit the breach
- Manipulating the "site" parameter in the URL to arbitrary values, such as deviating from intended values like "facebook," "twitter," or "instagram," causes the redirection mechanism to fail, resulting in retention on the index page and potential exposure of sensitive information like flags or vulnerabilities within the redirection functionality.

## What's the correct way
- Direct Linking without Redirection: Instead of utilizing redirection with parameters, provide direct links to the respective social media platforms without any intermediary redirection.
