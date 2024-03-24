## How we found the flag
- We clicked on "© BornToSec" at the bottem of every page, with leaded us to "http://{ip}/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
- We start to investaging the html of the page, and we found 
```
<!--
    You must come from : "https://www.nsa.gov/".
-->
<!--
    Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
- We make a GET request on Postman and set the Header
    - Referer: https://www.nsa.gov/
    - User-Agent: ft_bornToSec

## How to exploit the breach
- Getting different information vy changing the header

## What's the correct way
- Don't fully trust the information on header, and render important information on the page. Header is easy to modify in request.