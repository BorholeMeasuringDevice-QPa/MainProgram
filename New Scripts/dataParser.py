import sys


def splitter(input):
        try:
                strInput = str(input)
                splitted = strInput.split(';')
                del splitted[0]
                del splitted[-1]
                del splitted[-1]
                return splitted
        except:
                return ['0','0','0','0','0','0','0','0','0']


def readValues(values, n):

        sumTable = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for table in values:
                i = 0
                for e in table:
                        sumTable[i] += int(int(e.strip())/n)
                        i += 1
        return sumTable
