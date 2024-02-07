# import requests
import datetime
from bs4 import BeautifulSoup
import requests

tldr_base_url = 'https://tldr.tech'

categories = {
    "tech": "2018-09-14",
    "webdev": "2023-12-04",
    "ai": "2023-02-13",
    "infosec": "2024-01-03",
    "product": "2023-12-01",
    "devops": "2023-12-01",
    "founders": "2024-01-03",
    "design": "2023-08-29",
    "marketing": "2023-12-04",
    "crypto": "2022-01-10",
}

def scrape_path(category, date):
    url = f'{tldr_base_url}/{category}/{date}'
    response = requests.get(url)
    valid = response.headers.get('x-matched-path').endswith('/[date]')
    return response if valid else None

def find_earliest_date(category):
    current_date = datetime.datetime.now()
    grace = 14
    earliest_date = None
    while True:
        current_date = current_date - datetime.timedelta(days=1)
        current_date_str = current_date.strftime('%Y-%m-%d')
        response = scrape_path(category, current_date_str)
        if response is None:
            grace -= 1
        else:
            grace = 14
            earliest_date = current_date_str

        if grace == 0:
            return earliest_date
