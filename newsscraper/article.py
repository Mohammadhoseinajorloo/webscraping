class Article:
    def __init__(self, title, date, link, summary, image):
        self.image = image
        self.title = title
        self.date = date
        self.link = link
        self.author = None
        self.summary = summary
