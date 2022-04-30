from flask import render_template
from app import app

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title='Home-Welcome to the Best News Preview Website'
    return render_template('index.html',title = title)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that return the news details page and its data
    '''
    title = f'You are viewing{news_id}'
    return render_template('news.html',title = title)




