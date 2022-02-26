# Patient-Monitoring-Platform

The following readme contains information about this project and the branching strategy.

**Branching Strategy** - https://github.com/mpavithr/Patient-Monitoring-Platform/wiki/Branching-Strategy

**Description of the project**

This project is a platform to monitor patients at home or in the hospital.

There are 4 categories of users that will use this platform:
1. Patients
2. Medical Professionals
3. Administrator
4. Developers (app developers, device integrators, Machine learning scientists)

**What can each category of users do?**

Administrators can:
- Add users to the system: Users should be added to the system and cannot register before being added to the system
- Assign and Change Roles to users like Patient, Nurse, Doctor, Admin, Family member. Also, A user can have different roles, e.g., a user can be a patient and/or a doctor, A user can be a family member and/or a patient
- Ability to disable or enable any device maker or application developer

Medical Professionals can:
- Browse Patients
- Assign a medical device to a Patient
- Assign Alert and scheduling for medical measurement, e.g., Patient to measure blood pressure daily.  MP will receive an alert if it not done. Temperature is higher or lower than a value.  MP will get an alert if the measurement is outside acceptable range
- MP can input data for any patient
- MP can chat with patients using text, voice or videos.
- MP can read transcripts of Patient uploaded videos and messages
- MP can search for keywords in messages and chats
- MP have a calendar where they can show open time slots for appointments
- MP can see all appointments booked at any time

Patients can:
- Enter measurement at any time
- Write a text or upload video or voice message to the MP
- Book an appointment with the MP
- View their medical measurements

**Modules for the Platform**

For the users to be able to do the things they need to do, there will be several modules which are Device Module, Calendar Module, Alerts module, Chat Module, Voice transcriber, Administrative module, Data Management Module, API Module

Device Module: 
<<<<<<< HEAD
Can take in information about measurements that a device has measured for each user.
(Previous understanding - Contains Device Table, Measurement Table, User Table
Who can access the tables? Patient can enter measurements and devices to the device and measurement and user table.
Medical Professionals can view the entire measurement, device and user table as well as enter information to it.

Device table describes type of device, what it measures and in which units and other details about the device. 
Measurement table contains measurements and has a column for device id and User ID linking the device and user tables with the measurement table.)

**Branching Strategy**

This project follows feature branching for continuous delivery and continuous integration. Each module to be developed in this project is considered a feature.

The following are the branches:
1. Main Branch - Everything in this branch is ready for production. Anyone can use the code and files contained in this branch.
2. Device Branch - This branch is for the code and files needed for the device module. Once developed, tested and pulled and reviewed, it's merged into the main branch.
Similarly, there will be branches for Calendar, alert, Chat, Voice and API modules which will all be merged back to the main branch once tested and developed.


=======
Interface for devices to interact with the system.
>>>>>>> origin/main
