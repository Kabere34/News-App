from flask import render_template
from app import app
from .request import get_news,get_sites,get_sources


#Views
@app.route('/')
def index():

    '''
    View root page function that returns the NEWS page and its data
    '''

    bridges=get_sites()


    return render_template('index.html',bridges=bridges)

@app.route('/sources/<source>')
def sources(source):
    '''
    View sources page function that return the sources details page and its data
    '''

    platforms=get_sources(source)

    return render_template('sources.html',platforms=platforms)


@app.route('/headlines')
def headlines():
    '''
    View sources page function that return the sources details page and its data
    '''
    news=get_news()

    return render_template('headlines.html',news=news)
