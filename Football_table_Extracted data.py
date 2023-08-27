#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd 
from bs4 import BeautifulSoup


# In[18]:


url = "https://www.skysports.com/premier-league-table"
response = requests.get(url)
#print(response)


# In[19]:


soup = BeautifulSoup(response.content,"html.parser")
print(soup)


# In[20]:


league_table = soup.find("table",class_="standing-table__table")
print(league_table)


# In[34]:


for team in league_table.find_all("tbody"):
    rows = team.find_all("tr")
    for row in rows:
        pl_team = row.find("td", class_="standing-table__cell standing-table__cell--name").text.strip()
        pl_points = row.find_all("td", class_="standing-table__cell")[9].text
        
        print(pl_team, pl_points)


# In[35]:


for row in rows:
            columns = row.find_all('td')
            data = [column.get_text(strip=True) for column in columns]
            print(data)


# In[ ]:





# In[ ]:





# In[41]:


import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Font

# Send a GET request to the URL and get the HTML response
URL_Link = 'https://www.skysports.com/premier-league-table'
response = requests.get(URL_Link)

# Parse the HTML response with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table that contains the state and capital names
table = soup.find("table", class_="standing-table__table")

# Create a new Excel workbook to save the data
wb = Workbook()
ws = wb.active

# Set headers and make them bold
headers = ["#", "Team", "Pl", "W", "D", "L", "F", "A", "GD", "Pts"]
for col_num, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_num, value=header)
    cell.font = Font(bold=True)

# Loop through the rows of the table and extract the data
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    if len(cells) >= 10:
        row_data = [cell.text.strip() for cell in cells]
        ws.append(row_data)

# Save the workbook into a file
wb.save('Football_table.xlsx')


# In[ ]:




