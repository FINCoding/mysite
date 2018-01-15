import json
from channels.channel import Group
def ws_connect(message):
    Group('chat').add(message.reply_channel)
    message.reply_channel.send({"accept": True})
def ws_message(message):
    Group('chat').send({'text': json.dumps({'message': message.content['text'],
                                            'sender': message.reply_channel.name})})
def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)