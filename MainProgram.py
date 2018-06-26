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

#funkcja uśredniająca dane
def data_averaging(data):
    sum=0
    for e in data:
        sum+=e
    average=round(sum/len(data),5)
    return average

# funkcja zbierająca wynik po uśrednieniu
def data_final_result():
    Final_result={
    "magnetometr_x":data_averaging(data_sorter(data_collector(),"magnetometr_x")),
    "magnetometr_y":data_averaging(data_sorter(data_collector(),"magnetometr_y")),
    "magnetometr_z":data_averaging(data_sorter(data_collector(),"magnetometr_z")),
    "akcelerometr_x":data_averaging(data_sorter(data_collector(),"akcelerometr_x")),
    "akcelerometr_y":data_averaging(data_sorter(data_collector(),"akcelerometr_y")),
    "akcelerometr_z":data_averaging(data_sorter(data_collector(),"akcelerometr_z")),
    "barometr_t":data_averaging(data_sorter(data_collector(),"barometr_t")),
    "barometr_p":data_averaging(data_sorter(data_collector(),"barometr_p")),
    "barometr_h":data_averaging(data_sorter(data_collector(),"barometr_h")),
    "enkoder_m":data_averaging(data_sorter(data_collector(),"enkoder_m"))}
    return Final_result

#funckja wyświetlająca dane
def data_viewer():
    return True

def main(args):
    #print("Wartości uśrednione dla 10 pomiarów: ")
     file=create_a_file()
     data1=data_final_result()
     data2 = data_final_result()
     data3 = data_final_result()
     write_to_file(data1,file)
     write_to_file(data2,file)
     write_to_file(data3,file)
    #print(data_final_result())
     return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


