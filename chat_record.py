from telethon import TelegramClient, sync
import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv('API_HASH')
target_room_id = int(os.getenv('TARGET2_ROOMID'))
session_name = os.getenv("SESSION_NAME")

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    async with client:
        # Fetch the last 100 messages from the target chat room
        history = await client.get_messages(target_room_id, limit=10)
        for message in history:
            print(message.sender.id, message.text)

client.loop.run_until_complete(main())
