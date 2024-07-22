class Article:
    def __init__(self, title, date, link, summary, image, provider):
        self.provider_name = provider
        self.image = image
        self.title = title
        self.date = date
        self.link = link
        self.author = None
        self.summary = summary
