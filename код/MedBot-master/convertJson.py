from striprtf.striprtf import rtf_to_text
import json


def convertSymptoms():
    aList=[]
    with open("SYMPTOMS.WIN") as infile:
        for line in infile:

            splitted_text = str(line).split()
            # print(splitted_text[0])
            # # del s
            # s={}
            # s[splitted_text[0]]=lin
            s={}
            s['id']=splitted_text[0]
            str1=""
            for i in range(1,len(splitted_text)):
                str1+=" " + splitted_text[i]
            s['q']=str1
            aList.append(s)
    jsonString = json.dumps(aList, ensure_ascii=False)
    jsonFile = open("que.json", "w", encoding="UTF-8")
    jsonFile.write(jsonString)
    jsonFile.close()
    
    
def convertHyp():
    aList=[]
    with open("HYPOTHES.WIN") as infile:
        s={}
        lineNum=0
        for line in infile:
            if (lineNum % 3)==0:
                s['descr']=line            
            if lineNum%3==1:
                splitted_text = str(line).split()
                s['vv']=splitted_text[0]
                # print(len(splitted_text))
                nList=[]
                for i in range(1,len(splitted_text)):
                    nList.append(splitted_text[i])
                # print(nList)
                nNum=0
                vv= pmax= pmin=0
                plist=[]
                for item in nList:
                    if (nNum % 3)==0 and nNum>0:
                        vv=item
                        plist.append([vv,pmax,pmin])
                    if (nNum % 3)==1:
                        pmax=item
                    if (nNum % 3)==2:
                        pmin=item
                    nNum+=1
                s['pList']=plist   
            if (lineNum % 3)==2:    
                aList.append(s)
                s={}
            lineNum+=1
            
    jsonString = json.dumps(aList, ensure_ascii=False)
    jsonFile = open("Hyp.json", "w", encoding="UTF-8")
    jsonFile.write(jsonString)
    jsonFile.close()
    

#  0.02      3 1.0 0.01 
def proc(ans, vv, pmax, pmin):
    up = up = ((2 * pmax - 1) * ans / 100 + 1 - pmax) * vv;
    down = ((2 * pmax - 1) * ans / 100 + 1 - pmax) * vv + ((2 * pmin - 1) * ans / 100 + 1 - pmin) * (1 - vv)
    if down!=0:
        vv=up/down
    return (vv, up, down)
    



if __name__ == '__main__':
    # fileObject = open("data2.json", "r", encoding="UTF-8")
    # jsonContent = fileObject.read()
    # aList = json.loads(jsonContent)
    # jsonString = json.dumps(nList, ensure_ascii=False)
    # jsonFile = open("data3.json", "w", encoding="UTF-8")
    # jsonFile.write(jsonString)
    # jsonFile.close()
    # a=getRft(11)
    # print(a)
    convertSymptoms()
    convertHyp()
