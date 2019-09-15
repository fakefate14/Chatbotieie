import pprint
from flask import Flask , request

## from{ name of your file } import search
from Resource.wolf import search_wiki
Line_Access_Token = 'cjlnc6T11x4diTSuUFrWK2CKJ/Gh8X0vta/++gA3S7mr6/X+ofWm+Jywh3l/iaEtYdi46Sp2z9x0LbUhiIWBe0F+Oq0psi1nvZVXLmPMQ+0Ma3iluZB5boFoaF/PYh1+w8z1IaIeDywucA0sa9Tn6gdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':

        pp = pprint.PrettyPrinter(indent=3)
        ### dictionary from line
        data = request.json
        data_show = pp.pprint(data)

        ## extract text from line
        text_fromline = data['events'][0]['message']['text']
        ## ค้นหาคำจาก wikipedia
        result = search_wiki(text_fromline)

        ### import function ในการส่งmessage reply.py
        from reply import ReplyMessage

        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Acees_Token = Line_Access_Token
        )


        return 'OK'

    elif request.method == 'GET':
        return 'นี้คือลิงค์เว็บสำหรับรับ package'

if __name__ == "__main__":
    app.run(port=200)
