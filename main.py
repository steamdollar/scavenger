from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
from datetime import datetime
import asyncio

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv('API_HASH')
dot_room_id = int(os.getenv('TARGET_ROOM'))
target_id = int(os.getenv('TARGET_ID'))
my_chatroom_id = int(os.getenv('MY_ROOM'))
session_name = os.getenv("SESSION_NAME")

print("Application run...")

client = TelegramClient(session_name, api_id, api_hash)

print("Instance created")

async def periodic_message():
    while True:
        await client.send_message(my_chatroom_id, 'Periodic status message')
        await asyncio.sleep(43200)

async def my_event_handler(event):
    if event.sender_id == target_id:
        now = datetime.now()
        print("Target spoke", "time:", now.date(), now.time())
        await client.forward_messages(my_chatroom_id, event.message)

async def main():
    await client.start()
    print("Client started")
    client.loop.create_task(periodic_message())
    client.add_event_handler(my_event_handler, events.NewMessage(chats=dot_room_id))
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())