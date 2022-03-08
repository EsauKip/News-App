from app import app
import urllib.request,json
from .models import article
Article = article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
base_article_url = app.config["ARTICLES_API_BASE_URL"]

def get_sources(source):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results
def getting_articles(id):
    getting_article_url = base_article_url.format(id,api_key)
    with urllib.request.urlopen(getting_article_url) as url:
        article_news_data = url.read()
        article_news_response = json.loads(article_news_data)

        article_news_results = None
      

        if article_news_response['articles']:
            article_news_list = article_news_response['articles']
            article_news_results = process_articles(article_news_list)


    return article_news_results