## 0x11. Python - Network #1

urllib is a Python module that can be used for opening and reading URLs. It defines functions and classes to help with URL actions (basic and digest authentication, redirections, cookies, etc). Here's a simple example of how to use it
```
from urllib.request import urlopen
data = urlopen("http://www.google.com").read()
```
On the other hand, requests is a Python module for HTTP requests that aims to be more user-friendly than urllib. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application. Here's a similar example using requests:
```
import requests
response = requests.get("http://www.google.com")
data = response.text
```
Both libraries can be used to send HTTP/1.1 requests. With it, you can add form data, multipart files, and parameters via simple Python libraries to HTTP requests.


## Tasks/Files

|      Tasks          |Files               |
|----------------|-------------------------------|
|0. What's my status? #0|`0-hbtn_status.py`|
|1. Response header value #0|`1-hbtn_header.py`|          
|2. POST an email #0|`2-post_email.py`|
|3. Error code #0|``3-error_code.py``| 
|4. What's my status? #1|``4-hbtn_status.py``| 
|5. Response header value #1|``5-hbtn_header.py``| 
|6. POST an email #1|``6-post_email.py``|       
|7. Error code #1|``7-error_code.py``| 
|8. Search API|``8-json_api.py``| 
|9. My GitHub!|``10-my_github.py``|
