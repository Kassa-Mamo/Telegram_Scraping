 import asyncio
from telethon import TelegramClient
import csv
import os
import pandas as pd  # Added for Pandas functionality

# Define paths
DATA_FOLDER = r"C:\Users\user\Desktop\10 Acedamy W5\All Data"
CHANNELS_FILE = os.path.join(DATA_FOLDER, "channels_to_crawl.csv")
SCRAPED_FILE = os.path.join(DATA_FOLDER, "scraped_data.csv")
LOG_FILE = os.path.join(DATA_FOLDER, "scraper.log")

# Bot API token
bot_token = '8195121045:AAGhcNPKCcnuZ1Uh9qBhb-6nk1AvLdutok0'  # Replace with your Bot API Token

async def main():
    print("Connecting to Telegram bot...")
    async with TelegramClient('scraper', api_id=None, api_hash=None) as client:
        # Use the bot token for authentication
        await client.start(bot_token=bot_token)
        print("Connected to Telegram bot!")

        # Read channels using Pandas
        try:
            channels_df = pd.read_csv(CHANNELS_FILE)
            channels = channels_df['Channel Link'].tolist()  # Replace 'Channel Link' with the correct column name in your CSV
        except FileNotFoundError:
            print(f"Error: Channels file not found at {CHANNELS_FILE}")
            return
        except KeyError:
            print("Error: The 'Channel Link' column is missing in the CSV file")
            return

        # Prepare output CSV
        with open(SCRAPED_FILE, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['channel', 'sender', 'timestamp', 'message'])

            # Scrape messages
            for channel in channels:
                try:
                    print(f"Scraping channel: {channel}")
                    async for message in client.iter_messages(channel, limit=100):
                        writer.writerow([channel, message.sender_id, message.date, message.text])
                except Exception as e:
                    print(f"Error with channel {channel}: {e}")
                    with open(LOG_FILE, 'a') as log_file:
                        log_file.write(f"Error with channel {channel}: {e}\n")
    print("Scraping completed!")


# Run the async function
if __name__ == "__main__":
    # Check if already running inside an event loop
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # No running loop
        loop = None

    if loop and loop.is_running():
        print("Detected running event loop. Using create_task()")
        asyncio.create_task(main())
    else:
        print("No running event loop. Using asyncio.run()")
        asyncio.run(main())

