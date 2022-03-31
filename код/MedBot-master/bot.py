from webbrowser import get
import telebot;

bot = telebot.TeleBot('5111904045:AAH8VIo6dXf1Uz-CddZ818PUOWXzoF0j6t8');

from striprtf.striprtf import rtf_to_text
import json

global qList
global qid
qList=[]
qid=0
global hList
hList=[]

def getQuest():
    global qid
    qid+=1
    global qList
    return qList[qid]['q'] 

def getRft(id):
    fileName= "./descript/"+str(id)+".rtf"
    with open(fileName) as infile:
        content = infile.read()
        text = rtf_to_text(content)
        return(text)
    # print(text)
    
#  0.02      3 1.0 0.01 
def proc(ans, vv, pmax, pmin):
    # print(vv, pmax, pmin)
    up =  ((2 * pmax - 1) * ans / 100 + 1 - pmax) * vv;
    down = ((2 * pmax - 1) * ans / 100 + 1 - pmax) * vv + ((2 * pmin - 1) * ans / 100 + 1 - pmin) * (1 - vv)
    if down!=0:
        vv=up/down
    return (vv, up, down)

def refresh(ans):
    global qid
    global hList
    nList=[]
    for item in hList:
        # print(item)
        vv = item['vv']
        pList = item['pList']
        if len(pList)>0:
            for p1 in pList:
                # print(p1)
                if p1[0]==str(qid):
                    pmax=float(p1[1])
                    pmin=float(p1[2])
                    (vv, up, down)=proc(ans, float(vv), pmax, pmin)
        item['vv']=vv
        nList.append(item)
    hList=nList
    
def drawDiag():
    global hList
    str1="Возможные диагнозы:"
    for item in hList:
        # print(item)
        vv = item['vv']
        if float(vv)>0.6:
            str1 += "\n" + item["descr"]
    if len(str1)>19:
        return str1
    return ""

def initData():
    global qList
    global hList
    fileObject = open("que.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    qList = json.loads(jsonContent)
    fileObject = open("Hyp.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    hList = json.loads(jsonContent)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    helpStr="Привет, это проект MedBot - Многофункциональный сервис для медицинской диагностики заболеваний. Внимание: при любом диагнозе необходима консультация врача! \n Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, helpStr)
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "MedBot - Многофункциональный сервис для медицинской диагностики заболеваний. Внимание: при любом диагнозе необходима консультация врача! \n Список команд: \n /q - ответить на следующий вопрос\n число от 0 до 100 в % насколько верно утверждение\n /n - Начать опрос (начать заново) \n /info получить информацию о диагнозе \n /i \"номер\" вывести информацию о диагнозе \n /about - О проекте \n ")
    elif str(message.text).lower() == "/q":
        bot.send_message(message.from_user.id, getQuest())
    elif str(message.text).lower() == "/n":
        initData()
        bot.send_message(message.from_user.id, getQuest())
    elif splitted_text[0] == "/i":
        bot.send_message(message.from_user.id, getRft(splitted_text[1]))
    elif str(message.text).lower() == "/about":
        with open("descr.txt", encoding="UTF-8") as infile:
            content = infile.read()
        bot.send_message(message.from_user.id, content)
    elif str(message.text).lower() == "/info":
        fileObject = open("Sym.json", "r", encoding="UTF-8")
        jsonContent = fileObject.read()
        symList = json.loads(jsonContent)
        str1="Список заболеваний:"
        for item in symList:
            str1+="\n"+item['id']+" "+ item['name']
        str1+="\n ввидите /i \"номер\" вывести информацию о диагнозе \n"
        bot.send_message(message.from_user.id, str1)
    elif isinstance(int(splitted_text[0]), int):
        ans=splitted_text[0]
        print(ans)
        refresh(float(ans))
        d=drawDiag()
        bot.send_message(message.from_user.id, d+"\n" + getQuest())
    else:
        bot.send_message(message.from_user.id, helpStr)

initData()
bot.polling(none_stop=True, interval=0)