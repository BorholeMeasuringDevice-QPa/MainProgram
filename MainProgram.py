#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program do wczytywania i obsługi danych z Arduino

import datetime
import DataAdjustment as DA



#funkcja czekająca na sygnał z enkodera
def trigger():
    Trigger=False
    return Trigger






# funkcja odczytująca dane z Arduino
def data_reader():
    return True

# funckja formatująca dane na typy obsługiwane przez program
def data_converter():
    return True

#funkcja tworząca nowy plik
def create_a_file():
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    file_name="file_"+date+".txt"
    file = open(file_name,"w+")
    file.write("Zapis z: "+date+"\n")
    e=0
    return file;

#funkcja zapisująca dane do pliku
def write_to_file(data,file):
    e=0
    Key_list = ["magnetometr_x", "magnetometr_y", "magnetometr_z", "akcelerometr_x", "akcelerometr_y",
                "akcelerometr_z", "barometr_t", "barometr_p", "barometr_h", "enkoder_m"]
    while e < len(data):
        file.write(str(data[Key_list[e]]) + " | ")
        e += 1
    file.write("\n")
    return 0;

#funckja wyświetlająca dane
def data_viewer():
    return True

def main(args):
    #print("Wartości uśrednione dla 10 pomiarów: ")
     file=create_a_file()
     data1= DA.data_final_result()
     data2 = DA.data_final_result()
     data3 = DA.data_final_result()
     write_to_file(data1,file)
     write_to_file(data2,file)
     write_to_file(data3,file)
    #print(data_final_result())
     return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


