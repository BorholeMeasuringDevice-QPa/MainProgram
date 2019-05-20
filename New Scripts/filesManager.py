import os
import datetime
import sys


def createFolder(folderName):

    try:
        date = datetime.date.today()

        basePath = '/home/pi/Desktop/'+folderName+'/' + str(date)

        os.mkdir(basePath)

        os.mkdir(basePath+'/Videos')
        os.mkdir(basePath+'/Readings')

        return basePath

    except:
        print('Folder juz istnieje')
        sys.exit(1)


def createTxtFile(fileName, basePath):

    dtime = str(datetime.datetime.now())
    dtime = dtime.replace(':', '-')
    dtime = dtime.replace('.', '-')
    dtime = dtime.replace(' ', '-')

    newFile = open(basePath+'/Readings/'+fileName+"_"+str(dtime)+'.txt', 'w+')

    currentFileName = basePath+'/Readings/'+fileName+"_"+str(dtime)+'.txt'

    return currentFileName


def writeToTxtFile(content, myFile):
    myFile.write(content+'\n')
    return 0


def writeHeader(myFile, tag):
    dateTimeNow = str(datetime.datetime.now())
    myFile.write(str("Reading <"+tag+"> from: "+dateTimeNow)+"\n")

#createFolder('Archive')
#createTxtFile('testowy','Archive')
