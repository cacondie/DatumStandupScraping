from bs4 import BeautifulSoup,Tag
from src.article import Article

class ThisDayInHistory:
    def __init__(self, http):
        self.http = http

    def get_articles(self):
        art = None
        page = self.http.get_page("https://www.history.com/this-day-in-history")
        soup = BeautifulSoup(page.content, 'html.parser')
        side_bar = soup.find('div', class_="categories")
        list_items = side_bar.find_all('li')
        articles = []
        for item in list_items:
            contents = item.contents
            for c in contents:
                if(isinstance(c,Tag)):
                    nam = c.get('class')
                    if "category" in nam:
                        art = Article(c.text)
                        articles.append((art))
                    elif "year" in nam:
                        article_data=self.get_article_data(item)
                        art.add_article(c.text,article_data[0], article_data[1])
                        break
        return articles

    def get_article_data(self,title):
        base_address = "https://www.history.com"

        new_links = title.find_all('a', href=True)
        title = new_links[0].text
        new_page = base_address + new_links[0]['href']
        sub_page = self.http.get_page(new_page)
        new_soup = BeautifulSoup(sub_page.content, 'html.parser')
        content = new_soup.find_all('article')
        return title, content[0].text




