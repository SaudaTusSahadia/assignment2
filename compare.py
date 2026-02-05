import requests
import csv
from bs4 import BeautifulSoup

# --- PART A & B: LOAD DATA ---
with open("index.html", "r") as f:
    local_soup = BeautifulSoup(f, "html.parser")

web_url = "https://www.html5webtemplates.co.uk/wp-content/uploads/2020/templates/black_pink_white/index.html"
response = requests.get(web_url)
web_soup = BeautifulSoup(response.text, "html.parser")

# --- PART C: EXTRACT DATA ---
local_title = local_soup.title.string.strip() if local_soup.title else "No Title"
web_title = web_soup.title.string.strip() if web_soup.title else "No Title"

local_h1 = local_soup.find("h1").text.strip() if local_soup.find("h1") else "None"
web_h1 = web_soup.find("h1").text.strip() if web_soup.find("h1") else "None"

# --- PART D: SAVE TO CSV ---
filename = "comparison_results.csv"

# Define the data structure
data = [
    ["Element", "Local File", "Web URL", "Match?"],
    ["Title", local_title, web_title, local_title == web_title],
    ["H1 Heading", local_h1, web_h1, local_h1 == web_h1]
]

with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Comparison complete! Results saved to {filename}")
