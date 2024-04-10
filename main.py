import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, folder_path):
    response = requests.get(url)
    body = BeautifulSoup(response.text, "html.parser")
    os.makedirs(folder_path, exist_ok=True)

    images = body.find_all("img")
    count = 1
    for img_tag in images:
        img_url = img_tag.get("src")
        if img_url:
            img_url = urljoin(url, img_url)
            img_response = requests.get(img_url)
            filename = f"{count:03}.jpg"
            count += 1
            with open(os.path.join(folder_path, filename), "wb") as image_file:
                image_file.write(img_response.content)
            print(f"Downloaded {filename}")

if __name__ == "__main__":
    webpage_url = input("Enter the webpage url: ")
    download_folder = input("Enter the directory path: ")

    download_images(webpage_url, download_folder)