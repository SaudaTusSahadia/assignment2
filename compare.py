import requests
from bs4 import BeautifulSoup

# --- PART A: LOAD YOUR LOCAL FILE ---
with open("index.html", "r") as f:
    local_soup = BeautifulSoup(f, "html.parser")

# --- PART B: FETCH THE WEB PAGE ---
web_url = "https://www.html5webtemplates.co.uk/wp-content/uploads/2020/templates/black_pink_white/index.html"
response = requests.get(web_url)
web_soup = BeautifulSoup(response.text, "html.parser")

# --- PART C: COMPARE DATA ---
# 1. Compare Page Titles
local_title = local_soup.title.string if local_soup.title else "No Title"
web_title = web_soup.title.string if web_soup.title else "No Title"

print(f"--- TITLE COMPARISON ---")
print(f"Local: {local_title}")
print(f"Web:   {web_title}\n")

# 2. Compare Main Headings (H1)
local_h1 = local_soup.find("h1").text if local_soup.find("h1") else "None"
web_h1 = web_soup.find("h1").text if web_soup.find("h1") else "None"

print(f"--- HEADING COMPARISON ---")
print(f"Local H1: {local_h1}")
print(f"Web H1:   {web_h1}\n")

# --- PART D: SIMPLE LOGIC CHECK ---
if local_h1.strip() == web_h1.strip():
    print("MATCH: Both sites have the same main heading!")
else:
    print("DIFFERENT: The main headings do not match.")
