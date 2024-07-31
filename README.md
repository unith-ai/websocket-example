# WebSocket Client Example

This README provides an overview of the WebSocket client example, explaining how to use it and how it works.

## Overview

This WebSocket client example allows you to connect to a chat server, send messages, and receive responses. It's designed to work with the Unith chat API.

## Files

The example consists of four main Python files:

1. `main.py`: The main script that sets up the WebSocket connection and handles user input.
2. `websocket.py`: Contains a helper function to handle backend responses.
3. `videos.py`: Provides a function to fetch idle video URLs (not directly used in the WebSocket communication).
4. `auth.py`: Handles authentication with the chat-origin API.

## Prerequisites

- Python 3.7 or higher
- `websockets` library
- `requests` library

Install the required libraries using pip:

```
pip install websockets requests 
```

## Usage

1. Open `main.py` and modify the following parameters in the `main()` function call at the bottom of the file:
   - `org_name`: Your organization name
   - `head_name`: The name of the AI head you want to communicate with
   - `api_key`: Your API key (optional)

2. Run the script:

```
python main.py
```

3. Once connected, you can enter messages when prompted. Type your message and press Enter to send it to the server.

4. The script will display the responses from the server.

5. To exit the program, use Ctrl+C or close the terminal.

## How It Works

1. **Authentication**:
   - The `request_token()` function in `auth.py` is called to authenticate with the chat-origin API.
   - It sends a POST request to the API with hardcoded anonymous credentials.
   - The function returns a user ID and access token, which are used for subsequent communications.

2. **Connection Establishment**:
   - The `main()` function in `main.py` establishes a WebSocket connection to the Unith chat API.
   - It uses the user ID and token obtained from the authentication step, along with an optional API key, to create the authentication information.
   - This auth info is sent to the server to establish the connection.

3. **Message Sending**:
   - The script enters a loop where it prompts the user for input.
   - Each message is sent to the server as a JSON object containing the user ID, event type, and message text.

4. **Receiving Responses**:
   - The `backend_responses()` function in `websocket.py` handles incoming messages from the server.
   - It prints each received message and continues until it receives a message with `is_last` set to `True`.

5. **Error Handling**:
   - The script includes basic error handling for WebSocket exceptions and authentication failures.

6. **Idle Video Fetching** (not directly used in WebSocket communication):
   - The `fetch_idle_video()` function in `videos.py` can be used to retrieve the URL of an idle video for the AI head.

## Authentication Details

The `auth.py` file contains the `request_token()` function, which handles the authentication process:

- It sends a POST request to `https://chat-origin.api.unith.live/token` with hardcoded credentials (username: "anonymous", password: "Password1").
- If successful, it extracts the `user_id` and `access_token` from the response.
- These credentials are then used in the main script to authenticate the WebSocket connection.

Note: The use of hardcoded credentials is generally not recommended for production environments. In a real-world scenario, you would typically use more secure authentication methods.

## Notes

- The current implementation uses a hardcoded organization name ("unith") and head name ("aiko"). Modify these in the `main()` function call if needed.
- The API key is optional. If not provided, an empty string will be sent.
- The script will continue running and allowing message input until manually terminated.
- The authentication process uses anonymous credentials. In a production environment, you would typically use more secure authentication methods.

## Troubleshooting

- If you encounter connection issues, ensure your internet connection is stable and that you're using the correct organization name and head name.
- Check that your API key (if used) is valid and has the necessary permissions.
- If authentication fails, check that the authentication endpoint is correct and that the anonymous credentials are still valid.
- If you receive unexpected responses or errors, check the Unith API documentation for any recent changes or updates.

For more information or support, please refer to the Unith API documentation or contact their support team.