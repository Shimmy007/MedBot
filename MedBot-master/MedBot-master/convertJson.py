from striprtf.striprtf import rtf_to_text
import json


def convertSymptoms():
    aList=[]
    with open("SYMPTOMS.WIN") as infile:
        for line in infile:
            # print(splitted_text[0])
            # splitted_text = str(line).split()
            # print(splitted_text[0])
            # # del s
            # s={}
            # s[splitted_text[0]]=line
            aList.append(line)
    jsonString = json.dumps(aList, ensure_ascii=False)
    jsonFile = open("Symptoms.json", "w", encoding="UTF-8")
    jsonFile.write(jsonString)
    jsonFile.close()
    
    
def convertSymptoms():
    aList=[]
    with open("HYPOTHES.WIN") as infile:
        for line in infile:
            # print(splitted_text[0])
            # splitted_text = str(line).split()
            # print(splitted_text[0])
            # # del s
            # s={}
            # s[splitted_text[0]]=line
            aList.append(line)
    # jsonString = json.dumps(aList, ensure_ascii=False)
    # jsonFile = open("desc.json", "w", encoding="UTF-8")
    # jsonFile.write(jsonString)
    # jsonFile.close()
        
    # print(text)
    
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
