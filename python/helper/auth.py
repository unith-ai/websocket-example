import requests

from typing import Tuple


def request_token() -> Tuple[str, str]:
    """
    Authenticate against the chat-origin API and retrieve user credentials.

    Returns:
        Tuple[str, str]: A tuple containing the user ID and access token.
            Returns (None, None) if the request fails or the expected fields are not found.
    """
    payload = {"username": "anonymous", "password": "Password1"}
    session = requests.Session()

    try:
        response = session.post(
            "https://chat-origin.api.unith.live/token", data=payload
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None, None

    json_response = response.json()
    user_id = json_response.get("user_id")
    access_token = json_response.get("access_token")

    return user_id, access_token
