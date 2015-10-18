import os, sys, re

def main(argv):
    for files in os.listdir(argv[0]):
        newname = files.replace(" ", "")
        newname = re.sub(r"\d+", "", newname)
        #newname = newname.replace("-", "")
        newname = newname[2:]
        #print(newname)
        os.rename(argv[0] + "/" +files, argv[0] + "/" + newname)
main(sys.argv[1:])