from typing import List
import pyodbc
from dao.IHospital_Service import IHospitalService
from entity.appointment import Appointment
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException
from util.PropertyUtil import PropertyUtil


class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        try:
            # Connect to the database using the connection string obtained from PropertyUtil
            self.connection = pyodbc.connect(PropertyUtil.getPropertyString())
            self.cursor = self.connection.cursor()
            print("Database connection successful")
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def getAppointmentById(self, appointmentId: int) -> Appointment:
        try:
            query = "SELECT * FROM Appointment WHERE appointmentId = ?"
            self.cursor.execute(query, (appointmentId,))
            row = self.cursor.fetchone()
            if row:
                appointment = Appointment(*row)
                return appointment
            else:
                return None
        except pyodbc.Error as e:
            print(f"Error fetching appointment by ID: {e}")
            raise

    def getAppointmentsForPatient(self, patientId: int) -> List[Appointment]:
        try:
            query = "SELECT * FROM Appointment WHERE patientId = ?"
            self.cursor.execute(query, (patientId,))
            rows = self.cursor.fetchall()
            return [Appointment(*row) for row in rows]
        except pyodbc.Error as e:
            print(f"Error fetching appointments for patient: {e}")
            raise

    def getAppointmentsForDoctor(self, doctorId: int) -> List[Appointment]:
        try:
            query = "SELECT * FROM Appointment WHERE doctorId = ?"
            self.cursor.execute(query, (doctorId,))
            rows = self.cursor.fetchall()
            return [Appointment(*row) for row in rows]
        except pyodbc.Error as e:
            print(f"Error fetching appointments for doctor: {e}")
            raise

    def scheduleAppointment(self, appointment):
        try:
            query = "INSERT INTO Appointment (appointmentId,patientId, doctorId, appointmentDate, description) VALUES (?,?, ?, ?, ?)"
            self.cursor.execute(query, (
            appointment._appointmentId, appointment._patientId, appointment._doctorId, appointment._appointmentDate, appointment._description))
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error scheduling appointment: {e}")
            raise

    def updateAppointment(self, appointment):
        try:
            query = "UPDATE Appointment SET appointmentDate = ?, description = ? WHERE appointmentId = ?"
            self.cursor.execute(query, (appointment.appointmentDate, appointment.description, appointment.appointmentId))
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error updating appointment: {e}")
            raise

    def cancelAppointment(self, appointmentId):
        try:
            # Check if the appointment exists
            check_query = "SELECT COUNT(*) FROM Appointment WHERE appointmentId = ?"
            self.cursor.execute(check_query, (appointmentId,))
            row = self.cursor.fetchone()
            if row[0] == 0:
                # If the appointment does not exist, raise PatientNumberNotFoundException
                raise PatientNumberNotFoundException("Appointment not found.")

            # Delete the appointment
            delete_query = "DELETE FROM Appointment WHERE appointmentId = ?"
            self.cursor.execute(delete_query, (appointmentId,))
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error cancelling appointment: {e}")
            raise
