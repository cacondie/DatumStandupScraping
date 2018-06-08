class ArticleData():
    def __init__(self, title, year, article):
        self.Title = title
        self.Year = year
        self.Article = article

    def __str__(self):
        return self.Year + ":" + self.Title