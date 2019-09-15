RichData = {
  "size": {
    "width": 2500,
    "height": 843
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": "เมนูหลัก",
  "areas": [
    {
      "bounds": {
        "x": 34,
        "y": 34,
        "width": 758,
        "height": 784
      },
      "action": {
        "type": "message",
        "text": "BX"
      }
    },
    {
      "bounds": {
        "x": 864,
        "y": 30,
        "width": 750,
        "height": 792
      },
      "action": {
        "type": "message",
        "text": "NEWS"
      }
    },
    {
      "bounds": {
        "x": 1703,
        "y": 34,
        "width": 759,
        "height": 780
      },
      "action": {
        "type": "postback",
        "text": "",
        "data": "QA"
      }
    }
  ]
}

import json
import requests
from sdk import channel_access_token

#ไม่ต้องเปลี่ยนอะไร จะได้ Richmenu iD ออกมา
def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):

    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())



CreateRichMenu(ImageFilePath='Resource\Slide1.jpg',Rich_json=RichData,channel_access_token=channel_access_token)

