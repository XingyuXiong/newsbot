from googletrans import Translator


def trans(translator,source,src='en',dest='zh-cn'):
    return translator.translate(source,src=src,dest=dest).text