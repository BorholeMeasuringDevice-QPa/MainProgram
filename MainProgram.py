#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program do wczytywania i obsługi danych z Arduino

import datetime

# funkcja odczytująca dane z Arduino
def data_reader():
    return True

# funckja formatująca dane na typy obsługiwane przez program
def data_converter():
    return True

#funkcja zapisująca odczyty do pliku
def save_to_file(data):
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    file_name="file_"+date+".txt"
    file = open(file_name,"w+")
    file.write("Zapis danych z: "+date+"\n\n")
    i=0
    while(i<20):
        file.write(data+" nr "+str(i)+"\n")
        i+=1
    file.close()
    print("Done")
    return 0;

#funkcja uśredniająca dane
def data_averaging(data):
    sum=0
    for e in data:
        sum+=e
    average=round(sum/len(data),5)
    return average

#funckja wyświetlająca dane
def data_viewer():
    return True

def main(args):

    data=[2.35,2.47,3.01,2.5,2.7,3.0,2.12]
    save_to_file("TESTOWY NAPIS")
    print(data_averaging(data))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


