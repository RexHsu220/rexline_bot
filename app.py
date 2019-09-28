from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('SPtN2nC5c7BS9z4yTMUuGsNNou8S6hi0+MMYAPqG5H+pAxl7zMoWyO4eu1I+omPknqKQz1Tq5cOef6NXqmxBUV6ULokEwLwTLqYB8rJpJwxkISSBlFjaKwxSk/0Rva2GbSyGTDlh+z2cuy9bkOFjTgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8887b8963cb9fea56054ebb573471e95')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    str1 = 'Have you eaten before?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = str1))


if __name__ == "__main__":
    app.run()