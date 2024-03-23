## How we found the flag
- From the main page, click on "SIGN IN", then click on "Add images" (http://{ip}/?page=upload)
- The page is designed to upload an image to the site, with one html upload tag, and when i can selected a image, but when i selected a non-image file, i got "Your image was not uploaded."
- The protection seems to nice from the website, so i tried to make to request with the curl command 
```
 curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" "http://192.168.56.101/index.php?page=upload" | grep 'The flag is :'
```
- In this command, i make the uploaded file recognize as jpeg with "type=image/jpeg" while the file is actually a php file, and the request went through, 


## How to exploit the breach
- Bypassing File Upload Restrictions: Manipulate file extension and content-type headers to disguise PHP code as image files with JPEG extensions, exploiting the server's validation mechanism for arbitrary code execution and unauthorized access.

- Command Injection via CURL Request: Craft a POST request using CURL to upload a malicious file disguised as an image, bypassing validation and potentially compromising sensitive data by executing arbitrary PHP code on the server.

- Exploiting Lack of Input Sanitization: Inject malicious commands or scripts into file uploads due to inadequate input sanitization, allowing for the embedding of PHP code within image data to gain unauthorized access or manipulate data.

## What's the correct way
- Enhance validation to check both file extensions and content types thoroughly.
- Double check file type at the server side before proceeding anything
- Employ whitelist-based validation to restrict uploads to known safe file types.