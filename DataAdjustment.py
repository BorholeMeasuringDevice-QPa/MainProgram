import RandomDataGenerator as R

# funkcja sortująca dane do dalszych obliczeń
def data_sorter(Data_collection,key):
    Sorted_data=[]
    e = 0
    while e < len(Data_collection):
        Sorted_data.insert(e,Data_collection[e][key])
        e += 1

    return Sorted_data

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
    "magnetometr_x":data_averaging(data_sorter(data_collector(10),"magnetometr_x")),
    "magnetometr_y":data_averaging(data_sorter(data_collector(10),"magnetometr_y")),
    "magnetometr_z":data_averaging(data_sorter(data_collector(10),"magnetometr_z")),
    "akcelerometr_x":data_averaging(data_sorter(data_collector(10),"akcelerometr_x")),
    "akcelerometr_y":data_averaging(data_sorter(data_collector(10),"akcelerometr_y")),
    "akcelerometr_z":data_averaging(data_sorter(data_collector(10),"akcelerometr_z")),
    "barometr_t":data_averaging(data_sorter(data_collector(10),"barometr_t")),
    "barometr_p":data_averaging(data_sorter(data_collector(10),"barometr_p")),
    "barometr_h":data_averaging(data_sorter(data_collector(10),"barometr_h")),
    "enkoder_m":data_averaging(data_sorter(data_collector(10),"enkoder_m"))}
    return Final_result

# funkcja zbierająca odczyty do dalszych obliczeń
def data_collector(amount):
    Data_collection = [];
    for i in range(amount):
        Data_collection.insert(i,R.raw_data_generator());
    return Data_collection

