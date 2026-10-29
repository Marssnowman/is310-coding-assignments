import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

BASE_URL = "https://minecraft.wiki"

HEADERS = {
    "User-Agent": "is310-course-scraper/1.0 (student project; cc149@illinois.edu)"
}

# Level 1: page containing the list of mobs
start_url = "https://minecraft.wiki/w/Mobs"

target_mobs = [
    "Creeper",
    "Pig",
    "Skeleton",
    "Zombie",
    "Spider",
    "Sheep",
    "Cow",
    "Chicken",
    "Slime",
    "Ghast"
]

response = requests.get(start_url, headers=HEADERS, timeout=10)

print("Status code:", response.status_code)

if response.status_code != 200:
    print("Could not access the mob list page.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

mob_links = []

# Find links for the 10 selected mobs from the main Mobs page
for mob_name in target_mobs:
    found_url = None

    for link in soup.find_all("a", href=True):
        if link.get_text(" ", strip=True) == mob_name:
            found_url = urljoin(BASE_URL, link["href"])
            break

    if found_url:
        mob_links.append({
            "name": mob_name,
            "url": found_url
        })
    else:
        print("Could not find link for:", mob_name)

results = []

# Level 2: visit each individual mob page
for mob in mob_links:
    time.sleep(1)

    page_response = requests.get(
        mob["url"],
        headers=HEADERS,
        timeout=10
    )

    if page_response.status_code != 200:
        print("Skipping:", mob["name"])
        continue

    page_soup = BeautifulSoup(page_response.text, "html.parser")

    description = ""

    # Find the first substantial paragraph
    for paragraph in page_soup.select(".mw-parser-output > p"):
        text = paragraph.get_text(" ", strip=True)

        if len(text) > 40:
            description = text
            break

    results.append({
        "mob_name": mob["name"],
        "page_url": mob["url"],
        "description": description
    })

    print("Scraped:", mob["name"])

with open("minecraft_mobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["mob_name", "page_url", "description"]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Saved {len(results)} records to minecraft_mobs.csv")