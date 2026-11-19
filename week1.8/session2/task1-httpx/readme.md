
# Task 1 - Using httpx

We will use a simple source of web data: [HTTPbin](https://httpbin.io/json)

This provides synthetic data and a REST API, with no authentication, for testing code.

## Create a virtual environment

See slide on `Installing httpx CLI`

## Instal httpx

`pip install 'httpx[cli]'`

## Command-line use

We can fetch data for a single post from the API with

`httpx https://httpbin.io/json​`

Note the reply and identify:
- HTTP status code: Status code 200 OK
- HTTP header HTTP/1.1
- Data (this format is called JSON, we will discuss it next) Date: Thu, 19 Nov 2026 16:24:50 GMT

## Other response codes

What is the difference if we request content that does not exist?

`httpx https://httpbin.io/jsoon​`
This will return a 404 error where item is not found.