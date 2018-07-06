import requests
from bs4 import BeautifulSoup

# Initialize variables for later use
playerdatasaved = ''
playerdata = ''
header = " ,Name,Team,Position,Age,Games,Minutes,Min%,Usg%,TO_rate,FTA," + \
         "FT%,2PA,2P%,3PA,3P%,eFG%,TS%,Points,Rebounds,TRB%,Assists," + \
         "AST%,Steals,Blocks,TOs,Versatility,O_RTG,D_RTG"

# Link to html to pull out of
r = requests.get("https://www.nbastuffer.com/2017-2018-nba-player-stats/")

# Grab the html data from the link above
soup = BeautifulSoup(r.content, "html.parser")
# Find the table with the html id of 'tablepress-7'
table = soup.find('table', id='tablepress-7')
# Find all table rows (tr) within that table and link them to the name "rows"
rows = table.find_all('tr')

# For each row, reset playerdata, then grab each column and separate by a ","
for row in rows:
    playerdata = ""
    for cols in row.findAll('td'):
        playerdata = playerdata + "," + cols.text
    # Add that row, separated by commas, to playerdatasaved in a new row
    playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

# Create/open test.csv, write the header, then write the playerdatasaved
file = open("test.csv", "w")
file.write(str(header))
file.write(playerdatasaved)
file.close()
