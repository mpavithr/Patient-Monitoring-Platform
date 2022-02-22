import json

def errors_and_converting(device):
    if device["device_id"] < 0 or device["device_id"] > 10:
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
        num2str = str(device["device_id"])
        with open('device_%s.txt'%num2str, 'w') as f:
            print(device, file=f)


if __name__ == "__main__":
    file = str(input("Enter device file in json format:"))
    if not file.endswith('.json'):
        print("Please enter a json file!!")
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
    for device in data["devices"]:
        errors_and_converting(device)
    print("Done!")
