import string
import numpy as np
import os

def shell(user, device, measurement):
  #Creates an interface for users to add in their data
  firstName = input("Enter your first name: ")
  lastName = input("Enter your last name: ")
  gender = input("Enter your gender: ")
  contact = input("Enter your contact number: ")
  roleID = input("Enter your roleID (1: Patient 2: Doctor 3: administrator 4: developer): ")
  dob = input("Enter your date of birth in MMDDYYYY format: ")
  address = input("Enter your address: ")
  billing = input("Enter your billing info: ")
  allergies = input("Enter your allergies: ")
  medicalID = input("Enter your medical ID: ")
  family = input("Enter your number of people in your family: ")
  medicalHistory = input("Enter your medical history: ")
  primaryCare = input("Enter your primary care physician: ")
  medicalCondition = input("Enter your medical condition: ")
  emergencyContact = input("Enter your emergencyContact: ")
  #Creating dictionary from users input data
  user["first name"]= firstName
  user["last name"]= lastName
  user["gender"] = gender
  user["contact"]=contact
  user["roleID"]=roleID
  user["dob"]=dob
  user["address"]=address
  user["billing"]=billing
  user["allergies"]=allergies
  user["medicalID"]=medicalID
  user["family"]=family
  user["medicalHistory"]=medicalHistory
  user["primaryCare"]=primaryCare
  user["medicalCondition"]=medicalCondition
  user["emergencyContact"]=emergencyContact
  #Creates an interface for users to add in their device data
  deviceID = input("Enter device ID (1: thermometer, 2: weight scale, 3: BP measuror, 4: pulse meter, 5: oximeter, 6: glucometer, 7: height): ")
  dateofPurchase = input("Enter the date of purchase of the device: ")
  macAddress = input("Enter the MAC Address: ")
  frameworkVersion = input("Enter the framework version: ")
  softwareVersion = input("Enter the software version: ")
  #Creating dictionary from users input device data
  device["deviceID"]=deviceID
  device["dateofPurchase"]=dateofPurchase
  device["macAddress"]=macAddress
  device["frameworkVersion"]=frameworkVersion
  device["softwareVersion"]=softwareVersion
  #Creates an interface for users to add in their measurements
  ameasurement = input("Enter the measurement: ")
  #Creating dictionary from users measurements
  measurement["deviceID"]=deviceID
  measurement["ameasurement"]=ameasurement

def main():
    listofUsers = []
    listofdevices = []
    listofmeasurements = []
    user = {}
    device = {}
    measurement = {}
    shell(user, device, measurement)
    listofUsers.append(user)
    listofdevices.append(device)
    listofmeasurements.append(measurement)

if __name__=="__main__":
    main()
