"""
File: Grade.py

Author: Thomas Cenova

Description:
Simple script to successively go through each python script in a folder
Must be run with folder to look in in same directory


"""


import sys
import os

"""
Function to return a list of folder contents
:param path string of path to folder
:return list of strings of the files in the folder
"""
def getFolderContents(path):
    return os.listdir(path)

"""
Function to run a python script from within this script
NOTE: assumes you can run a python script by calling the file itself
"""
def runPythonScript(folder, name):
    command = "\"" + os.getcwd() + "\\" + folder + "\\" + name + "\""
    if sys.platform != "win32":
        command = "python3 " + command
    os.system(command)

"""
Function that prints instructions on usage and commands
"""
def howToUse():
    print("Commands are:                                                      \n"
          "             STOP            - stops program                       \n"
          "             GOTO fileNumber - goes to that file number            \n"
          "             BACK            - goes to last file run               \n"
          "             LIST            - lists all files in folder             ")

def findLibPath():
    if sys.platform == "win32":
        for element in sys.path:
            if element[-3:] == "lib":
                return element
    else:
        return "idle3 "

"""

"""
def runInIDLE(folder, name, libPath):
    command = libPath + "\\idlelib\\idle " + "\"" + os.getcwd() + "\\" + folder + "\\" + name + "\""
    os.system(command)

"""

"""
def main(argv):
    if len(argv) > 1:
        print("Usage: Grade.py folderName")
        return

    howToUse()

    libPath = findLibPath()
    #print(str(sys.path) + "  HAHA")

    path = argv[0]
    files = getFolderContents(path)
    fileNumber = 0;
    while (fileNumber<len(files)+1):
        goodCMD = False
        while (goodCMD == False):
            if fileNumber<len(files):
                print("Currently at file: \n" + "#: " + str(fileNumber) + "\tName: " + files[fileNumber])
            else:
                print("End of files")
            entered = input("Please enter command or hit enter to continue\n>>>")
            cmdList = entered.split()
            if (fileNumber>len(files)-1):
                return
            if cmdList == []:
                goodCMD = True
            elif cmdList[0] == "GOTO":
                try:
                    fileNumber = int(cmdList[1])
                    print("Going to " + cmdList[1])
                except:
                    print ("Usage: GOTO filenumber")
            elif cmdList[0] == "BACK":
                if fileNumber > 0:
                    fileNumber -= 1
                else:
                    print("Cannot go back")
            elif cmdList[0] == "STOP":
                return
            elif cmdList[0] == "LIST":
                print("Folder Contents:"
                      "#\tFilename")
                for x in range (0, len(files)-1):
                    print(str(x) + "\t" + files[x])

        print("Running :" + files[fileNumber])
        runInIDLE(path, files[fileNumber], libPath)
        input("Press ENTER to run program")
        runPythonScript(path, files[fileNumber])
        fileNumber += 1


#run main only if run file directly
if __name__ == '__main__':
    main(sys.argv[1:])

