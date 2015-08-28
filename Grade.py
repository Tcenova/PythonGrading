"""
File: Grade.py

Author: Thomas Cenova

Description:


"""


import sys
import os

"""
:param path

"""
def getFolderContents(path):
    return os.listdir(path)

"""

"""
def runPythonScript(folder, name):
    command = "python \"" + os.getcwd() + "\\" + folder + "\\" + name + "\""
    os.system(command)

"""
"""
def howToUse():
    print("Commands are:                                            \n"
          "             STOP - stops program                        \n"
          "             GOTO fileNumber - goes to that file number  \n"
          "             BACK - goes to last file run                \n")

"""

"""
def main(argv):
    if len(argv) > 1:
        print("Usage: Grade.py folderName")
        return

    howToUse()

    path = argv[0]
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
            if cmdList == []:
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


#run main only if run directly
if __name__ == '__main__':
    main(sys.argv[1:])

