from app import app
import urllib.request,json
from .models import News,Sites,Sources


# News=news.News
# Sites=news.Sites
# Sources=news.Sources


# Getting api key
api_key = 'c4abb2dc4e3c4308b670a8e86481e3b0'

base_url='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

sites_url='https://newsapi.org/v2/top-headlines/sources?language=en&apiKey={}'

sources_url='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

def get_news():
  get_news_url = base_url.format(api_key)

  with urllib.request.urlopen(get_news_url)as url:
    get_news_data=url.read()
    get_news_response=json.loads(get_news_data)

    news_results=None

    if get_news_response['articles']:
      news_results_list=get_news_response['articles']
      news_results=process_news_results(news_results_list)
  return news_results

def process_news_results(news_list):
  '''
    Function that processes the news results and transforms them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
  news_results=[]
  for news_item in news_list:

    author=news_item.get('author')
    title=news_item.get('title')
    description=news_item.get('description')
    url=news_item.get('url')
    urlToImage=news_item.get('urlToImage')
    publishedAt=news_item.get('publishedAt')
    content=news_item.get('content')

    news_object=News(author,title,description,url,urlToImage,publishedAt,content)
    news_results.append(news_object)

  return news_results

# sites
def get_sites():
  get_sites_url = sites_url.format(api_key)

  with urllib.request.urlopen(get_sites_url)as url:
    get_sites_data=url.read()
    get_sites_response=json.loads(get_sites_data)

    sites_results=None

    if get_sites_response['sources']:
      sites_results_list=get_sites_response['sources']
      sites_results=process_sites_results(sites_results_list)

  return sites_results

def process_sites_results(sites_list):
  '''
    Function  that processes the sites result and transform them to a list of Objects

    Args:
        sites_list: A list of dictionaries that contain sites details

    Returns :
        sites_results: A list of sites objects
    '''

  sites_results = []
  for sites_item in sites_list:
    id=sites_item.get('id')
    name=sites_item.get('name')
    description=sites_item.get('description')
    url=sites_item.get('url')
    category=sites_item.get('category')

    sites_object = Sites(id, name, description, url, category)
    sites_results.append(sites_object)

  return sites_results

# sources
def get_sources(source):
  get_sources_url = sources_url.format(source,api_key)

  with urllib.request.urlopen(get_sources_url)as url:
    get_sources_data=url.read()
    get_sources_response=json.loads(get_sources_data)

    sources_results=None

    if get_sources_response['articles']:
      sources_results_list=get_sources_response['articles']
      sources_results=process_sources_results(sources_results_list)
  return sources_results

def process_sources_results(sources_list):
  '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sites details

    Returns :
        sources_results: A list of sites objects
    '''
  print(sources_list)

  sources_results=[]
  for sources_item in sources_list:
    sources=sources_item.get('sources')
    author=sources_item.get('author')
    title=sources_item.get('title')
    description=sources_item.get('description')
    url=sources_item.get('url')
    urlToImage=sources_item.get('urlToImage')
    publishedAt=sources_item.get('publishedAt')
    content=sources_item.get('content')




    sources_object = Sources(sources,author,title,description,url,urlToImage,publishedAt,content)
    sources_results.append(sources_object)

  return sources_results

