import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

html = requests.get('https://www.ssa.gov/employer/ssnvhighgroup.htm').text
soup = BeautifulSoup(html, "html.parser")
base_url = 'https://www.ssa.gov/employer/'

final = pd.DataFrame(columns=['date', 'area_number', 'highest_group_number', 'changed'])

def filt(x):
    global final
    if '\t' in x.line and x.line[0].isnumeric():
        for y in range(0, len(x.line.strip().split()), 2):
            if x.line.split()[y]:
                final = final.append({'date':the_date, 'area_number':x.line.split()[y], 'highest_group_number':x.line.split()[y+1].replace('*', ''), 'changed': 'x' if '*' in x.line.split()[y+1] else ''}, ignore_index=True)

for x in soup.find_all('a', {'href': re.compile('.*.txt')}):
    temp = pd.read_csv(base_url + x['href'], header=None)
    temp.columns = ['line']
    the_date = temp.line[0].split()[-1]
    temp.apply(filt, axis=1)

final.to_csv('highest_group_numbers.csv', index=False)