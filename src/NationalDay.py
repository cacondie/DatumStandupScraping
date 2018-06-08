from bs4 import BeautifulSoup
from titlecase import titlecase

class NationalDay():
    def __init__(self, http):
        self.Date=None
        self.Days = []
        self.http = http
        
    def get_days(self):
        base_address = "https://nationaldaycalendar.com/latest-posts"
        page = self.http.get_page(base_address)
        soup = BeautifulSoup(page.content, 'html.parser')
        entry_tag = soup.find('h2', class_="entry-title")
        days = entry_tag.text
        national_days = [titlecase(day) for day in days.split('–')]
        self.Date=national_days[0]
        self.Days=national_days[1:]