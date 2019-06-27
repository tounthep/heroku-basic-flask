import json
import requests
from flask import Flask, request, abort

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
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

line_channel_access_token = 'eP7aREyHj2iX/OnEgScz7L9sxkD6AEbcVbngnyyo1XHA//uDDFCXuQn1ZPxZ2Rrsi31xBcSmr2PCwmWNxZYAnV9CvrUmVnJVjMO0mNgN57t9xxP7zPBAx4s269q0w3/KiCiggHP4wo0JgqWmf7S9GwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(line_channel_access_token)
Authorization = "Bearer {}".format(line_channel_access_token)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    body = json.loads(body)
    print (body)

    reply_token = body['events'][0]["replyToken"]
    print("reply_token: {}".format(reply_token))

    event_type = body['events'][0]['type']
    print("event_type: {}".format(event_type))

    if event_type == "message":
        message_type = body['events'][0]['message']['type']
        # print("message_type: {}".format(message_type))
        if message_type == "text":
            text = body['events'][0]['message']['text']
            print("text: {}".format(text))
            if "home" in text or "Home" in text:
                print("replying text:{}".format(text))
                reply_menu(reply_token)

    return '',200

def reply_menu(reply_token):
    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": [{
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://www.sentangsedtee.com/wp-content/uploads/2018/05/cute-dog-shiba-inu-ryuji-japan-17.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
          }
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "เลือกผมสิฮับ",
                "uri": "https://linecorp.com"
              },
              "color": "#905C44",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://i3.wp.com/www.catdumb.com/wp-content/uploads/2016/01/3297.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
          }
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Add to Cart",
                "uri": "https://linecorp.com"
              },
              "color": "#905C44",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://fongfai.files.wordpress.com/2012/07/chihuahua_dog_a_001.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
          }
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Add to Cart",
                "uri": "https://linecorp.com"
              },
              "color": "#905C44",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://108dog.com/market/board/attachments/1652093_95c67471aa53896c967a33d7b5ddf6ae160758cd",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
          }
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Add to Cart",
                "uri": "https://linecorp.com"
              },
              "color": "#905C44",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://www.dogsclip.com/img/upload/03PhotoAlbums/Albums/ShareImg/dsc_albumShareImg5929571495220925.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
          }
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "spacer",
              "size": "xxl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Add to Cart",
                "uri": "https://linecorp.com"
              },
              "color": "#905C44",
              "style": "primary"
            }
          ]
        }
      }
    ]
  }
}]
        })
    )

if __name__ == "__main__":
    app.run()
