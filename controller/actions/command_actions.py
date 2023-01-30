from model.slack_view import *
from view.slack_blocks import *
from main import app

def help(received_body):

    def parser(received_body):
        trigger_id = received_body['trigger_id']
        callback_id = received_body['callback_id']
        return trigger_id, callback_id


    trigger_id, callback_id = parser(received_body)

    view = SlackView(trigger_id=trigger_id, callback_id=callback_id)
    blocks = [help_block()]
    view.set_blocks(blocks)
    body = view.body()

    app.client.views_open(trigger_id=trigger_id, view=body['view'])


