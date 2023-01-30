from controller.tools.logger.log import logger

def slack_observer(data):
    logger.info(data)

    if data['text'] != '':
        logger.info("커맨드 입력")
        command = data['text']
        if command in