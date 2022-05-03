from re import U


class News:
  def __init__(self,author,title,description,url,urlToImage,publishedAt,content):

    self.author=author
    self.title=title
    self.description=description
    self.url=url
    self.urlToImage=urlToImage
    self.publishedAt=publishedAt
    self.content=content

class Sites:
  def __init__(self,id,name,description,url,category,):

    self.id=id
    self.name=name
    self.description=description
    self.url=url
    self.category=category

class Sources:
  def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content):

    self.source=source
    self.author=author
    self.title=title
    self.description=description
    self.url=url
    self.urlToImage=urlToImage
    self.publishedAt=publishedAt
    self.content=content
