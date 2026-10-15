import requests

# Read Data

url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url,timeout=10,verify=False)

# print(f"Status code : {response.status_code}")
# print(f"Response : {response.json()}")


# Post Data

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Python API Learning",
    "body": "Learning REST API integration",
    "userId": 1,
}

# response = requests.post(url,json=payload,timeout=10,verify=False)

# print(f"Status code : {response.status_code}")
# print(f"Response : {response.json()}")

# 6. Query Parameters

url = "https://jsonplaceholder.typicode.com/posts"


params = {
    "userId": 1,
    "_limit": 5,
}

# response = requests.get(url,params=params,timeout=10,verify=False)

# response.raise_for_status()

# posts = response.json()

# for post in posts:
#     print(post["id"],post["title"])

# 7. Request Headers

url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "Accept": "application/json",
}

# response = requests.get(
#     url,
#     headers=headers,
#     timeout=10,
#     verify=False
# )

# response.raise_for_status()

# print(response.json())

# 8. Handling HTTP Errors

# url = "https://jsonplaceholder.typicode.com/posts/1"
url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

# try:
#     response = requests.get(url, timeout=10,verify=False)
#     response.raise_for_status()
#     print(response.json())

# except requests.exceptions.HTTPError as error:
#     print(f"HTTP error: {error}")

# except requests.exceptions.Timeout:
#     print("The API request timed out.")

# except requests.exceptions.ConnectionError:
#     print("Unable to connect to the API.")

# except requests.exceptions.RequestException as error:
#     print(f"Request failed: {error}")

# 9. Validate API Responses


url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10, verify=False)
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
