# script para obtener datos meteorológios
# cargar las librerías
import pandas as pd
import requests
from bs4 import BeautifulSoup

# consulta a servidor
URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL).text

# HTML
soup = BeautifulSoup(req, 'lxml')
table = soup.find('table', attrs={'id':'weather_records'}) # tabla en HTML

# elaboración del DataFrame
columns_head = []
records = []

for row in table.find_all('th'):    
    columns_head.append(row.text)
    
for row in table.find_all('tr'):
    if not row.find_all('th'):
        records.append(celda.text for celda in row.find_all('td'))
        
weather_records = pd.DataFrame(data=records, columns=columns_head) # DataFrame

# mostrar primeros 5
print(weather_records.head())
