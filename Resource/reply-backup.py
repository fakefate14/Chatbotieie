import json
import requests


def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) 
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = { ### Class = Dict
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        },{
            "type":"text",
            "text":'ท่านสามารถใช้งานโดยการพิมพ์ประโยคที่ต้องการค้นหาค่ะ'
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object Class = Str
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 'OK'