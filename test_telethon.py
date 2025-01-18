from telethon import TelegramClient

# Replace with your API credentials
api_id = 20173022  # Your API ID
api_hash = 'bab4a3351ed7634a8c1a3f8767fcf75c'  # Your API Hash

async def test_connection():
    async with TelegramClient('test_session', api_id, api_hash) as client:
        print("Successfully connected to Telegram!")

import asyncio
asyncio.run(test_connection())
