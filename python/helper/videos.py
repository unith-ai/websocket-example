import requests


def fetch_idle_video(org_name: str, head_name: str) -> str:
    """
    Fetches the URL of the corresponding Idle Video from the chat-origin API

    Returns:
        str: A string that is representing the URL of the idle video stored in an s3 Bucket.
            Returns None if the request fails.
    """
    try:

        response = requests.get(
            f"https://chat-origin.api.unith.live/api/v1/videos/{org_name}/{head_name}"
        )
        response.raise_for_status()
        head_values = response.json()
        video_id = head_values[0].get("video_id")

        idle_video_url = requests.get(
            f"https://chat-origin.api.unith.live/api/v1/idle/{org_name}/{head_name}/{video_id}"
        )
        idle_video_url.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

    idle_video_url = idle_video_url.json()

    return idle_video_url
