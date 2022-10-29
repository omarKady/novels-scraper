# pip3 install requests
# pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
import pygsheets
import pandas as pd

order = []
titles = []
writers = []
countries = []

def import_to_google_sheet(csv_file):
    if csv_file:
        #authorization
        gc = pygsheets.authorize(service_file='/home/omar/Downloads/web-scrappint-g-sheet-3042f849f4cf.json')
        sh = gc.open('Sheet1')
        wks = sh[0]


def write_to_excel(columns,order,titles,writers,countries):
    lines = zip(order,titles,writers,countries)
    with open("novels.csv","w") as my_file:
        wr = csv.writer(my_file)
        wr.writerow(columns)
        wr.writerows(lines)
    import_to_google_sheet(my_file)


def scrap_novels(url):
    site_result = requests.get(page_url)
    source = site_result.content
    soup = BeautifulSoup(source, "lxml")
    novels_table = soup.find('table', {"class":"wikitable"})
    columns = [i.get_text(strip=True) for i in novels_table.find_all('th')]
    data = []
    for tr in novels_table.find("tbody").find_all("tr"):
        data.append([td.get_text(strip=True) for td in tr.find_all("td")])

    for row in data:
        if row:
            order.append(row[0])
            titles.append(row[1])
            writers.append(row[2])
            countries.append(row[3])
    write_to_excel(columns,order,titles,writers,countries)


page_url = "https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9"
scrap_novels(page_url)