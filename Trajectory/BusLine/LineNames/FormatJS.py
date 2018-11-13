import json

def splitLines(fileName,outFile):
    f_in = open(fileName,'r',encoding='utf-8')
    f_out=  open(outFile,'w',encoding='utf-8')
    
    lines = f_in.readlines()
    station = [line.strip('\n') for line in lines]

    json.dump(station,f_out,ensure_ascii=False,indent=4)
    f_in.close()
    f_out.close()
        

if __name__ == "__main__":
    fileName = "C:\\Users\\scott\\Desktop\\StationLines.csv"
    outFile = "C:\\Users\\scott\\Desktop\\StationLinesJS.js"
    splitLines(fileName,outFile)