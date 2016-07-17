# coding: utf-8

'''
slack client wrapper

slack = MySlack(token)
'''

from slacker import Slacker

class MySlack(object):

    def __init__(self, token):
        self.client = Slacker(token)
        self._ids = None

    def history(self, channel):
        channel_id = self._get_channel_id(channel)
        history = self.client.channels.history(channel=channel_id, count=1000).body
        return [
            x["text"] for x in history["messages"]
            if (x.get("text") is not None) and (x.get("subtype") is None)
        ]

    def upload_file(self, channel, file_path):
        channel_id = self._get_channel_id(channel)
        self.client.files.upload(file_path, channels=channel_id)

    def _get_channel_id(self, name):
        if self._ids is None:
            ids = self.client.channels.list(exclude_archived=1).body
            self._ids = dict((x["name"], x["id"]) for x in ids["channels"])

        channel_id = self._ids.get(name.replace("#", ""))
        if channel_id is None:
            raise RuntimeError("%s is not found or eval_channel_id wasn't called" % name)
        return channel_id
