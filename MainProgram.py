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
def data_averaging():
    return True

#funckja wyświetlająca dane
def data_viewer():
    return True

def main(args):
    save_to_file("TESTOWY NAPIS")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


