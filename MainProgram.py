#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Program do wczytywania i obsługi danych z Arduino

import datetime
import random

#generator losowych danych
def raw_data_generator():
    raw_data={
    "magnetometr_x":random.uniform(30.0,40.0),
    "magnetometr_y":random.uniform(20.0,30.0),
    "magnetometr_z":random.uniform(10.0,20.0),
    "akcelerometr_x":random.uniform(40.0,50.0),
    "akcelerometr_y":random.uniform(50.0,60.0),
    "akcelerometr_z":random.uniform(60.0,70.0),
    "barometr_t":random.uniform(20.0,30.0),
    "barometr_p":random.uniform(1000.0,1100.0),
    "barometr_h":random.uniform(100.0,101.0),
    "enkoder_m": random.uniform(100.0, 101.0)}
    return raw_data

# funkcja zbierająca odczyty do dalszych obliczeń
def data_collector():
    Data_collection = [];
    for i in range(10):
        Data_collection.insert(i,raw_data_generator());
    return Data_collection

# funkcja sortująca dane do dalszych obliczeń
def data_sorter(Data_collection,key):
    Sorted_data=[]
    e = 0
    while e < len(Data_collection):
        Sorted_data.insert(e,Data_collection[e][key])
        e += 1

    return Sorted_data


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
    print("Wartości uśrednione dla 10 pomiarów: ")
    print("średnia wartość mag_x: "+str(data_averaging(data_sorter(data_collector(),"magnetometr_x"))))
    print("średnia wartość mag_y: "+str(data_averaging(data_sorter(data_collector(),"magnetometr_y"))))
    print("średnia wartość mag_z: "+str(data_averaging(data_sorter(data_collector(),"magnetometr_z"))))
    print("średnia wartość akc_x: "+str(data_averaging(data_sorter(data_collector(),"akcelerometr_x"))))
    print("średnia wartość akc_y: "+str(data_averaging(data_sorter(data_collector(),"akcelerometr_y"))))
    print("średnia wartość akc_z: "+str(data_averaging(data_sorter(data_collector(),"akcelerometr_z"))))
    print("średnia wartość bar_t: "+str(data_averaging(data_sorter(data_collector(),"barometr_t"))))
    print("średnia wartość bar_p: "+str(data_averaging(data_sorter(data_collector(),"barometr_p"))))
    print("średnia wartość bar_h: "+str(data_averaging(data_sorter(data_collector(),"barometr_h"))))
    print("średnia wartość enk_h: "+str(data_averaging(data_sorter(data_collector(),"enkoder_m"))))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


