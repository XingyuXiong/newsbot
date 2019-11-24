from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='793110ecda064a68846a1510d0e7d0ae')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()

countries = {'ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr','hk',
             'hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz','ph','pl',
             'pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us','ve','za'}

languages = {'ar','en','cn','de','es','fr','he','it','nl','no','pt','ru','sv','ud'}

categories = {'business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology'}

sort_method = {'relevancy','popularity','publishedAt'}
