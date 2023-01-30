from controller.enums import *


class SlackView:
    trigger_id: str
    view_id: str
    title: str
    callback_id: VIEW_CALL_BACK_ID
    blocks: list

    def __init__(self, trigger_id: str, callback_id: VIEW_CALL_BACK_ID, view_id: str = None):
        self.trigger_id = trigger_id
        self.callback_id = callback_id
        if view_id: self.view_id = view_id
        self.title = VIEW_TITLE(callback_id).value

    def set_blocks(self, blocks: list):
        self.blocks = blocks

    def body(self):
        body = {
            'trigger_id': self.trigger_id,
            'callback_id': self.callback_id,
            'view': {
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": self.title,
                    "emoji": True
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit",
                    "emoji": True
                },
                "close": {
                    "type": "plain_text",
                    "text": "Cancel",
                    "emoji": True
                },
                "blocks": self.blocks
            }
        }
        return body
