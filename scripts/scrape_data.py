import csv
import logging

# Define the file paths
scraped_data_file = r"C:\Users\user\Desktop\10 Acedamy W5\All Data\scraped_data.csv"
clean_data_file = r"C:\Users\user\Desktop\10 Acedamy W5\All Data\clean_data.csv"
log_file = r"C:\Users\user\Desktop\10 Acedamy W5\All Data\scraper.log"

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO)

# Test Data to Write
scraped_data = [
    ["Channel Name", "Channel Link"],  # Header row
    ["ExampleChannel1", "https://t.me/example1"],
    ["ExampleChannel2", "https://t.me/example2"]
]

cleaned_data = [
    ["Cleaned Channel Name", "Cleaned Channel Link"],  # Header row
    ["ExampleChannel1_Cleaned", "https://t.me/example1_cleaned"],
    ["ExampleChannel2_Cleaned", "https://t.me/example2_cleaned"]
]

# Write to scraped_data.csv
try:
    with open(scraped_data_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in scraped_data:
            writer.writerow(row)
    logging.info("Scraped data written successfully.")
except Exception as e:
    logging.error(f"Failed to write scraped data: {e}")

# Write to clean_data.csv
try:
    with open(clean_data_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in cleaned_data:
            writer.writerow(row)
    logging.info("Cleaned data written successfully.")
except Exception as e:
    logging.error(f"Failed to write cleaned data: {e}")
