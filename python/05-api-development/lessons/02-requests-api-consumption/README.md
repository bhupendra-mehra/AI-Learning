# Lesson 02 — Consuming REST APIs with Python Requests

## 1. Learning Objectives

By the end of this lesson, I will be able to:

- Understand how Python communicates with REST APIs.
- Use the `requests` library to send HTTP GET and POST requests.
- Work with query parameters, headers, and JSON payloads.
- Read and validate API responses.
- Handle HTTP errors, timeouts, and connection failures.
- Build a reusable API client.

## 2. Prerequisites

- Python basics: variables, dictionaries, functions, and exceptions.
- Lesson 01: HTTP, REST, and JSON.
- Python virtual environment configured.
- Basic Git commands.

## 3. What Is the Requests Library?

The `requests` library allows Python applications to communicate with HTTP APIs.

For example, a Python application can use an API to:

- Retrieve customer information.
- Create an order.
- Fetch product details.
- Communicate with an AI model API.
- Retrieve data from an external service.

### Installation

```bash
python -m pip install requests
```

Import the library:

```python
import requests
```

## 4. HTTP GET Request

A GET request retrieves information from an API.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

print(response.status_code)
print(response.json())
```

Important properties:

- `response.status_code`: HTTP status code.
- `response.json()`: Parses a JSON response into Python data.
- `response.text`: Response body as text.
- `response.headers`: Response headers.
- `response.url`: Final response URL.

A successful response commonly returns status code `200`.

## 5. HTTP POST Request

A POST request commonly creates a resource or submits data.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Python API Learning",
    "body": "Learning REST API integration",
    "userId": 1,
}

response = requests.post(
    url,
    json=payload,
    timeout=10,
)

print(response.status_code)
print(response.json())
```

Use the `json` parameter to send a Python dictionary as JSON.

**Note:** JSONPlaceholder is a testing API. A successful POST simulates creation; it does not permanently save the new resource.

## 6. Query Parameters

Query parameters filter or customize API requests.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,
    "_limit": 5,
}

response = requests.get(
    url,
    params=params,
    timeout=10,
)

response.raise_for_status()

posts = response.json()

for post in posts:
    print(post["id"], post["title"])
```

The `params` argument encodes query parameters into the URL.

## 7. Request Headers

Headers provide additional information to the server.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "Accept": "application/json",
}

response = requests.get(
    url,
    headers=headers,
    timeout=10,
)

response.raise_for_status()

print(response.json())
```

Common headers include:

- `Accept`: Expected response format.
- `Content-Type`: Format of the request body.
- `Authorization`: Credentials or access token.

Never hardcode real API keys or access tokens in source code.

## 8. Handling HTTP Errors

An HTTP response can indicate failure even when the request itself completed successfully.

Use `raise_for_status()` to raise an exception for unsuccessful HTTP status codes.

```python
import requests

url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    print(response.json())

except requests.exceptions.HTTPError as error:
    print(f"HTTP error: {error}")

except requests.exceptions.Timeout:
    print("The API request timed out.")

except requests.exceptions.ConnectionError:
    print("Unable to connect to the API.")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
```

Important exception types:

- `HTTPError`: An unsuccessful HTTP status after calling `raise_for_status()`.
- `Timeout`: The request exceeded its timeout.
- `ConnectionError`: A connection problem occurred.
- `RequestException`: Base class for request-related exceptions.

A timeout prevents a request from waiting indefinitely. Production applications may also require retries and appropriate logging.

## 9. Validate API Responses

Do not assume that every response contains the fields your application expects.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    post = response.json()

    if not isinstance(post, dict):
        raise ValueError("Expected a JSON object.")

    if "title" not in post:
        raise ValueError("Missing title field.")

    print(post["title"])

except (
    requests.exceptions.RequestException,
    ValueError,
) as error:
    print(f"API processing failed: {error}")
```

Response validation protects your application from unexpected data structures.

## 10. Mini-Project: Reusable API Client

Create a file named `api_client.py` in this lesson folder.

```python
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post(post_id: int) -> dict:
    """Retrieve a post by its ID."""
    url = f"{BASE_URL}/posts/{post_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object.")

        return data

    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            f"Unable to retrieve post {post_id}"
        ) from error


if __name__ == "__main__":
    try:
        post = get_post(1)

        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")

    except (RuntimeError, KeyError) as error:
        print(f"Error: {error}")
```

Run the project:

```bash
python api_client.py
```

Expected result: the program displays the ID, title, and body of post 1 when the API is available.

## 11. Magento / PHP Comparison

| Python                 | PHP                                             |
| ---------------------- | ----------------------------------------------- |
| `requests.get()`       | HTTP client GET request                         |
| `requests.post()`      | HTTP client POST request                        |
| `response.json()`      | `json_decode()`                                 |
| `response.status_code` | HTTP response status                            |
| `raise_for_status()`   | Explicit status checking and exception handling |

In Magento 2, external API integrations commonly use an HTTP client such as `Magento\Framework\HTTP\Client\Curl`. Python's `requests` library serves a similar purpose in Python applications.

## 12. Exercises

### Exercise 1 — Retrieve a Post

- Retrieve post ID 5.
- Print its title and body.
- Check the response status.

### Exercise 2 — Retrieve Multiple Posts

- Fetch posts for `userId=2`.
- Limit the results to five.
- Print each post's ID and title.

### Exercise 3 — Create a Post

- Submit a POST request with a title, body, and user ID.
- Print the response status and JSON body.
- Explain why the testing API does not permanently save the post.

### Exercise 4 — Handle Failures

- Request an invalid endpoint.
- Handle HTTP errors.
- Configure a timeout.
- Handle connection failures.

### Exercise 5 — Improve the API Client

- Allow the post ID to be passed as a function argument.
- Validate the response structure.
- Keep HTTP handling separate from output formatting.

## 13. Completion Checklist

- [x] Installed `requests`.
- [x] Completed a GET request.
- [x] Completed a POST request.
- [x] Used query parameters and headers.
- [x] Parsed and validated JSON responses.
- [x] Handled HTTP errors and timeouts.
- [x] Built and tested `api_client.py`.
- [x] Completed the exercises.
- [x] Committed the lesson to Git.

## 14. Key Takeaways

- REST APIs allow applications to exchange data over HTTP.
- `requests` makes HTTP communication straightforward in Python.
- Use `response.json()` to parse JSON responses.
- Use `raise_for_status()` to detect HTTP errors.
- Set timeouts for network requests.
- Validate external data instead of trusting its structure.
- Keep API communication reusable and separate from business logic.