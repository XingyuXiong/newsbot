from newsapi import NewsApiClient
from tools import get_from_dict

max_return_num=2


api_key='793110ecda064a68846a1510d0e7d0ae'
newsapi=NewsApiClient(api_key=api_key)


search_param={'keyword':'q','sources':'sources','domain':'domains'}
def read(search_type,addition):
    articles=None
    articles=eval('newsapi.get_everything({0}="{1}")'.format(search_param[search_type],addition))

    articles=articles['articles'][:max_return_num]
    #print(articles)
    titles=get_from_dict(articles,'title')
    #print(titles)
    return titles


sort_param={'popular':'top','similar':'relevancy','date_sort':'publishedAt'}
def sort(search_type,search_addition,sort_type,addition):
    articles=None
    if sort_type=='date_sort' and addition:
        articles=eval('newsapi.get_everything({0}="{1}",sort_by="{2}",from_param="{3}")'
            .format(search_param[search_type],search_addition,sort_param[sort_type],addition))
    if sort_type in sort_param:
        articles=eval('newsapi.get_everything({0}="{1}",sort_by="{2}")'
            .format(search_param[search_type],search_addition,sort_param[sort_type]))
    articles=articles['articles'][:max_return_num]
    titles=get_from_dict(articles,'title')
    return titles


def read_with_keyword():
    pass


if __name__=='__main__':
    print(read('keyword','france'))
    print(sort('keyword','france','date_sort','2019-11-23'))