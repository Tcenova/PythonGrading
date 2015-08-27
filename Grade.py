__author__ = 'Thomas Cenova'

"""
Grade.py

Author: Thomas Cenova

"""

#import shutil
import sys
import os

def getFolderContents(path):
    return os.listdir(path)

def runPythonScript(folder, name):
    os.system(os.getcwd() + "/" + folder + "/" + name)

def main(argv):
    path = argv[0]
    #print(getFolderContents(path))

    #print(os.getcwd())
    #os.system(os.getcwd() + "/" + argv + "/" + getFolderContents(argv)[1])
    files = getFolderContents(path)
    fileNumber = 0;
    while (fileNumber<len(files)+1):
        goodCMD = False
        while (goodCMD == False):
            if fileNumber<len(files):
                print("Currently at file # : " + str(fileNumber))
            else:
                print("End of files")
            entered = input("Please enter command or hit enter to continue\n>>>")
            cmdList = entered.split()
            #print(cmdList)
            if (fileNumber>len(files)-1):
                return
            if cmdList == [] or cmdList[0] == "GO":
                #fileNumber += 1
                goodCMD = True
            elif cmdList[0] == "GOTO":
                try:
                    fileNumber = int(cmdList[1])
                    print("Going to " + cmdList[1])
                    #goodCMD = False
                except:
                    print ("Usage: GOTO filenumber")
            elif cmdList[0] == "BACK":
                if fileNumber > 0:
                    fileNumber -= 1
                    #goodCMD = False
                else:
                    print("Cannot go back")
            elif cmdList[0] == "STOP":
                return
            print(str(fileNumber) + "    " + str(goodCMD))


        print("Running :" + files[fileNumber])
        runPythonScript(path, files[fileNumber])
        fileNumber += 1



if __name__ == '__main__':
    main(sys.argv[1:])

