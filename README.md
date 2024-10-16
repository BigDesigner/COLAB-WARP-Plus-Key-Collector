# WARP+ Key Collector

This repository contains a Python notebook for collecting and organizing keys from various Telegram channels related to WARP Plus. The tool utilizes web scraping techniques to extract keys and their associated timestamps from specified Telegram pages.

## Features

- **Web Scraping**: The notebook scrapes messages from multiple Telegram channels to gather WARP Plus keys.
- **Timestamp Grouping**: Keys are organized by their timestamps, making it easier to track when each key was posted.
- **Downloadable Output**: The collected keys are saved to a text file that can be easily downloaded for further use.

## Requirements

- Python 3
- `requests` library for making HTTP requests
- `BeautifulSoup` from `bs4` for parsing HTML
- `defaultdict` from `collections` for organizing data
- `datetime` for handling timestamps

## Usage

1. Open the notebook in [Google Colab](https://colab.research.google.com/github/BigDesigner/WARP-Plus-Key-Collector/blob/main/Warp-plus-key-collector.ipynb).
2. Run the code cells sequentially. The script will scrape the specified Telegram channels for keys.
3. After execution, a downloadable text file containing the collected keys will be generated.

## Telegram Channels Scraped

The following Telegram channels are included in the scraping process:

- [warpplus](https://t.me/s/warpplus)
- [warppluscn](https://t.me/s/warppluscn)
- [warpPlusHome](https://t.me/s/warpPlusHome)
- [warp_veyke](https://t.me/s/warp_veyke)

## Notes

- Ensure that you have the necessary permissions to scrape data from the specified Telegram channels.
- The scraping might be subject to the terms of service of Telegram and the respective channel owners.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
