
class Patient:

    def __init__(self, patientID, name, address, phone_no):
        self.patientID = patientID
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.checked_in = False

    def check_in():
        """ Allows patient to check in """
        self.checked_in = True

    def change_address(new_address):
        """ Updates address for patient """
        self.address = new_address

    def change_phone_no(new_phone_no):
        """ Updates phone number for patient """
        self.phone_no = new_phone_no