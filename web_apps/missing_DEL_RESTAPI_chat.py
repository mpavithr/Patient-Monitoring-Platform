import json
import requests

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

def correct_keys_for_chat_json(device_list):
    correct_keys = 1
    for each_device_dict in device_list:
        if type(each_device_dict) is not dict:
            correct_keys = 0
            break
        res = list(each_device_dict.keys())
        if res[0] != 'timestamp':
            correct_keys = 0
            break
        if res[1] != 'sender_id':
            correct_keys = 0
            break
        if res[2] != 'reciever_id':
            correct_keys = 0
            break
        if res[3] != 'text':
            correct_keys = 0
            break
        if res[4] != 'attachment_video_url':
            correct_keys = 0
            break
        if res[5] != 'attachment_audio_url':
            correct_keys = 0
            break
        if res[6] != 'attachment_image_url':
            correct_keys = 0
            break
        if res[7] != 'attachment_file_url':
            correct_keys = 0
            break
    return correct_keys


def correct_value_for_chat_json(device_list):
    correct_values = 1
    for each_device_dict in device_list:
        if type(each_device_dict) is not dict:
            correct_values = 0
            break
        if not isinstance(each_device_dict['timestamp'],str):
            correct_values = 0
            break
        if not isinstance(each_device_dict['sender_id'],int):
            correct_values = 0
            break
        if not isinstance(each_device_dict['reciever_id'],int):
            correct_values = 0
            break
        if not isinstance(each_device_dict['text'],str):
            correct_values=0
            break
        if not isinstance(each_device_dict['attachment_video_url'],str):
            correct_values=0
            break
        if not isinstance(each_device_dict['attachment_audio_url'],str):
            correct_values=0
            break
        if not isinstance(each_device_dict['attachment_image_url'],str):
            correct_values=0
            break
        if not isinstance(each_device_dict['attachment_file_url'],str):
            correct_values=0
            break
    return correct_values


if __name__ == "__main__":
    BASE = "http://127.0.0.1:5000/"
    file = str(input("Enter chat file in json format:"))
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
    chat_data = data[res]
    #Now the measurements part
    if correct_keys_for_chat_json(chat_data) == 0:
        print("The chat file you have entered has incorrect keys. Please enter a valid chat file in json format.")
        exit()
    if correct_value_for_chat_json(chat_data) == 0:
        print("The chat file you entered has incorrect values. Please enter a valid chat file in json format.")
        exit()
    for i in range(len(chat_data)):
        response = requests.post(BASE + "chat/" + str(i), chat_data[i])
        print(response.json())
    input()
    #Trying to update
    response = requests.delete(BASE + "chat/9")
    print(response)
    '''
    for i in range(len(device_data)):
            response = requests.post(BASE + "device/" + str(i), device_data[i])
            print(response.json())
    input()
    #Trying to update
    response = requests.put(BASE + "device/3", {"name":"Thermometer","firmware_version":110,"serial_number":2342})
    print(response.json())
    input()
    response = requests.delete(BASE + "device/0")
    print(response)
    input()
    response = requests.get(BASE + "device/6")
    print(response.json())
    file = str(input("Enter patient data file in json format:"))
    jsonFlag = checkingForJSON(file)
    emptyFlag = checkingEmptyFile(file)
    if jsonFlag==0 or emptyFlag==0:
        exit()
    try:
        a_file = open(file)
    except IOError:
        print ("Could not open file, please close file!")
        exit()
    with a_file as f:
        data = json.load(f)
    patient_data = data["measurements"]
    for i in range(len(patient_data)):
        response = requests.post(BASE + "measurement/" + str(i), patient_data[i])
        print(response.json())
    input()
    response = requests.put(BASE + "measurement/1", {"measurement":112})
    print(response.json())
    input()
    response = requests.delete(BASE + "measurement/1")
    print(response)
    input()
    response = requests.get(BASE + "measurement/0")
    print(response.json())
    '''
