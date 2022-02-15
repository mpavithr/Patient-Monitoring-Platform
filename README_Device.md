The main branch as of 2/13/2022 fulfills phase 0 of project.
The Device branch as of 2/13/2022 fulfills phase 1 of project.

In this branch there is one python file:

entering_in_shell.py - when running this file, users will be able to enter in their user information, device information and measurements through the command line creating a shell for the device interface.

The file will then use the information recieved through the command line and put the information into tables according to the schemata in main branch (Project 2.xlsx) thus creating a device interface.

When running the file, it creates an example simulation.

So there will be an entry in a user table, device table, and measurement table every time the file is run.

Tables will be for now python dictionaries for each user, each device and each measurement.

Unit Testing involves creating unit tests for whether the information provided by a user is valid for the field and whether empty fields are empty in the table/dict.

User list will contain dictionaries of all users.
Device list will contain dictionaries of all devices.
Measurement list will contain measurements of all measurements.

EDIT - I am going to tweak the device module. entering_in_shell.py remains for now. device_interface.py takes in a json file for a device, the json file contains device measurement data for all patients the device has used, tests for all the valid fields, and if it is correct, it outputs a text file.

JSON File Example:
"users":[
  {
    userID:
    measurement:
  }
  {
    userID:
    measurement:
  }
]

