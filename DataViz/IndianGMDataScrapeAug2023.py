import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Indian_chess_players'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tables = soup.find_all('table', class_='wikitable')

# Assuming the table you want is the 6th table on the page
GM_data = tables[5]

state_list = []
state_counts = {}

for row in GM_data.find_all('tr')[1:]:  # Skip the header row
    td_elements = row.find_all('td')

    if len(td_elements) >= 3:
        state = td_elements[2].get_text(strip=True)
        state_list.append(state)

# filling dict
for stateName in state_list:
    if stateName in state_counts:
        state_counts[stateName] += 1
    else:
        state_counts[stateName] = 1

sorted_state_count = dict(
    sorted(state_counts.items(), key=lambda item: item[1], reverse=True))

print(sorted_state_count)
