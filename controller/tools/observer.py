from controller.tools.logger.log import logger
from controller.action import *

def slack_observer(received_body):
    logger.info(received_body)

    if received_body['text'] != '':
        logger.info("커맨드 입력")
        command = received_body['text']
        if command in COMMAND_ACTION:
            COMMAND_ACTION[command](received_body)