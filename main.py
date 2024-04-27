import os
import re
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup


def download_sdo_images(path, start_date, end_date, resolution, channels):
    # Create directory to save images if it doesn't exist
    os.makedirs(path, exist_ok=True)

    # Convert start and end dates to datetime objects
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date = start

    failures = []
    while date <= end:
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")

        # Build the URL to fetch the HTML page
        url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all <a> tags, extract href and filter based on regex
            all_links = [a['href'] for a in soup.find_all('a', href=True)]
            image_pattern = re.compile(f".*_{resolution}_(?:{'|'.join(channels)}).jpg")
            links = list(filter(lambda a: image_pattern.match(a), all_links))

            # Download each image
            for link in links:
                image_url = f"https://sdo.gsfc.nasa.gov/assets/img/browse/{year}/{month}/{day}/{link}"
                img_response = requests.get(image_url)
                if img_response.status_code == 200:
                    with open(f'sdo_images/{link}', 'wb') as f:
                        f.write(img_response.content)
                    print(f"Downloaded {link}")
                else:
                    print(f"Failed to download {link}")
                    failures.append(link)
        else:
            print(f"Failed to retrieve image listing for {date.strftime('%Y-%m-%d')}")

        # Increment the date by one day
        date += timedelta(days=1)
    print(f"Found {len(failures)}: {failures}")


if __name__ == '__main__':
    # Change these settings
    path = "sdo_images"
    start_date = "2023-01-01"
    end_date = "2023-01-02"
    # Available resolutions: 4096 2048 1024 512
    resolution = "4096"
    # Available channels: 0094 0131 0171 0193 0211 0304 0335 1600 1700 HMIB HMII HMID HMIBC HMIIF HMIIC
    channels = ["0094", "0131", "0171", "0193", "0211", "0304", "0335", "1600", "1700", "HMIB", "HMII", "HMID", "HMIBC",
                "HMIIF", "HMIIC"]

    download_sdo_images(path, start_date, end_date, resolution, channels)
