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
Interface for devices to interact with the system.
