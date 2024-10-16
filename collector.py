import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime

# Telegram channel pages
urls = [
    'https://t.me/s/warpplus',
    'https://t.me/s/warppluscn',
    'https://t.me/s/warpPlusHome',
    'https://t.me/s/warp_veyke'
]

# A dictionary that groups keys by timestamps
keys_by_url = defaultdict(lambda: defaultdict(list))

# Loop through each URL
for url in urls:
    # Fetch the HTML content of the page
    response = requests.get(url)
    html_content = response.text

    # Analyze the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Select <div> tags to find messages and timestamps
    message_blocks = soup.find_all('div', class_='tgme_widget_message')

    # Get the timestamp and keys for each message block
    for message in message_blocks:
        # Get the timestamp
        timestamp = message.find('time')
        if timestamp:
            # Create date and time information
            timestamp_text = timestamp['datetime']  # Using the "datetime" attribute
            timestamp_date = datetime.fromisoformat(timestamp_text).strftime('%Y-%m-%d %H:%M')
        else:
            timestamp_date = "Unknown"

        # Select <code> tags to find keys
        code_elements = message.find_all('code')
        keys = [code.text for code in code_elements]

        # If there are keys, add them to the list with the timestamp
        if keys:
            for key in keys:
                keys_by_url[url][timestamp_date].append(key)

# Write the keys to a file
file_path = '/content/keys.txt'
with open(file_path, 'w') as file:
    for url, timestamp_keys in keys_by_url.items():
        file.write(f"URL: {url}\n")  # Write the URL
        # Sort the timestamps in descending order
        for timestamp in sorted(timestamp_keys.keys(), reverse=True):
            keys = timestamp_keys[timestamp]
            file.write(f"{timestamp}\n")  # Write the date and time
            for key in keys:
                file.write(f"Key: {key}\n")  # Write the keys
        file.write("\n")  # Add a blank line

# Create a link to download the file
from google.colab import files
files.download(file_path)
