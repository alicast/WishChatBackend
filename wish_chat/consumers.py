from channels.consumer import SyncConsumer


class wish_chatConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        pass