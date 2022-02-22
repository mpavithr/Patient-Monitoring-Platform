import requests
import json
'''
BASE = "http://127.0.0.1:5000/"

data = [{"patientName": "Meena", "date":"02/21/2022", "time":"07:24", "machineID":1,"measurement":98.4},
        {"patientName": "John", "date":"02/20/2022", "time":"19:39", "machineID":3,"measurement":92.0},
        {"patientName": "Mary", "date":"02/19/2022", "time":"23:59", "machineID":5,"measurement":70.0}]

for i in range(len(data)):
        response = requests.put(BASE + "device/" + str(i), data[i])
        print(response.json())

input()
response = requests.delete(BASE + "device/0")
print(response)
input()
response = requests.get(BASE + "device/6")
print(response.json())
'''
def errors_and_converting(device):
    if device["idDevice"] < 0 or device["idDevice"] > 10:
        print("Device you are using is not authenticated in our system. Try using another device.\n")

    #Checking for errors
    elif not isinstance(device["patientName"],str):
        print("Please send in the patient's valid name using english alphabets.\n")

    elif not isinstance(device["date"],str):
        print("Please send in the date the patient's measurement was taken in as a string format 'MM/DD/YYYY'.\n")

    #Add in checking whether date is a valid date
    #Add in checking whether time is a valid time
    elif not isinstance(device["time"],str):
        print("Please send in the time the patient's measurement was taken in as a string format 'HH:MM'.\n")

    elif not isinstance(device["machineID"],int):
        print("Please send in a valid machine ID NUMBER from 1 to 6 according to the machine type table.\n")

    elif device["machineID"] < 1 or device["machineID"] > 6:
        print("Please send in a valid machine ID NUMBER from 1 to 6 according to the machine type table.\n")

    #Add in checking whether measurement is valid corresponding to machineID
    elif not isinstance(device["measurement"],float):
        print("Please send in the patient's measurement in a float format.\n")

    else:
        num2str = str(device["idDevice"])
        with open('device_%s.txt'%num2str, 'w') as f:
            print(device, file=f)

def checkingForJSON(file):
    jsonFlag = 0
    if not file.endswith('.json'):
        print("Please enter a json file!!")
    else:
        jsonFlag=1
    return jsonFlag

def checkingEmptyFile(file):
    emptyFlag = 0
    if not file:
        print("Please enter a json file!! Don't leave it empty!")
    else:
        emptyFlag=1
    return emptyFlag

if __name__ == "__main__":
    BASE = "http://127.0.0.1:5000/"
    file = str(input("Enter device file in json format:"))
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
    #Hardcoding device authentication ids
    device_authentication_ids = [i for i in range(11)]
    device_data = data["devices"]
    for device in data["devices"]:
        errors_and_converting(device)
    print("Done with checking device data fields!")
    #i here refers to the device entry in the device module system, not the device id
    for i in range(len(device_data)):
            response = requests.post(BASE + "device/" + str(i), device_data[i])
            print(response.json())
    input()
    #Trying to update
    response = requests.put(BASE + "device/0", {"patientName":"Meena"})
    print(response.json())
    input()
    response = requests.delete(BASE + "device/0")
    print(response)
    input()
    response = requests.get(BASE + "device/6")
    print(response.json())
