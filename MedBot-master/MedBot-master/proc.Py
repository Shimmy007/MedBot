from striprtf.striprtf import rtf_to_text
import json


def getRft(id):
    fileName= "./descript/"+str(id)+".rtf"
    with open(fileName) as infile:
        content = infile.read()
        text = rtf_to_text(content)
        return(text)
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
    
    fileObject = open("Symptoms.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    for item in aList:
        print(item)
        splitted_text = str(item).split()
        print(splitted_text[0])
        ans=input()
        pmax=1.0
        pmin = 0.01
        vv=0.02
        (vv, up, down)=proc(ans, vv, pmax, pmin)
    
    (vv, up, down)=proc(ans, vv, pmax, pmin)
    print(vv)
    print(down)
    print(up)
    
    
    