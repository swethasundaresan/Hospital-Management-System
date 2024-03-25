CREATE DATABASE HospitalDB;
USE HospitalDB;
CREATE TABLE Patient (
    patientId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dateOfBirth DATE,
    gender VARCHAR(10),
    contactNumber VARCHAR(20),
    address VARCHAR(255)
);
INSERT INTO Patient VALUES (1,'Swetha','Sundar','2002-12-12','female','9876543219','Anna Park, Salem'),
(2,'Raj','Kumar','1999-10-09','male','8579867462','PB Colony, Coimbatore'),
(3,'Sheela','Sekar','2004-09-10','female','8567983676','VR Street, Madurai');

CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    specialization VARCHAR(100),
    contactNumber VARCHAR(20)
);

INSERT INTO Doctor VALUES(100,'Ram','Krishnan','Neurologist','8585645675'),
(101,'Sanjith','Jha','Cardiologist','9465347327'),
(102,'Ranjeeta','Singh','Gynecologist','9635426369');

CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY,
    patientId INT,
    doctorId INT,
    appointmentDate DATETIME,
    description VARCHAR(255),
    FOREIGN KEY (patientId) REFERENCES Patient(patientId),
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
);

INSERT INTO Appointment VALUES 
(1,1,101,'2024-03-21','High blood pressure'),
(2,3,100,'2024-03-10','migraine'),
(3,2,102,'2024-03-22','Check-Up');



