The main branch as of 2/13/2022 fulfills phase 0 of project.
The Device branch as of 2/13/2022 fulfills phase 1 of project.
The Device branch as of 2/22/2022 fulfills phase 2 of project.

**This branch is for the device module. The device module is an interface where devices can interact with the system.**

deviceRESTAPI.py - this code integrates the device module into a RESTFUL system. Implements PUT, POST, GET, DELETE commands where the user using the module can insert measurements of a patient into a database (for now, this database is a dictionary), update measurements, get measurements and delete measurements.

Each entry in the device module has the following fields:
1. Device_id - unique id of a device, every device has one, for authentication purposes
2. patientName - name of the patient whose measurement is being taken
3. date - date the patient took the measurement with the device in "MM/DD/YYYY" format
4. time - time the patient took the measurement with the device in "HH:MM" format
5. machineID - each device corresponds to a machine, the machine ids are listed as follows (1:Thermometer, 2:BP Monitor, 3:Oximeter, 4:Weight, 5:Glucometer, 6:Stadiometer) 
6. measurement - the actual measurement recorded by the device

deviceAPIwebAppTest1.py - this code takes in a json file. Checks whether it is a valid json file. This json file contains information about devices and each device has the following fields corresponding to the entries in the device module: 

1. Device_id - unique id of a device, every device has one, for authentication purposes
2. patientName - name of the patient whose measurement is being taken
3. date - date the patient took the measurement with the device in "MM/DD/YYYY" format
4. time - time the patient took the measurement with the device in "HH:MM" format
5. machineID - each device corresponds to a machine, the machine ids are listed as follows (1:Thermometer, 2:BP Monitor, 3:Oximeter, 4:Weight, 5:Glucometer, 6:Stadiometer) 
6. measurement - the actual measurement recorded by the device

In this file, I have hardcoded all the device IDs for device authentication. If a device_id value of a device in the json file is not present in the hardcoded values, the device is invalid and will not be expected and the program will ask the third party user to try again. 

this code file checks for errors in the data fields of the device whether it is given in the correct format. If everything looks correct. Each device prints its information into a text file. 

Unit Tests include:
Unit Test 1: Checking whether the input file can be opened.
Unit Test 2: Checking whether the input file is in json format.

This fulfils phase 1 of the project.

JSON File Example:
{
    "devices":[
        {
            "device_id": 2,
            "patientName": "John Smith",
            "date": "01/10/2022",
            "time": "07:53",
            "machineID": 2,
            "measurement": 120.00
        },
        {
            "device_id": 4,
            "patientName": "Jane Doe",
            "date": "02/14/2022",
            "time": "20:56",
            "machineID": 6,
            "measurement": 66.00
        }
    ]
}
