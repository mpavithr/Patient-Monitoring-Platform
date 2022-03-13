#import requests
import json

def checkingForJSON(file):
    jsonFlag = 0
    if not file.endswith('.json'):
        print("Please enter a json file!!\n")
    else:
        jsonFlag=1
    return jsonFlag

def checkingEmptyEntryforFile(file):
    emptyFlag = 0
    if not file:
        print("Please enter a json file!! Don't leave it empty!")
    else:
        emptyFlag=1
    return emptyFlag

def checkingEmptyFile(file):
    with open(file, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
           return True
    return False

def getList(dict):
    return list(dict.keys())

def correct_keys_for_device_json(device_list):
    correct_keys = 1
    for each_device_dict in device_list:
        if type(each_device_dict) is not dict:
            correct_keys = 0
            break
        res = list(each_device_dict.keys())
        if len(res) != 6:
            correct_keys = 0
            break
        if res[0] != 'name':
            correct_keys = 0
            break
        if res[1] != 'firmware_version':
            correct_keys = 0
            break
        if res[2] != 'date_of_purchase':
            correct_keys = 0
            break
        if res[3] != 'serial_number':
            correct_keys = 0
            break
        if res[4] != 'mac_address':
            correct_keys = 0
            break
        if res[5] != 'machineID':
            correct_keys = 0
            break
    return correct_keys

def correct_keys_for_measurement_json(measurement_list):
    correct_keys = 1
    for each_measure_dict in measurement_list:
        if type(each_measure_dict) is not dict:
            correct_keys = 0
            break
        res = list(each_measure_dict.keys())
        if len(res) != 7:
            correct_keys = 0
            break
        if res[0] != 'device_id':
            correct_keys = 0
            break
        if res[1] != 'patient_id':
            correct_keys = 0
            break
        if res[2] != 'assigner_id':
            correct_keys = 0
            break
        if res[3] != 'machineID':
            correct_keys = 0
            break
        if res[4] != 'date_assigned':
            correct_keys = 0
            break
        if res[5] != 'date_returned':
            correct_keys = 0
            break
        if res[6] != 'measurement':
            correct_keys = 0
            break
    return correct_keys

def correct_value_for_device_json(device_list):
    correct_values = 1
    for each_device_dict in device_list:
        if type(each_device_dict) is not dict:
            correct_values = 0
            break
        if not isinstance(each_device_dict['name'],str):
            correct_values = 0
            break
        if not isinstance(each_device_dict['firmware_version'],float):
            correct_values = 0
            break
        if not isinstance(each_device_dict['date_of_purchase'],str):
            correct_values = 0
            break
        if not isinstance(each_device_dict['serial_number'],int):
            correct_values=0
            break
        if not isinstance(each_device_dict['mac_address'],str):
            correct_values=0
            break
        if not isinstance(each_device_dict['machineID'],int):
            correct_values=0
            break
    return correct_values

def correct_value_for_measurement_json(measurement_list):
    correct_values = 1
    for each_measure_dict in measurement_list:
        if type(each_measure_dict) is not dict:
            correct_values = 0
            break
        if not isinstance(each_measure_dict['device_id'],int):
            correct_values = 0
            break
        if not isinstance(each_measure_dict['patient_id'],int):
            correct_values = 0
            break
        if not isinstance(each_measure_dict['assigner_id'],int):
            correct_values = 0
            break
        if not isinstance(each_measure_dict['machineID'],int):
            correct_values=0
            break
        if not isinstance(each_measure_dict['date_assigned'],str):
            correct_values=0
            break
        if not isinstance(each_measure_dict['date_returned'],str):
            correct_values=0
            break
        if not isinstance(each_measure_dict['measurement'],float):
            correct_values=0
            break
    return correct_values


if __name__ == "__main__":
    BASE = "http://127.0.0.1:5000/"
    file = str(input("Enter device file in json format:"))
    jsonFlag = checkingForJSON(file)
    emptyFlag = checkingEmptyEntryforFile(file)
    try:
        a_file = open(file)
    except IOError:
        print ("Could not open file, please close file!")
        exit()
    if checkingEmptyFile(file) is True:
        print("The file you have entered is empty, please enter a valid device file in json format")
        exit()

    if jsonFlag==0 or emptyFlag==0:
        exit()
    with a_file as f:
        data = json.load(f)
    res = list(data.keys())[0]
    device_data = data[res]
    #Now the measurements part
    file = str(input("Enter measurement file in json format:"))
    jsonFlag = checkingForJSON(file)
    emptyFlag = checkingEmptyEntryforFile(file)
    try:
        a_file = open(file)
    except IOError:
        print ("Could not open file, please close file!")
        exit()
    if checkingEmptyFile(file) is True:
        print("The file you have entered is empty, please enter a valid device file in json format")
        exit()

    if jsonFlag==0 or emptyFlag==0:
        exit()
    
    with a_file as f:
        data = json.load(f)
    res = list(data.keys())[0]
    measurement_data = data[res]
    if correct_keys_for_device_json(device_data) == 0:
        print("The device file you have entered has incorrect keys. Please enter a valid device file in json format.")
        exit()
    if correct_keys_for_measurement_json(measurement_data)==0:
        print("The measurement file you have entered has incorrect keys. Please enter a valid measurement file in json format.")
        exit()
    if correct_value_for_device_json(device_data) == 0:
        print("The device file you entered has incorrect values. Please enter a valid device file in json format.")
        exit()
    if correct_value_for_measurement_json(measurement_data)==0:
        print("The measurement file you entered has incorrect values. Please enter a valid measurement file in json format.")
        exit()
