class Appointment:
    def __init__(self, appointmentId, patientId,doctorId, appointmentDate, description):
        self.__appointmentId = appointmentId
        self.__patientId = patientId
        self.__doctorId = doctorId
        self.__appointmentDate = appointmentDate
        self.__description = description

    @property
    def _appointmentId(self):
        return self.__appointmentId

    @_appointmentId.setter
    def _appointmentId(self, value):
        self.__appointmentId = value

    @property
    def _patientId(self):
        return self.__patientId

    @_patientId.setter
    def _patientId(self, value):
        self.__patientId = value

    @property
    def _doctorId(self):
        return self.__doctorId

    @_doctorId.setter
    def _doctorId(self, value):
        self.__doctorId = value

    @property
    def _appointmentDate(self):
        return self.__appointmentDate

    @_appointmentDate.setter
    def _appointmentDate(self, value):
        self.__appointmentDate = value

    @property
    def _description(self):
        return self.__description

    @_description.setter
    def _description(self, value):
        self.__description = value

    def __str__(self):
        return f"Appointment ID: {self._appointmentId}\nPatient ID: {self._patientId}\nDoctor ID: {self._doctorId}\nAppointment Date: {self._appointmentDate}\nDescription: {self._description}\n"
