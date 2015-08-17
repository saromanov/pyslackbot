from slacker import Slacker
from slackclient import SlackClient
import time

class PySlackbot:
    def __init__(self, token):
        self.slack = Slacker(token)
        self.slackrtm = SlackClient(token)
        self.events = {}

    def search_and_send(self, search, send):
        channel = []
        result = self.slack.search.messages(search)
        for match in result.body['messages']['matches']:
            channel.append(match['channel'])
        print(channel)

    def send_message(self, text):
        self.events['message'] = send_message_inner

    def registerEvent(typename, func):
        self.events[typename] = func

    def start(self):
        if self.slackrtm.rtm_connect():
            while True:
                resp = self.slackrtm.rtm_read()
                if resp['type'] in self.events:
                    self.events[resp['type']](resp)


## Common methods

def send_message_inner(resp, client, text):
    channel = resp['channel']
    client.chat.post_message(channel, text)

def upload_file_inner(resp, client, path):
    channel = resp['channel']
    client.files.upload(path)

