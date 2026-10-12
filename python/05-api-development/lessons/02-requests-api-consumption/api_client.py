import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post(post_id: int) -> dict:
    """Retrieve a post by its ID."""
    url = f"{BASE_URL}/posts/{post_id}"

    try:
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object.")

        return data

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error {error}")
    except requests.exceptions.Timeout:
        print("The API request timeout")
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the API.")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Unable to retrieve post {post_id}") from error


if __name__ == "__main__":
    try:
        post = get_post(2)

        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")

    except (RuntimeError, KeyError) as error:
        print(f"Error: {error}")
