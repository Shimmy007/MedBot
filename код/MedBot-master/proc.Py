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
        if float(vv)>0.9:
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
    
if __name__ == '__main__':

    initData()
    
    for i in range(30):
        q=getQuest()
        print(q)
        ans=90
        refresh(ans)
        d=drawDiag()
        print(d)
