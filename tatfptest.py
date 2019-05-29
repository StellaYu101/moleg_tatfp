# SETUP
import urllib2, csv
from bs4 import BeautifulSoup

# SETUP CSV
csvfile = open('tatfp.csv', 'w')
tatfp_writer = csv.writer(csvfile)

# GETTING THE WEBSITE
url = 'https://www.senate.mo.gov/19info/BTS_Web/TrulyAgreed.aspx?SessionType=R'
html = urllib2.urlopen(url).read()

# PROCESSING THE HTML
soup = BeautifulSoup(html, 'html.parser')

# SCRAPING THE DATA

tables = soup.find_all('table', {'id': 'Table2'})

for table in tables:
    
    rows = table.find_all('tr')

    for row in rows:
        data = []

        cells = row.find_all('td')

        for cell in cells:
            data.append(cell.text.strip().encode('utf-8'))
            #strip is a string method to trim down whitespaces, which means it can only follow a text object. Therefore, here we use text.strip() instead of strip() alone.
            
        tatfp_writer.writerow(data)
       

        


            
