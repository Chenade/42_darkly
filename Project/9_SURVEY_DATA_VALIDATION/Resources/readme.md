## How we found the flag
- From the main page, click on "SURVEY" (http://{ip}/?page=survey)
- Notice that the grade select has values from 1 to 10, and once we select a value, the average gets affected right away and updates itself.
- By inspect these options, we see that they have a format of 
```
<option value="n">n</option>
```
- Modify the value to a large number like 100000 and choose the corresponding option on the page.

## How to exploit the breach
- In our case, the survey result is easily manipulated with the breach.

## What's the correct way 
- Never trust user input, always do data validation to make sure the input value stays within the desired range.
- Sanitize the input data before using it.