import json
import asyncio
import websockets


async def backend_responses(websocket: websockets.WebSocketClientProtocol):
    """ Awaits and prints all backend responses triggered by a user input message.

    The first message received is an echo message.

    Its possible to receive one or more response messages per user input message.

    The part_order key of the response represents the the order of response messages, starting from 0
    
    The is_last key for the last message is True, otherwise False

    Receives:
        An active websocket connection

    Returns:
        None
    """
    last_message = False

    while not last_message:
        try:
            recv = await asyncio.wait_for(websocket.recv(), timeout=30)

            message = json.loads(recv)
            print(f"Message received {message}")

            if message.get("is_last") == True:
                last_message = True

        except websockets.exceptions.WebSocketException as e:
            print(e)
            return
