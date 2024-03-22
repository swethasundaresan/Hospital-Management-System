class Patient:
    def __init__(self, patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    @property
    def _patientId(self):
        return self.__patientId

    @_patientId.setter
    def _patientId(self, value):
        self.__patientId = value

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
    def _dateOfBirth(self):
        return self.__dateOfBirth

    @_dateOfBirth.setter
    def _dateOfBirth(self, value):
        self.__dateOfBirth = value

    @property
    def _gender(self):
        return self.__gender

    @_gender.setter
    def _gender(self, value):
        self.__gender = value

    @property
    def _contactNumber(self):
        return self.__contactNumber

    @_contactNumber.setter
    def _contactNumber(self, value):
        self.__contactNumber = value

    @property
    def _address(self):
        return self.__address

    @_address.setter
    def _address(self, value):
        self.__address = value