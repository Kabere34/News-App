from flask import render_template
from app import app

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message="a news app on"
    return render_template('index.html',message=message)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that return the news details page and its data
    '''
    return render_template('news.html',id=news_id)

def index():
  '''
  View root page fuction that returns the index page and its data
  '''
  title='Home-Welcome to the Best Preview Website'
  return render_template('index.html',title = title)

def news():
  '''
   View root page function that returns the news page and its data
  '''
  title = 'News- A moview Site'
  return render_template('news.html', title = title)
