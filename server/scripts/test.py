from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='793110ecda064a68846a1510d0e7d0ae')
all_articles = newsapi.get_everything(q='bitcoin',
                                      sort_by='relevancy',)
print(all_articles)