from entity import appointment
from dao.hospital_service_impl import HospitalServiceImpl
from entity.appointment import Appointment


class MainModule:
    def __init__(self):
        self.hospital_service = HospitalServiceImpl()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Get appointment by ID")
            print("2. Get appointments for patient")
            print("3. Get appointments for doctor")
            print("4. Schedule appointment")
            print("5. Update appointment")
            print("6. Cancel appointment")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.get_appointment_by_id()
            elif choice == '2':
                self.get_appointments_for_patient()
            elif choice == '3':
                self.get_appointments_for_doctor()
            elif choice == '4':
                self.schedule_appointment()
            elif choice == '5':
                self.update_appointment()
            elif choice == '6':
                self.cancel_appointment()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_appointment_by_id(self):
        appointment_id = int(input("Enter appointment ID: "))
        appointment = self.hospital_service.getAppointmentById(appointment_id)
        if appointment:
            print("Appointment details:")
            print(appointment)
        else:
            print("Appointment not found.")

    def get_appointments_for_patient(self):
        patient_id = int(input("Enter patient ID: "))
        appointments = self.hospital_service.getAppointmentsForPatient(patient_id)
        if appointments:
            print("Appointments for patient:")
            for appointment in appointments:
                print(appointment)
        else:
            print("No appointments found for the patient.")

    def get_appointments_for_doctor(self):
        doctor_id = int(input("Enter doctor ID: "))
        appointments = self.hospital_service.getAppointmentsForDoctor(doctor_id)
        if appointments:
            print("Appointments for doctor:")
            for appointment in appointments:
                print(appointment)
        else:
            print("No appointments found for the doctor.")

    def schedule_appointment(self):
        # Collect appointment details from user input
        appointment_id = int(input("Enter appointment ID: "))
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        appointment_date = input("Enter appointment date (YYYY-MM-DD HH:MM:SS): ")
        description = input("Enter description: ")

        # Create an Appointment object
        appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)

        # Call the service method to schedule the appointment
        success = self.hospital_service.scheduleAppointment(appointment)
        if success:
            print("Appointment scheduled successfully.")
        else:
            print("Failed to schedule appointment.")

    def update_appointment(self):
        appointment_id = int(input("Enter appointment ID to update: "))
        # Retrieve the appointment details based on the appointment ID
        appointment = self.hospital_service.getAppointmentById(appointment_id)
        if appointment:
            try:
                # Prompt the user to enter updated details
                new_appointment_date = input("Enter new appointment date (YYYY-MM-DD HH:MM:SS): ")
                new_description = input("Enter new description: ")

                # Update the appointment with the new details
                appointment.appointmentDate = new_appointment_date
                appointment.description = new_description
                appointment.appointmentId = appointment_id

                # Execute the update query to update the appointment in the database
                success = self.hospital_service.updateAppointment(appointment)
                if success:
                    print("Appointment updated successfully.")
                else:
                    print("Failed to update appointment.")
            except Exception as e:
                print(f"Error updating appointment: {e}")
        else:
            print("Appointment not found.")

    def cancel_appointment(self):
        appointment_id = int(input("Enter appointment ID to cancel: "))
        success = self.hospital_service.cancelAppointment(appointment_id)
        if success:
            print("Appointment cancelled successfully.")
        else:
            print("Failed to cancel appointment.")


if __name__ == "__main__":
    main_module = MainModule()
    main_module.menu()
