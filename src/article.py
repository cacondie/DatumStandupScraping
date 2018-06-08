from typing import List, Any
from .article_data import ArticleData

class Article():
    Articles: List[ArticleData]

    def __init__(self, cat):
        self.Category = cat
        self.Articles = []
        self.ColumnWidth = 12

    def add_article(self,year,title,data):
        a = ArticleData(title, year, data)
        self.Articles.append(a)
        self.set_ColumnWidth()

    def __str__(self):
        return self.Category + " : " + len(self.Articles)

    def set_ColumnWidth(self):
        NumberOfArticles = 1 if len(self.Articles) == 0 else len(self.Articles)
        self.ColumnWidth = int(12 / NumberOfArticles)
