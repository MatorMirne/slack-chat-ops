from secret import Token
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=Token.SLACK_APP_TOKEN)

@app.command("/chatops")
def handle_some_command(ack, body, logger):
    ack()
    logger.info(body)
    print(body)

if __name__ == "__main__":
    SocketModeHandler(app, Token.SLACK_APP_TOKEN).start()