# coding: utf-8

'''
mecab wrapper

mecab = MyMeCab()
'''

import MeCab

class MyMeCab(object):

    def __init__(self, dict_path="/usr/lib/mecab/dic/mecab-ipadic-neologd/"):
        args = "-Ochasen"
        if dict_path != "":
            args += " -d %s" % dict_path

        self.tagger = MeCab.Tagger(args)
        self.tagger.parse('')  # suppress UnicodeDecodeError

    # ref: http://qiita.com/kenmatsu4/items/9b6ac74f831443d29074
    # text: str (not bytes)
    def parse(self, text):
        node = self.tagger.parseToNode(text)
        output = []
        while node:
            if node.surface != "":  # remove header and footer
                word_type = node.feature.split(",")[0]
                if word_type in ["動詞", "名詞"]:
                    output.append(node.surface)
            node = node.next
            if node is None:
                break
        return output
