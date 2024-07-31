import json
import asyncio
import websockets

from helper.auth import request_token
from helper.websocket import backend_responses


async def main(org_name: str, head_name: str, api_key: str = None):
    async with websockets.connect(
        f"wss://chat-origin.api.unith.live/api/v2/switch/{org_name}/{head_name}"
    ) as websocket:

        # create auth info
        user_id, token = request_token()
        auth_info = {"token": token, "api_key": api_key or ""}

        # establish connection
        try:
            await websocket.send(json.dumps(auth_info))
            await backend_responses(websocket)
        except:
            return

        message = {
            "id": 0,
            "user_id": user_id,
            "event": "text",
        }

        while True:
            message["text"] = input("Enter a message:")
            try:
                await websocket.send(json.dumps(message))
            except websockets.exceptions.WebSocketException as e:
                print("error generating message")

            await backend_responses(websocket)


if __name__ == "__main__":
    # asyncio.run(main("org_name", "head_name", "api_key"))
    asyncio.run(main("unith", "aiko"))
