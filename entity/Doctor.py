class Doctor:
    def __init__(self, doctorId, firstName, lastName, specialization, contactNumber):
        self.__doctorId = doctorId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__specialization = specialization
        self.__contactNumber = contactNumber

    @property
    def _doctorId(self):
        return self.__doctorId

    @_doctorId.setter
    def _doctorId(self, value):
        self.__doctorId = value

    @property
    def _firstName(self):
        return self.__firstName

    @_firstName.setter
    def _firstName(self, value):
        self.__firstName = value

    @property
    def _lastName(self):
        return self.__lastName

    @_lastName.setter
    def _lastName(self, value):
        self.__lastName = value

    @property
    def _specialization(self):
        return self.__specialization

    @_specialization.setter
    def _specialization(self, value):
        self.__specialization = value

    @property
    def _contactNumber(self):
        return self.__contactNumber

    @_contactNumber.setter
    def _contactNumber(self, value):
        self.__contactNumber = value
    
    def __str__(self):
        return f"Doctor ID: {self.__doctorId}\nFirst Name: {self.__firstName}\nLast Name: {self.__lastName}\nSpecialization: {self.__specialization}\nContact Number: {self.__contactNumber}\n"
