from newsapi import NewsApiClient

max_return_num=2


api_key='793110ecda064a68846a1510d0e7d0ae'
newsapi=NewsApiClient(api_key=api_key)

def read(search_type,addition):
    if search_type=='keyword':
        articles=newsapi.get_everything(q=addition)[:max_return_num]


def sort():
    pass


def read_with_keyword():
    pass


if __name__=='__main__':
    print(read('keyword','france'))