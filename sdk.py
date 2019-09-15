import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *


# from linebot.models import (
    
#     MessageEvent, TextMessage, TextSendMessage,
# )


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable

channel_secret = '5e80705c8b91410f7f45de328ff69e89'
channel_access_token = 'cjlnc6T11x4diTSuUFrWK2CKJ/Gh8X0vta/++gA3S7mr6/X+ofWm+Jywh3l/iaEtYdi46Sp2z9x0LbUhiIWBe0F+Oq0psi1nvZVXLmPMQ+0Ma3iluZB5boFoaF/PYh1+w8z1IaIeDywucA0sa9Tn6gdB04t89/1O/w1cDnyilFU='

#### ไม่ได้ใช้ ใช้สำหรับพวก Production ####

# channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
# channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
# if channel_secret is None:
#     print('Specify LINE_CHANNEL_SECRET as environment variable.')
#     sys.exit(1)
# if channel_access_token is None:
#     print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
#     sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/webhook", methods=['POST'])
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
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):

    print (event.reply_token)
    print (event.message.text)

    Reply_token = event.reply_token
    Text_from_user = event.message.text

######## Original ###########
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text)
    # )

    
    # #Set ข้อความ ประเภท Text
    # Text_tosend_1 = TextSendMessage(text='Uncle Engineer_01',quick_reply=None)
    # Text_tosend_2 = TextSendMessage(text='Uncle Engineer_02',quick_reply=None)
    # Text_tosend_3 = TextSendMessage(text='Uncle Engineer_03',quick_reply=None)
    # Text_tosend_4 = TextSendMessage(text='Uncle Engineer_04',quick_reply=None)
    # Text_tosend_5 = TextSendMessage(text='Uncle Engineer_05',quick_reply=None)

    # # Texttosend = TextSendMessage(text='Uncle Engineer',quick_reply=None)

    # #Set ข้อความ ประเภท  Image 
    # image_message_1 = ImageSendMessage(
    #          original_content_url       ='https://www.khaosod.co.th/wp-content/uploads/2018/07/7-10.jpg'
    #         ,preview_image_url          ='https://www.khaosod.co.th/wp-content/uploads/2018/07/7-10.jpg')
    # image_message_2 = ImageSendMessage(
    #          original_content_url       ='https://i0.wp.com/news.phuketindex.com/wp-content/uploads/2009/12/boxing.jpg'
    #         ,preview_image_url          ='https://www.khaosod.co.th/wp-content/uploads/2019/07/aptopix_pacquiao_thurman_boxing.jpg')


    # line_bot_api.reply_message(
    #     Reply_token,
    #     messages = [Text_tosend_1,Text_tosend_2,Text_tosend_3,image_message_1,image_message_2]
    # )

    ## ตัวอย่าง Push Message ## ทำพร้อม Replay ไม่ได้ 
    # line_bot_api.push_message(
    #     to ='User ID'
    #     messages = [Text_tosend_1,Text_tosend_2,Text_tosend_3,image_message_1,image_message_2]
    # )

    if Text_from_user == 'AX':

        from Resource.bxAPI import GetBxPrice
        Bxprice = GetBxPrice()
        print(Bxprice)

        Text_tosend_1 = TextSendMessage(text=str(Bxprice),quick_reply=None)

        line_bot_api.reply_message(
            Reply_token,
            messages = [Text_tosend_1]
        )
    
    ### FLEX ###
    if Text_from_user == 'BX':

        from Resource.bxAPI import GetBxPrice
        from random import randint 
        randomnum =randint(1,10)
        Bxdata = GetBxPrice(Number_to_get=randomnum)

        from Resource.FlexMessage import setbubble , setCarousel

        flexdata = setCarousel(Bxdata)

        from Resource.reply import SetMenuMessage_Object , send_flex

        flex = SetMenuMessage_Object(flexdata)
        send_flex(reply_token=Reply_token,file_data=flex,bot_access_key=channel_access_token)
        print(flex)

    else :
        text_list = [
            'ไม่เข้าใจอ่ะ','อีหยังวะ','พูดใหม่ๆๆๆ','อะไรว้า'
        ]
        from random import choice
        textdata = choice(text_list)
        Text_tosend_1 = TextSendMessage(text=textdata,quick_reply=None)

        line_bot_api.reply_message(
            Reply_token,
            messages = [Text_tosend_1]
        )    


#richmenu-7fa3d3463f121fb55d0d50e739a26975
@handler.add(FollowEvent)
def RegisRichmenu(event):

    # Reply_token = event.reply_token
    userid = event.source.user_id
    displayname = line_bot_api.get_profile(user_id=userid)

    button_1 = QuickReplyButton(action=MessageAction(label='AX',text='AX'))
    button_2 = QuickReplyButton(action=MessageAction(label='BX',text='BX'))
    quickbutton = QuickReply(items=[button_1,button_2])


    text1 = TextSendMessage(text=f'Hi Hello {displayname.display_name}')
    text2 = TextSendMessage(text=f'กรุณาเลือกเมนูที่ท่านต้องการค่ระบ',quick_reply=quickbutton)
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-7fa3d3463f121fb55d0d50e739a26975')

    line_bot_api.reply_message(
        Reply_token,
        messages = [text1,text2]
    )     



if __name__ == "__main__":
    app.run(port = 200)