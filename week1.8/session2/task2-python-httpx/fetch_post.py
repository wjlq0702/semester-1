"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object
print(response.status_code) # Line of code from the test has found the status_code
if response.status_code == 200:
    print(response.json())
else:
    print("Error has occured")      # response object, json() method