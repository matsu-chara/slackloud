# coding: utf-8

'''
mecab wrapper

mecab = MyMeCab()
'''

import MeCab
import glob
import os
import subprocess

class MyMeCab(object):

    def __init__(self,
                 dic_path="/usr/lib/mecab/dic/mecab-ipadic-neologd/",
                 user_dic_path="/app/dic/"):
        self.dic_path = dic_path
        self.user_dic_path = user_dic_path

    def build_user_dic(self):
        if self.user_dic_path == "":
            return

        files = self._remove_ext(self._files(self.user_dic_path, "csv"))
        for f in files:
            target = f + ".csv"
            dest = f + ".dic"
            command_template = "/usr/lib/mecab/mecab-dict-index -d %s -u %s -f utf-8 -t utf-8 %s"
            command = command_template % (self.dic_path, dest, target)
            dev_null = open(os.devnull, 'w')
            subprocess.call(command.split(" "), stdout=dev_null)

    # ref: http://qiita.com/kenmatsu4/items/9b6ac74f831443d29074
    # text: str (not bytes)
    def parse(self, text):
        tagger = MeCab.Tagger(self._mecab_args())
        tagger.parse('')  # suppress UnicodeDecodeError
        node = tagger.parseToNode(text)
        output = []
        while node:
            if node.surface != "":  # remove header and footer
                word_type = node.feature.split(",")[0]
                if word_type in ["名詞"]:
                    output.append(node.surface)
            node = node.next
            if node is None:
                break
        return output

    def _mecab_args(self):
        args = "-Ochasen"
        if self.dic_path != "":
            args += " -d %s" % self.dic_path

        if self.user_dic_path != "":
            args += " -u "
            dics = self._files(self.user_dic_path, "dic")
            args += ",".join(dics)

        return args

    # return fullpath
    def _files(self, path, ext):
        return  [x for x in glob.glob(path + "/*." + ext)]

    def _remove_ext(self, files):
        return [os.path.splitext(x)[0] for x in files]
