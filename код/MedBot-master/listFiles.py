from striprtf.striprtf import rtf_to_text
import json
import os
dirname = './descript/'


def getRft(filename):
    fileName= dirname+filename
    with open(fileName) as infile:
        content = infile.read()
        text = rtf_to_text(content)
        return(text)
    # print(text)

def convertSym():
    files = os.listdir(dirname)
    # print(files)
    aList=[]    
    for file in files:
        rtf= getRft(file)
        # print(rtf)    
        splitted_text = str(rtf).split()
        s={}
        if splitted_text[1]=="Описание:":
            s['name']=splitted_text[0]
        else:
            s['name']=splitted_text[0]+' ' + splitted_text[1]
        s['file']=file
        s['id']=file.replace('.rtf','')
        aList.append(s)
    jsonString = json.dumps(aList, ensure_ascii=False)
    jsonFile = open("Sym.json", "w", encoding="UTF-8")
    jsonFile.write(jsonString)
    jsonFile.close()    
    
    

if __name__ == '__main__':
    convertSym()
    
    