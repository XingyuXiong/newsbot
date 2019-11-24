import pickle
import json
from filename import work_dir


try:
    from newsapi import NewsApiClient
except ImportError: 
    from newsapi.newsapi_client import NewsApiClient

global null
null=''

api_key='793110ecda064a68846a1510d0e7d0ae'
newsapi=NewsApiClient(api_key=api_key)

test_topics=['France']

def solve_code_error(input_dict):
    for key,value in input_dict.items():
        try:
            solve_code_error(value)
        except AttributeError:
            if isinstance(value,str):
                value=value 


class News():
    topic_stack={'France':1,'':'default information'}
    topic_content={}
    max_topic=10

    def __init__(self,topic_list=test_topics):
        pass


    def write_default_news(self):
        for topic in self.topic_stack:
            try:
                #print(json.dumps(newsapi.get_everything(q='France'),ensure_ascii=False))
                self.topic_content[topic]=newsapi.get_everything(q=topic)
            except RuntimeError:
                pass
            else:
                break
        with open(work_dir+'pickle_topic_content','wb') as file:
            pickle.dump(self.topic_content,file)


    def read_default_news(self):
        with open(work_dir+'pickle_topic_content','rb') as file:
            self.topic_content=pickle.load(file)


    def add_topic(self,new_topics_list):
        print(new_topics_list)
        new_topics={}
        for topic in new_topics_list:
            new_topics[topic]=newsapi.get_everything(q=topic)
        for new_topic_name in new_topics:
            if len(self.topic_content)>self.max_topic:
                self._forget_topic()
            self.topic_stack[new_topic_name]=new_topics[new_topic_name]
        print(self.topic_stack)


    def _forget_topic(self):
        pass


    def read_news(self,topic=''):
        read_response=self.topic_content['France']
        if topic in self.topic_content.keys():
            read_response=self.topic_content[topic]
        return read_response['articles']


if __name__=='__main__':
    #only for testing
    news=News()
    news.write_default_news()
    news.read_default_news()
    news.add_topic(new_topics_list=test_topics)
    print(news.read_news('France')['articles'])                