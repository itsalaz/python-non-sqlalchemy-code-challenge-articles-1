class Article:

    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception('Author must be an Author')
        if not isinstance(magazine, Magazine):
            raise Exception('Magazine must be a Magazine')
        self.author = author 
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, 'title'):
            self._title = title
        else:
            raise Exception('Title must be a title between 5 and 50 characters and cannot be changed after instantiated')

class Author:
    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception('Name must be a string greater than 0 characters and cannot be changed after instantiation')


    def articles(self):
        return [ article for article in Article.all if article.author == self ]

    def magazines(self):
        return list(set([ article.magazine for article in Article.all if article.author == self ]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
            
    def topic_areas(self):
        if not self.articles():
            return None
        else:
            return list(set([article.magazine.category for article in self.articles()]))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if isinstance (name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception('Name must be a string between 2 and 16 characters')

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception('Category must be a string greater than zero')

    def articles(self):
        return [ article for article in Article.all if article.magazine == self ]

    def contributors(self):
        return list(set([ article.author for article in Article.all if article.magazine == self ]))

    def article_titles(self):
            articles = [ article.title for article in Article.all if article.magazine == self ]
            return articles if articles else None
    

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        
        actual_authors = [author for author, count in author_count.items() if count > 2]
        if not  actual_authors:
            return None
        else:
            return actual_authors
                
