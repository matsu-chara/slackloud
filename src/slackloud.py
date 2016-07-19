#!/usr/bin/env python3
# coding: utf-8

'''
- fetch slack history
- generate wordcloud
- post to channel
'''

import sys
import words
from myslack import MySlack
from mymecab import MyMeCab
from mywordcloud import MyWordCloud

# (return token, channel, post_channel)
def parse_arg(argv):
    if len(argv) < 3:
        print("Usage: # python %s token channel" % argv[0])
        quit()

    return (argv[1], argv[2], argv[3] if (len(argv) == 4) else "")

def main():
    token, channel, post_channel = parse_arg(sys.argv)

    slack = MySlack(token)

    history = slack.history(channel)
    processed_history = words.remove_before_mecab(words.unescape(history))

    mecab = MyMeCab()
    mecab.build_user_dic()
    analyzed = mecab.parse(" ".join(processed_history))
    processed_analyzed = words.remove_after_mecab(analyzed)

    word_cloud = MyWordCloud(words.read_stopwords())
    word_cloud_file_path = "/app/result/wordcloud.png"
    word_cloud.generate(" ".join(processed_analyzed), word_cloud_file_path)

    if post_channel != "":
        slack.upload_file(post_channel, word_cloud_file_path)

if __name__ == '__main__':
    main()
