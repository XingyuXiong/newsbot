# utf-8
import pickle
import os
import sys
import time
import json
from googletrans import Translator
if __package__:
    from scripts.filename import spacy_model_name,work_dir
    from scripts.respond import start,respond
else:
    from filename import spacy_model_name,work_dir
    from respond import start,respond


RUNNING=True


def read_write_file(file,object=None):
    if os.path.exists(file):
        with open(file,'rb') as f:
            return pickle.load(f)
    else:
        with open(file,'wb') as f:
            pickle.dump(object,f)
            return object

'test'
'''
translator=Translator(service_urls=['translate.google.cn'])
source='你好'#can not be none
text=trans(translator,source)
print(text)
'''
'''
load_start=time.time()
nlp=None
if not os.path.exists(spacy_model_name):
    nlp=spacy.load('en_core_web_md')
nlp=read_write_file(spacy_model_name,nlp)
load_end=time.time()
print('loading model spends {0}s'.format(load_end-load_start))
'''
def receive():
    pass


def send(message):
    pass


def receive_respond(message,state,search_sequence):
    answer,state,search_sequence=respond(message,state,search_sequence)
    return answer,state,search_sequence


if __name__=='__main__':
    pass