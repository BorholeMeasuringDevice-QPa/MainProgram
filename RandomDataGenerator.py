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

def listed_data_generator():
    data_list=[random.uniform(30.0,40.0),random.uniform(20.0,30.0),random.uniform(10.0,20.0),
               random.uniform(40.0, 50.0),random.uniform(50.0,60.0),random.uniform(60.0,70.0),
               random.uniform(20.0, 30.0),random.uniform(1000.0,1100.0),random.uniform(100.0,101.0),
               random.uniform(100.0, 101.0)]
    raw_data=""
    for e in data_list:
        raw_data+="|"+str(e)

    return raw_data



