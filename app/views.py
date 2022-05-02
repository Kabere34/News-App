from flask import render_template
from app import app
from .request import get_news

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the NEWS page and its data
    '''
    news=get_news()


    return render_template('index.html',sources=news)

@app.route('/sources/<int:sources_id>')
def sources(sources_id):
    '''
    View sources page function that return the sources details page and its data
    '''
    title = f'You are viewing{sources_id}'
    return render_template('sources.html',title = title)




