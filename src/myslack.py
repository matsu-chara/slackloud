# coding: utf-8

'''
slack client wrapper
this clss require extra initialize method call

slack = MySlack(token)
slack.eval_channel_id()
'''

from slacker import Slacker

class MySlack(object):

    def __init__(self, token):
        self.client = Slacker(token)
        self.ids = None

    def eval_channel_id(self):
        ids = self.client.channels.list(exclude_archived=1).body
        self.ids = dict((x["name"], x["id"]) for x in ids["channels"])

    def history(self, channel):
        channel_id = self._get_channel_id(channel)
        history = self.client.channels.history(channel=channel_id, count=1000).body
        return [x["text"] for x in history["messages"] if x["text"] is not None]

    def upload_file(self, channel, file_path):
        channel_id = self._get_channel_id(channel)
        self.client.files.upload(file_path, channels=channel_id)

    def _get_channel_id(self, name):
        channel_id = self.ids[name.replace("#", "")]
        if channel_id is None:
            raise RuntimeError("%s is not found or eval_channel_id wasn't called" % name)
        return channel_id
