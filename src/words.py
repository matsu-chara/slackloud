# coding: utf-8

'''
remove words
'''

import re
import html

# remove words before mecab analyze
def remove_before_mecab(texts):
    # links, codes and emojis
    regex = re.compile(r"(<.*>|```.*```|`.*`|:.*:)")
    return [regex.sub('', x) for x in texts]

# remove words after mecab analyze
def remove_after_mecab(texts):
    regex = re.compile(r"[ぁ-ん]{0,2}")
    return [regex.sub('', x) for x in texts]

# this words will pass to WordCloud instance
def read_stopwords():
    return [
        u'ちゃん', u'みたい', u'感じ', u'思い', u'場合',
        u'すぎる', u'ところ', u'くれる', u'くださる', u'the', u'it',
        u'to', u'is', u'channel', u'joined'
    ]

def unescape(texts):
    return [html.unescape(x) for x in texts]
