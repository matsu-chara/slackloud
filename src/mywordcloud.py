# coding: utf-8

'''
word cloud wrapper

word_cloud = MyWordCloud()
'''

from wordcloud import WordCloud
from matplotlib import pyplot as plt

class MyWordCloud(object):

    def __init__(self, stop_words, font_path="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"):
        self.stop_words = stop_words
        self.word_cloud = WordCloud(
            background_color="white", font_path=font_path, width=900, height=900,
            stopwords=set(self.stop_words)
        )

    def generate(self, text, dest_path):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.word_cloud.generate(text))
        plt.axis("off")
        plt.savefig(dest_path, bbox_inches="tight", pad_inches=0.0)
